import textwrap, os, re
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



def page_breaker(jinja_context):  # FIXME unused?
    return textwrap.dedent(
        """
        
        .. raw:: pdf
        
           PageBreak   
           
        """)


def spacer(jinja_context):  # FIXME unused?
    return textwrap.dedent(
        """
        
        .. raw:: pdf
        
           Spacer 0 25
           
        """)


def _ensure_intial_game_data_dump_is_present(initial_game_data_dump_file):
    if not os.path.exists(initial_game_data_dump_file):

        # WORKAROUND FOR DEV ENV SETUP
        os.environ["DJANGO_SETTINGS_MODULE"] = settings_module = \
            "pychronia_game.tests.persistent_mode_settings"  # with DB not in temp dir

        from pychronia_game.scripts import dump_initial_game_yaml;
        dump_initial_game_yaml.execute(initial_game_data_dump_file)



def _extract_ingame_clues_text_from_docx(clues_file):
    """
    Extract texts and comments from Office DOCX file.

    # THIS SEEMS UNUSED #
    """
    import docx2txt
    # we may also use "img_dir" parameter to write images in /tmp/img_dir
    text = docx2txt.process(clues_file)
    return text


def _extract_ingame_clues_text_from_odt(clues_file):
    """
    Extract texts and comments from LibreOffice ODT file.
    """
    import odt2txt
    odt = odt2txt.OpenDocumentTextFile(clues_file)
    text = odt.toString()
    return text


def _generate_clues_pdfs_from_main_odt_document(input_doc, clues_parts, output_dir):
    current_page = 1
    for idx, (basename, pages_count) in enumerate(clues_parts):
        prefix = ""  # or ("%02d_" % idx) if debugging needed
        output_pdf = os.path.join(output_dir, prefix + basename + ".pdf")
        variables = dict(input=input_doc,
                         output=output_pdf,
                         page_range='%s-%s' % (current_page, current_page + pages_count - 1))
        cmd = 'python unoconv.py -f pdf -o "%(output)s" -e PageRange=%(page_range)s "%(input)s"' % variables
        print(cmd)
        os.system(cmd)

        # IMPORTANT - remove GAMEMASTER ANNOTATIONS from PDF file
        # BEWARE, this seems to CORRUPT a bit the PDF, find a better REGEX someday
        with open(output_pdf, 'rb') as f:
            data = f.read()
        assert b'Annots' in data  # all clues have annotations regarding their purposes
        regex = br'/Annots\s*\[[^]]+\]'
        data = re.sub(regex, b'', data, flags=re.MULTILINE)
        assert b'Annots' not in data  # no more clues VISIBLE (but still present in sources alas)
        with open(output_pdf, 'wb') as f:
            f.write(data)

        current_page += pages_count



def build_mysteryparty_pdf(output_dir, filename_base,
                        generate_rst_from_parts, jinja_env, extra_args,
                        parts, title,
                        add_page_breaks,
                        with_decorations,
                        jinja_context,
                        skip_pdf_output,
                        toc_depth):
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
                                       extra_args=extra_args)

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
