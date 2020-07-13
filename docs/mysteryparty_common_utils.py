import textwrap, os, re
from time import time


import rpg_sheet_generator as rpg



PLAYER_INITIAL_EMAIL_TEXT = """\
## Message exclusivement destiné à %(real_life_identity)s (%(real_life_email)s) ##

Bonjour,

Voici votre feuille de personnage complète pour cette soirée mystère, à lire et relire sans modération !

Certains d'entre vous ont des documents spécifiques en pièce jointe, avec des informations juridiques, scientifiques, épistolaires... en fonction de ce qui est mentionné dans leur fiche de personnage. 

Le document de l'Univers du Jeu et des Règles est aussi inclus !

IMPORTANT - Merci de bien vouloir :
- acquitter bonne réception de cet email
- signaler toute incohérence ou lacune que vous verriez dans ces documents par la suite
- IMPRIMER les documents spécifiques, pour les avoir avec vous le jour J

Bonne lecture !

bien amicalement,
Les Organisateurs
"""


def page_breaker(jinja_context):
    return textwrap.dedent(
        """
        
        .. raw:: pdf
        
           PageBreak   
           
        """)


def spacer(jinja_context):
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


def _send_email_to_recipients(sender, recipients, text, subject, attachements=None, dry_run=True, gmail_password=None):

    SMTP_HOST = "smtp.gmail.com:587"

    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    import smtplib

    assert len(recipients) <= 2, recipients  # safety

    recipients = recipients
    emaillist = [elem.strip() for elem in recipients]

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = msg['Reply-to'] = sender
    msg['To'] = ", ".join(recipients)

    msg.preamble = 'Multipart message.\n'

    part = MIMEText(text, _charset='utf8')
    msg.attach(part)

    for attachement in (attachements or []):
        part = MIMEApplication(open(attachement, "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachement))
        msg.attach(part)

    print("/!\\ %s SENDING EMAIL '%s' TO %s (attachments: %s)" % (
    "FAKE" if dry_run else "REALLY", subject, str(recipients), ", ".join(attachements)))

    if not dry_run:
        server = smtplib.SMTP(SMTP_HOST)
        server.ehlo()
        server.starttls()
        server.login(sender, gmail_password)
        res = server.sendmail(msg['From'], emaillist, msg.as_string())
        time().sleep(20)  # else gmail freaks out...
        return res
    return None


def _send_player_sheets_via_email(all_data, player_names, default_player_attachments, dry_run):

    # send already generated docs to players
    # BEWARE, first CHECK that filenames match file contents on all "clues" attachments!

    specific_recipients = set()
    gmail_password = all_data["gmail_smtp_password"]
    assert gmail_password, gmail_password

    gamemaster_email = all_data["global_parameters"]["master_real_email"]
    assert gamemaster_email, gamemaster_email

    for player in sorted(player_names):
        player_data = all_data["character_properties"][player]
        real_life_identity = player_data["real_life_identity"]
        real_life_email = player_data["real_life_email"]

        if real_life_email in specific_recipients:  # each player must have its own email
            raise ValueError('Duplicated specific recipient %s' % real_life_email)
        specific_recipients.add(real_life_email)

        player_attachments = [filename % dict(player=player) for filename in default_player_attachments]
        player_attachments += player_data["email_attachments"]

        for player_attachment in player_attachments:
            assert player in player_attachment or "common" in player_attachment, player_attachment  # do not mixup specific files
            assert os.path.exists(player_attachment), player_attachment

        text = PLAYER_INITIAL_EMAIL_TEXT % player_data

        _send_email_to_recipients(sender=gamemaster_email,
                                  recipients=[real_life_email],
                                  text=text,
                                  subject='Murder Party Chrysalis - votre fiche personnage pour %s' % player.capitalize(),
                                  attachements=player_attachments,
                                  dry_run=dry_run,
                                  gmail_password=gmail_password)