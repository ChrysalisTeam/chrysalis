import textwrap, os, subprocess, sys
import time


import rpg_sheet_generator as rpg



def analyze_and_normalize_game_items(game_items_raw, important_marker: str):
    """Detect game items as normal or important, and buidl a data tree including this information"""
    game_items = []
    for pair in game_items_raw:
        assert len(pair) == 2, pair
        section, item_titles = pair
        section_item_structs = []
        section_is_important = (important_marker in section)
        section = section.replace(important_marker, "")
        for item_title in item_titles:
            title_is_important = (important_marker in item_title)
            item_title = item_title.replace(important_marker, "").strip()
            section_item_struct = {
                "item_is_important": section_is_important or title_is_important,
                "item_label": item_title
            }
            section_item_structs.append(section_item_struct)
        game_items.append((section, section_item_structs))
    return game_items



def spacer(jinja_context):
    return textwrap.dedent(
        """
        
        .. raw:: pdf
        
           Spacer 0 25
           
        """)


def _ensure_intial_game_data_dump_is_present(initial_game_data_dump_file):
    if not os.path.exists(initial_game_data_dump_file):

        # WORKAROUND FOR DEV ENV SETUP
        os.environ["DJANGO_SETTINGS_MODULE"] = \
            "pychronia_game.tests.persistent_mode_settings"  # with DB not in temp dir

        from pychronia_game.scripts import dump_initial_game_yaml;
        dump_initial_game_yaml.execute(initial_game_data_dump_file)



def _extract_ingame_clues_text_from_odt(clues_file):
    """
    Extract texts and comments from LibreOffice ODT file.
    """
    import odt2txt
    odt = odt2txt.OpenDocumentTextFile(clues_file)
    text = odt.toString()
    return text


def _register_story_tags_from_clues_document(clues_document, jinja_env, language, comment_samples):
    """
    Fill fact/hint/symbol registries from the ingame clues ODT document, no rendered output is needed.

    Without translated document, the French one is used, but its symbol values aren't registered,
    since they would clash with those of translated templates.

    comment_samples maps languages to a text excerpt of a gamemaster comment of the matching document.
    """
    localized_clues_document = rpg.localize_source_filename(clues_document, language)
    is_translated = os.path.exists(localized_clues_document)  # always True for French
    document = localized_clues_document if is_translated else clues_document
    comment_sample = comment_samples[language if is_translated else rpg.DEFAULT_LANGUAGE]

    print("Extracting ingame clues text from ODT file %s" % document)
    content = _extract_ingame_clues_text_from_odt(document)
    if comment_sample not in content:  # the tags of gamemaster comments must be included
        raise RuntimeError("Comments of %s were not extracted (missing %r)" % (document, comment_sample))

    rpg.render_with_jinja_and_fact_tags(content=content,
                                        jinja_env=jinja_env,
                                        jinja_context=dict(register_symbols=is_translated))


def load_localized_rst_template(template_name, templates_roots, language):
    """
    Load the RST template "<name>_<language>.rst" from the first of templates_roots which contains it.
    """
    localized_template_name = rpg.localize_filename(template_name, language)
    for templates_root in templates_roots:
        rst_filepath = os.path.join(templates_root, localized_template_name)
        if os.path.exists(rst_filepath):
            return rpg.load_rst_file(rst_filepath)
    raise FileNotFoundError("Template %s not found in %s" % (localized_template_name, templates_roots))


def export_ingame_clues_pdfs(clues_document, clues_parts, output_dir, language):
    """
    SLOW - export the (translated) ingame clues ODT document into a myriad of small PDFs.
    """
    localized_clues_document = rpg.localize_source_filename(clues_document, language)
    if os.path.exists(localized_clues_document):
        _generate_clues_pdfs_from_main_odt_document(input_doc=localized_clues_document,
                                                    clues_parts=clues_parts,
                                                    output_dir=output_dir,
                                                    language=language)
    else:
        print("!!! Skipping export of ingame clues, since no translated document %s exists" % localized_clues_document)


def _normalize_pdf_text(text):
    return "".join(text.split()).lower()  # PDF text extraction is unreliable regarding spaces and line breaks


def _check_clues_first_pages(reader, clues_parts, language, input_doc):
    """
    Ensure that each clue starts on the expected page, by searching the text snippet declared for its first page
    (None meaning that this page has no text, eg. a picture), since page counts may change when editing the document.
    """
    errors = []
    current_page = 0
    for basename, pages_count, first_page_snippets in clues_parts:
        snippet = first_page_snippets[language] if first_page_snippets else None
        page_text = _normalize_pdf_text(reader.pages[current_page].extract_text() or "")
        if (snippet is None and page_text) or (snippet is not None and _normalize_pdf_text(snippet) not in page_text):
            errors.append("Page %s should start clue %s with %r, but contains %r" % (
                current_page + 1, basename, snippet, page_text[:60]))
        current_page += pages_count
    if errors:
        raise RuntimeError("Clue parts don't match the pages of %s, fix INGAME_CLUES_PARTS or the document:\n%s" % (
            input_doc, "\n".join(errors)))


def _get_resource_names_used(content_owner, reader):
    """
    Return the names of resources (fonts, images...) used by the content stream of a page or form XObject,
    including those used by its form XObjects which have no resources of their own.
    """
    from pypdf.generic import ContentStream, NameObject

    contents = content_owner.get_contents() if hasattr(content_owner, "get_contents") else content_owner
    if contents is None:
        return set()
    names = set()
    for operands, operator in ContentStream(contents, reader).operations:
        if operator == b"INLINE IMAGE":
            operands = list(operands["settings"].values())
        names.update(operand for operand in operands if isinstance(operand, NameObject))
    resources = content_owner.get("/Resources")
    xobjects = resources.get_object().get("/XObject", {}) if resources is not None else {}
    for name in names & set(xobjects.keys()):
        xobject = xobjects[name].get_object()
        if xobject.get("/Subtype") == "/Form" and "/Resources" not in xobject:
            names |= _get_resource_names_used(xobject, reader)  # such forms use the resources of their parent
    return names


def _prune_page_resources(page, reader):
    """
    Remove, from the resources of a page, those not used by its content stream.

    Office suites share the same resources (images, fonts...) between all pages, so without this,
    each clue PDF would embed all the images of the document, ie. spoil the other clues.
    """
    from pypdf.generic import DictionaryObject, NameObject

    resources = page.get("/Resources")
    if resources is None:
        return
    used_names = _get_resource_names_used(page, reader)
    pruned_resources = DictionaryObject()
    for category, entries in resources.get_object().items():
        entries = entries.get_object()
        if isinstance(entries, DictionaryObject):
            entries = DictionaryObject((name, value) for (name, value) in entries.items() if name in used_names)
        pruned_resources[NameObject(category)] = entries
    page[NameObject("/Resources")] = pruned_resources  # a copy, since the original is shared by all pages


def _generate_clues_pdfs_from_main_odt_document(input_doc, clues_parts, output_dir, language):
    """
    Export the whole ODT document to PDF once, then split it into one PDF per clue.

    Clue PDFs of output_dir are removed first, so that no clue of a failed export remains.

    IMPORTANT - GAMEMASTER COMMENTS of the document must not be exported.
    """
    from pypdf import PdfReader, PdfWriter

    full_pdf = os.path.join(output_dir, "_all_ingame_clues.pdf")
    for filepath in [full_pdf] + [os.path.join(output_dir, basename + ".pdf") for (basename, _count, _snippets) in clues_parts if basename]:
        if os.path.exists(filepath):
            os.remove(filepath)

    cmd = [sys.executable, "unoconv.py", "-f", "pdf", "-o", full_pdf,
           "-e", "ExportNotes=false", "-e", "ExportNotesInMargin=false", input_doc]
    print(cmd)
    try:
        subprocess.run(cmd, check=True)
        reader = PdfReader(full_pdf)
        if any(annot.get_object()["/Subtype"] == "/Text" for page in reader.pages for annot in page.get("/Annots", [])):
            raise RuntimeError("Gamemaster comments were exported to %s" % full_pdf)
        declared_pages_count = sum(pages_count for (_basename, pages_count, _snippets) in clues_parts)
        if declared_pages_count != len(reader.pages):  # else parts would be shifted
            raise RuntimeError("Clue parts declare %s pages, but %s has %s pages" % (declared_pages_count, input_doc, len(reader.pages)))
        _check_clues_first_pages(reader, clues_parts, language=language, input_doc=input_doc)

        current_page = 0
        for basename, pages_count, _snippets in clues_parts:
            if basename is None:  # pages to be skipped
                current_page += pages_count
                continue
            writer = PdfWriter()
            for page in reader.pages[current_page:current_page + pages_count]:
                _prune_page_resources(page, reader)
                writer.add_page(page)
            writer.write(os.path.join(output_dir, basename + ".pdf"))
            current_page += pages_count
    finally:
        if os.path.exists(full_pdf):
            os.remove(full_pdf)



def build_mysteryparty_pdf(output_dir, filename_base,
                        generate_rst_from_parts, jinja_env, extra_args,
                        parts, title,
                        add_page_breaks,
                        with_decorations,
                        jinja_context,
                        skip_pdf_output,
                        toc_depth,
                        language):
    assert callable(generate_rst_from_parts), generate_rst_from_parts

    if filename_base:
        print("Generating game pdf", filename_base)
    assert filename_base or skip_pdf_output

    rst_content = generate_rst_from_parts(
        parts,
        title=title,
        add_page_breaks=add_page_breaks,
        with_decorations=with_decorations,
        toc_depth=toc_depth,
        jinja_context=jinja_context)

    if jinja_context is not None:
        rst_content = rpg.render_with_jinja_and_fact_tags(
            content=rst_content,
            jinja_env=jinja_env,
            jinja_context=jinja_context)

    if not skip_pdf_output:
        filepath_base = os.path.join(output_dir, filename_base)
        rpg.convert_rst_content_to_pdf(filepath_base=filepath_base,
                                       rst_content=rst_content,
                                       conf_file="rst2pdf.conf",
                                       extra_args=extra_args,
                                       language=language)

    return rst_content


def _send_email_to_recipients(sender, recipients, text, subject, attachments=None, dry_run=True, smtp_conf=None):

    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    import smtplib

    assert len(recipients) <= 2, recipients  # safety

    attachments = attachments or []
    assert isinstance(attachments, list), attachments
    email_list = [elem.strip() for elem in recipients]
    del recipients

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = msg['Reply-to'] = sender
    msg['To'] = ", ".join(email_list)

    msg.preamble = 'Multipart message.\n'

    part = MIMEText(text, _charset='utf8')
    msg.attach(part)

    for attachement in attachments:
        part = MIMEApplication(open(attachement, "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachement))
        msg.attach(part)

    print("/!\\ %s SENDING EMAIL '%s' TO %s (attachments: %r)\n" % (
    "FAKE" if dry_run else "REALLY", subject, str(email_list), ", ".join(attachments)))

    if not dry_run:
        print(">>>>>> SMTP SETTINGS: %s" % str(smtp_conf))
        server = smtplib.SMTP(smtp_conf["host"])
        server.ehlo()
        server.starttls()
        server.login(smtp_conf["login"], smtp_conf["password"])
        res = server.sendmail(msg['From'], email_list, msg.as_string())
        time.sleep(10)  # else smtp freaks out...
        print("sendmail operation returned %s" % res)
        return res
    return None


def _send_character_sheets_via_email(all_data, player_names, subject, email_template, default_email_attachments, dry_run, allow_duplicate_emails=False, forced_recipient_email=None):
    # FIXME player_names is actually character_names !!!!!!!!!!!!!!

    # send already generated docs to players
    # BEWARE, first CHECK that filenames match file contents on all "clues" attachments!

    already_processed_recipients = set()
    smtp_conf = all_data["smtp_conf"]
    assert smtp_conf and isinstance(smtp_conf, dict), smtp_conf

    gamemaster_email = all_data["global_parameters"]["master_real_email"]
    assert gamemaster_email, gamemaster_email

    for player in sorted(player_names):
        player_data = all_data["character_properties"][player]
        player_data["mystery_party_date"] = all_data["mystery_party_date"]  # Especially interesting field
        #real_life_identity = player_data["real_life_identity"]
        real_life_email = forced_recipient_email if forced_recipient_email else player_data["real_life_email"]
        assert real_life_email, repr(real_life_email)
        official_name = player_data["official_name"]

        if not allow_duplicate_emails and (real_life_email in already_processed_recipients):
            # Here each player must have its own email
            raise ValueError('Duplicated specific recipient %s' % real_life_email)
        already_processed_recipients.add(real_life_email)

        email_attachments = [filename % dict(player=player) for filename in default_email_attachments]
        email_attachments += player_data["email_attachments"]
        email_attachments = [os.path.abspath(x) for x in email_attachments]

        for email_attachment in email_attachments:
            assert player in email_attachment or "common" in email_attachment or "documents" in email_attachment, email_attachment  # Do not mixup specific files
            assert os.path.isfile(email_attachment), email_attachment

        text = email_template % player_data

        _send_email_to_recipients(sender=gamemaster_email,
                                  recipients=[gamemaster_email, real_life_email],
                                  text=text,
                                  subject=subject % official_name,
                                  attachments=email_attachments,
                                  dry_run=dry_run,
                                  smtp_conf=smtp_conf)

if __name__ == '__main__':
    _send_email_to_recipients("webmaster@chrysalis-game.com",
                              recipients=["XXX"], text="test content", subject="test subject")
