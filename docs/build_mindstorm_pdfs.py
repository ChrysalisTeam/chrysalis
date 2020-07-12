# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import re
import rpg_sheet_generator as rpg
import sys
import textwrap
import time
from collections import OrderedDict
from pprint import pprint

IS_STANDALONE = True

INITIAL_GAME_DATA_DUMP = os.path.join(os.path.dirname(__file__), "_initial_game_data_dump.yaml")

# for now, only these two types exists
GAME_TYPE = "anteauction.standalone" if IS_STANDALONE else "postauction.custom"

DISABLE_DECORATIONS = False

TEMPLATES_ROOT = os.path.abspath("../script_fixtures/mysteryparty")
ALL_CLUES_DOCUMENT = os.path.join(TEMPLATES_ROOT, "miscellaneous", "ingame_clues.odt")

DOC_DIR = os.path.dirname(os.path.abspath(__file__))
STANDARD_EXTRA_ARGS = "--stylesheets=simple_tight"
DECORATIONS_EXTRA_ARGS = "--stylesheets=simple_large,dark_background_with_cover"

MAIN_OUTPUT_DIR = "output_mindstorm"
DOCUMENTS_OUTPUT_DIR = os.path.join(MAIN_OUTPUT_DIR, "documents")

if not os.path.exists(DOCUMENTS_OUTPUT_DIR):
    os.mkdir(DOCUMENTS_OUTPUT_DIR)

# TODO change this, "common lore introduction" changes are not relevant anymore!
PLAYER_INITIAL_EMAIL_TEXT = """\
## Message exclusivement destiné à %(real_life_identity)s (%(real_life_email)s) ##

Bonjour,

Voici votre feuille de personnage complète, à lire et relire sans modération !

Une fiche synthétique est également fournie, récapitulant les principaux éléments de votre fiche de personnage. 
N'hésitez pas à la compléter avec toute autre information que vous jugeriez bon de garder sur vous durant le jeu.

Certains d'entre vous ont des documents spécifiques en pièce jointe, avec des informations juridiques, scientifiques, épistolaires... en fonction de ce qui est mentionné dans leur fiche de personnage. 

Le document de l'Univers du Jeu et des Règles est aussi inclus, avec quelques évolutions :
- les photos du trombinoscope ont été mises à jour
- l'utilisation du "poing levé" pour signifier "je suis hors-jeu"
- vous n'avez pas tous la possibilité d'embaucher des mercenaires (mais toujours accès aux médiateurs obérons)

IMPORTANT - Merci de bien vouloir :
- acquitter bonne réception de cet email
- signaler toute incohérence ou lacune que vous verriez dans ces documents par la suite
- IMPRIMER la fiche synthétique ("cheat sheet"), ainsi que les documents spécifiques, pour les avoir avec vous le jour J

Bonne lecture !

bien vaporeusement,
Pascal Chambon pour le CLIVRA
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


jinja_env = rpg.load_jinja_environment(TEMPLATES_ROOT, use_macro_tags=True)

EXCLUDED_CHARACTERS = []  # mystery-party has no sheet for these characters, for now

_asset_path = lambda x: os.path.join(DOCUMENTS_OUTPUT_DIR, x)

CHARACTER_OVERRIDES = dict(  # ALL must have an "email_attachments" here
    amethyst=dict(email_attachments=[_asset_path("berserk_elixir_advanced_ingredients_for_amethyst.pdf"),
                                     _asset_path("lordanian_report_on_midolian_armies_balance_for_amethyst.pdf")]),
    garnet=dict(email_attachments=[]),

    malachite=dict(email_attachments=[]),
    spinel=dict(email_attachments=[]),

    peridot=dict(email_attachments=[_asset_path("origins_of_precious_stones_for_peridot.pdf")]),
    topaz=dict(email_attachments=[]),

    opal=dict(email_attachments=[_asset_path("deadliest_poisons_memo_for_opal.pdf"),
                                 _asset_path("secret_codes_standard_sheet_cheat_for_opal.pdf")]),
    lydia=dict(email_attachments=[]),

    waden=dict(email_attachments=[_asset_path("omrh_university_request_for_waden.pdf"),
                                  _asset_path("radioactive_samples_analysis_report_part_1_for_waden.pdf")]),
    cynthia=dict(email_attachments=[]),

    obsidian=dict(email_attachments=[_asset_path("sabarith_law_summary_for_obsidian.pdf")]),
)


def _ensure_intial_game_data_dump_is_present():
    if not os.path.exists(INITIAL_GAME_DATA_DUMP):
        # WORKAROUND FOR DEV ENV SETUP
        os.environ["DJANGO_SETTINGS_MODULE"] = settings_module = \
            "pychronia_game.tests.persistent_mode_settings"  # with DB not in temp dir

        from pychronia_game.scripts import dump_initial_game_yaml;
        dump_initial_game_yaml.execute(INITIAL_GAME_DATA_DUMP)


def _extract_ingame_clues_text_from_docx(clues_file):
    """
    UNUSED
    """
    import docx2txt

    docx_file = os.path.join(TEMPLATES_ROOT, clues_file)

    # we may also use "img_dir" parameter to write images in /tmp/img_dir
    text = docx2txt.process(docx_file)
    return text


def _extract_ingame_clues_text_from_odt(clues_file):
    """
    Extract texts and comments from LibreOffice file.
    """
    import odt2txt
    odt_file = os.path.join(TEMPLATES_ROOT, clues_file)
    odt = odt2txt.OpenDocumentTextFile(odt_file)
    text = odt.toString()
    return text


def _send_email_to_recipients(sender, recipients, text, subject, attachements=None, dry_run=True, gmail_password=None):
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
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(sender, gmail_password)
        res = server.sendmail(msg['From'], emaillist, msg.as_string())
        time.sleep(20)  # else gmail freaks out...
        return res
    return None


GAMEMASTER_MANUAL_PARTS = [
    "gamemaster_manual_mindstorm.rst",
    ## OBSOLETE "gamemaster_checklist_mindstorm.rst",
    # FIXME  add manor surveillance report ?????
]
PLAYER_MANUAL_PARTS = [
    "players/%(player_name)s.GAME_TYPE.rst".replace("GAME_TYPE", GAME_TYPE),
    "players/%(player_name)s_previous_days.rst",
    "players/%(player_name)s_misc_instructions.rst",
    "players/%(player_name)s_missions.rst",
    "players/%(player_name)s_specific_abilities.rst",
    "common_anthropia_account_summary_displayer.rst",  # nested in the same "specific abilities" chapter
    "miscellaneous/players_generic_abilities.rst",  # TODO move to common lore doc?
]

# Maps required permissions to ability descriptions
AVAILABLE_ANTHROPIA_ABILITIES = OrderedDict([
    ("access_mercenaries_hiring", "Embauche de mercenaires dans une grande ville de la planète"),
    ###("access_wiretapping", "Mise sur écoute d'un autre compte Anthropia (et protection contre les écoutes adverses)"),
    ("access_runic_translation", "Traduction de runes akarites à partir de leur transcription"),
    ("access_matter_analysis", "Analyse biophysique d'un objet"),
    ("access_world_scan", "Recherche par scanner mondial des clones d'un objet"),
    ("access_house_reports", "Rapports de vidéosurveillance du manoir de Loyd Georges"),
    ("access_geoip_location", "Géolocalisation de l'émetteur d'un message email"),
    ###(xxx, "Tiers de confiance numérique (à mettre en copie des messages contractuels)"),
])

COMMON_LORE_DOCS = [
    "context_intro.GAME_TYPE.rst".replace("GAME_TYPE", GAME_TYPE),
    "context_details.GAME_TYPE.rst".replace("GAME_TYPE", GAME_TYPE),

    "common_guests_gallery.rst",

    "common_auction_program.rst",

    "miscellaneous/sabarith_triumvirate.rst",
    "miscellaneous/judicial_penalties_overview.rst",
    "miscellaneous/duel_of_honor_rules.rst",
    "miscellaneous/oberons_introduction.rst",
    "miscellaneous/all_specific_abilities_overview.rst",
    "miscellaneous/anthropia_portal.rst",

    "game_rules.rst",
]

# BEWARE, be careful when regenerating PDF clues, that their titles and content match well!

INGAME_CLUES_PARTS = [  # content of ingame clues ODT document, as (filename, number_of_mages)
    ("nazur_mummy_analysis_results", 1),
    ("secret_codes_standard_sheet_cheat_for_opal", 1),
    ("sabarith_law_summary_for_obsidian", 1),
    ("radioactive_samples_analysis_report_part_1_for_waden", 1),
    ("radioactive_samples_analysis_report_part_2_for_waden", 1),
    ("panorbium_fortuna_letter_from_pr_loakim", 1),
    ("military_bag_request_from_pr_eusebon", 1),
    ("origins_of_precious_stones_for_peridot", 1),
    ("bibine_express_flyer_and_akarith_slang_lexicon", 1),
    ("recipe_cod_gratin", 1),
    ("judicator_praeves_instructions_for_murderer", 1),
    ("oleander_plant_info", 2),
    ("deadliest_poisons_memo_for_opal", 2),
    ("robb_barrow_instructions_memo", 1),
    ("digoxin_pharmacology_info", 2),
    ("loyd_georges_health_reports", 2),
    ("recipe_veal_stew", 1),
    ("acknowledgement_of_loyd_georges_complaint_about_shark", 1),
    ("miscellaneous_obscure_runes", 2),
    ("hydroland_sale_poster", 1),
    ("snitch_proposal_letter_for_loyd_georges", 1),
    ("lie_detector_written_interview_cards", 1),
    ("alphonse_debt_reminder_letter_and_mac_jolt_purchase_proposal", 1),
    ("waden_letter_about_orb_and_and_blispin_letter_for_rydji", 1),
    ("panorbium_fortuna_prophecy", 1),
    ("lordanian_report_on_midolian_armies_balance_for_amethyst", 1),
    ("heliossar_spy_reports_on_akaris_armament", 2),
    ("unused_view_of_city", 1),
    ("cynthia_wetfeet_building_picture", 1),
    ("misc_logos_for_game_environment", 2),
    ("enigmas_for_secret_code_and_lg_treasure", 1),
    ("massage_gift_voucher", 1),
    ("ultimate_bank_spider_kits", 1),
    ("coded_enigmas_for_panorbium_fortuna_and_lg_treasure", 1),
    ("coded_enigmas_for_akarith_sect_in_sabarim", 1),
    ("letter_from_rodok_forwarded_to_opal", 1),
    ("berserk_elixir_advanced_ingredients_for_amethyst", 1),
    ("loyd_georges_last_wills", 1),
    ("letters_intercepted_by_sect_about_retired_person", 3),
    ("omrh_university_request_for_waden", 2),
    ("special_missions_for_akarith_ambassador_assassination", 2),
    ("letters_revealing_electoral_fraud_of_lydia_and_crimes_of_opal", 1),
    ("alphonse_poem_for_loyd_georges", 1),
    ("secret_codes_of_modern_akarith_sects_for_cynthia", 1),
    ("telegrams_for_misc_characters_during_evening", 1),
    ("alliance_proposal_for_lordania_and_sabarim", 1),
    ("manor_letter_from_emilos_loakim_stolen_by_amethyst", 1),
    ("mining_lease_negotiation_contrat_for_akarith_ambassador", 1),
    ("letter_about_akarith_purifiers_counter_manipulation_for_cynthia", 1),
    ("loyd_markis_biography_extract", 1),
    ("highly_confidential_letter_for_loyd_georges_about_secret_villa", 1),
]


def _generate_clues_pdfs_from_main_odt_document():
    current_page = 1
    for idx, (basename, pages_count) in enumerate(INGAME_CLUES_PARTS):
        prefix = ""  # or ("%02d_" % idx) if debugging needed
        output_pdf = os.path.join(DOCUMENTS_OUTPUT_DIR, prefix + basename + ".pdf")
        variables = dict(input=ALL_CLUES_DOCUMENT,
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


def _expose_real_identities_in_rst_template(rst):
    # hacks to expose real identities of characters, when the doc is for the gamemaster
    rst = rst.replace(".official_name", ".spoiling_official_name")
    return rst


def _generate_spoiler_manor_surveillance_reports(jinja_context):
    """
    Beware, hackish stuff here: surveillance reports are themselves jinja templates,
    so we prerender them in a loop and then give them to the rest of the RST rendering.
    """
    template_file = os.path.join(TEMPLATES_ROOT, "gamemaster_manor_surveillance_reports_meta.rst")
    template_string = rpg.load_rst_file(template_file)
    rst = rpg.render_with_jinja_and_fact_tags(template_string, jinja_env=jinja_env, jinja_context=jinja_context)

    rst = _expose_real_identities_in_rst_template(rst)

    return rst  # this RST string will be evaluated with jinja once more!


# documents without decorations, typically ; one can provide a LIST of RST files
ISOLATED_DOCS = {
    "gamemaster_manor_surveillance_reports": _generate_spoiler_manor_surveillance_reports,
    "gamemaster_planning_details": "gamemaster_planning_details.rst",
    ##"gamemaster_players_actions_summary": "players/all_players_actions_summary.rst",  # for GAMEMASTER?
    "gamemaster_assets_checklist": "gamemaster_assets_checklist.rst",

    "common_guests_gallery": "common_guests_gallery.rst",  # cant be moved due to images...

    "documents/alphonse_special_sales": "miscellaneous/alphonse_special_sales.rst",

    "documents/players_last_minute_context": "miscellaneous/players_last_minute_context.rst",  # for SOME players

    "documents/players_negotiating_mandates": "missions/mining_lease_negotiation/negotiating_mandates.rst",
    # for SOME players

    ##"all_players_misc_instructions": "all_players_misc_instructions.rst", # useless now

    "documents/audio_recordings": "miscellaneous/audio_recordings.rst",

    "npc_alphonse_sheet": "npcs/alphonse_sheet.rst",
    "npc_rydji_sheet": "npcs/rydji_sheet.rst",
    "npc_robb_barrow_sheet": "npcs/robb_barrow_sheet.rst",
    "npc_notary_sheet": "npcs/notary_sheet.rst",
    "npc_akarith_ambassador_sheet": "npcs/akarith_ambassador_sheet.rst",
    "npc_oberon_agent_sheet": "npcs/oberon_agent_sheet.rst",
    "npc_neighbour_sheet": "npcs/old_neighbour_sheet.rst",
    "npc_salima_massagist_sheet": "npcs/salima_massagist_sheet.rst",

    "all_phone_appointments": ["appointments/mentor_briefings_all_factions.rst", spacer,
                               "appointments/yodic_council_interviews.rst", spacer,
                               "appointments/dorian_duke_blasphemy_proof_destruction_mission.rst", spacer,
                               "appointments/captain_rodimir_negotiation.rst"],
}


def generate_mindstorm_rst_from_parts(parts, title, add_page_breaks, with_decorations, toc_depth=1, jinja_context=None):
    """
    Parts can be basenames for RST templates, or callables taking jinja context
    as parameter and returning RST strings.
    """

    # define here specific RST structures, like custom roles
    full_data = textwrap.dedent("""
    
    .. CUSTOM ROLES HERE
    
    """)

    if title:
        full_data += textwrap.dedent("""
    #######################################################################################
    MINDSTORM
    #######################################################################################

    %s
    ################################################################ 


       
    .. raw:: pdf
    
       Spacer 0 80
   
       PageBreak standardPage
       
    .. contents:: Table of Contents
       :depth: %s
       
    """) % (title, toc_depth)

    for part in parts:
        if callable(part):
            new_data = part(jinja_context=jinja_context)  # builder function
        else:
            rst_filepath = os.path.join(TEMPLATES_ROOT, part)
            new_data = rpg.load_rst_file(rst_filepath)
        full_data += new_data
        if add_page_breaks:
            full_data += "\n\n.. raw:: pdf\n\n    PageBreak\n\n"
        full_data += "\n\n"

    if with_decorations:
        full_data += textwrap.dedent("""
            .. raw:: pdf
            
               PageBreak
               
               Spacer 0 80
               
            .. image:: ../assets/inpector_shark_menacing_small.png
                :align: center
                :width: 80%
        """)

    return full_data


def build_mindstorm_pdf(parts, filename_base,
                        title, with_decorations=True,
                        add_page_breaks=False,
                        jinja_context=None,
                        skip_pdf_output=False,
                        toc_depth=1):
    if filename_base:
        print("Generating", filename_base)
    assert filename_base or skip_pdf_output

    with_decorations = with_decorations and not DISABLE_DECORATIONS

    rst_content = generate_mindstorm_rst_from_parts(
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

    extra_args = DECORATIONS_EXTRA_ARGS if with_decorations else STANDARD_EXTRA_ARGS

    if not skip_pdf_output:
        filepath_base = os.path.join(MAIN_OUTPUT_DIR, filename_base)
        rpg.convert_rst_content_to_pdf(filepath_base=filepath_base,
                                       rst_content=rst_content,
                                       conf_file="rst2pdf.conf",
                                       extra_args=extra_args)

    return rst_content


def generate_mindstorm_sheets():
    _ensure_intial_game_data_dump_is_present()  # IMPORTANT

    has_coherence_errors = False

    all_data = dict(standalone=IS_STANDALONE,
                    use_player_photos=True,
                    gamemaster=False)  # TODO change me

    data = rpg.load_yaml_file(INITIAL_GAME_DATA_DUMP)
    all_data.update(data)  # TODO - replace that dump by source data, eventually

    all_data["available_anthropia_abilities"] = AVAILABLE_ANTHROPIA_ABILITIES

    murder_party_items = rpg.load_yaml_file("../script_fixtures/mysteryparty/gamemaster_assets_checklist.yaml")
    all_data["murder_party_items"] = murder_party_items

    # BEWARE - sensitive data specific to a murder party game
    data = rpg.load_yaml_file("../script_fixtures/local.yaml")  # must exist, see local.yaml.example
    all_data.update(data)

    players_names = sorted([k for (k, v) in all_data["character_properties"].items()
                            if not v["is_npc"] and k not in EXCLUDED_CHARACTERS])
    players_names_set_no_shark = set(players_names)
    assert "shark" not in players_names_set_no_shark
    players_names += ["shark"]  # special player
    all_data["players_names"] = players_names
    #print("-------->", players_names)

    master_login = all_data["global_parameters"]["master_login"]

    for k, v in CHARACTER_OVERRIDES.items():
        all_data["character_properties"][k].update(v)  # we override official names mainly

    for k, v in all_data["character_properties"].items():
        #print("HANDLING CHARACTER", k)

        # additional variables to DRY display
        official_name = all_data["character_properties"][k]["official_name"]
        full_official_title = "%s, %s" % (official_name,
                                          all_data["character_properties"][k]["official_role"])
        all_data["character_properties"][k]["full_official_title"] = full_official_title
        all_data["character_properties"][k]["spoiling_official_name"] = "%s (%s)" % (official_name, k.capitalize())

    # for standalone docs
    isolated_data = all_data.copy()
    isolated_data["current_player_id"] = None

    # -------------

    if False:
        # export clues into a myriad of small PDFs
        _generate_clues_pdfs_from_main_odt_document()

    # -------------

    if False:  # BEWARE DANGEROUS
        def _send_player_sheets_via_email(dry_run):

            # send already generated docs to players
            # BEWARE, first CHECK that filenames match file contents on all "clues" attachments!

            specific_recipients = set()
            gmail_password = all_data["gmail_smtp_password"]
            assert gmail_password, gmail_password

            gamemaster_email = all_data["global_parameters"]["master_real_email"]
            assert gamemaster_email, gamemaster_email

            for player in sorted(players_names_set_no_shark):
                player_data = all_data["character_properties"][player]
                real_life_identity = player_data["real_life_identity"]
                real_life_email = player_data["real_life_email"]

                if real_life_email in specific_recipients:  # each player must have its own email
                    raise ValueError('Duplicated specific recipient %s' % real_life_email)
                specific_recipients.add(real_life_email)

                player_attachments = [
                                         os.path.join(MAIN_OUTPUT_DIR, "common_lore_introduction.pdf"),
                                         os.path.join(MAIN_OUTPUT_DIR, "player_%s_cheat_sheet.pdf" % player),
                                         os.path.join(MAIN_OUTPUT_DIR, "player_%s_sheet_full.pdf" % player),
                                     ] + player_data["email_attachments"]

                for player_attachment in player_attachments:
                    assert player in player_attachment or "common" in player_attachment, \
                        player_attachment  # do not mixup specific files
                    assert os.path.exists(player_attachment), player_attachment

                text = PLAYER_INITIAL_EMAIL_TEXT % player_data

                _send_email_to_recipients(sender=gamemaster_email,
                                          recipients=[real_life_email],
                                          text=text,
                                          subject='Murder Party Chrysalis - votre fiche personnage pour %s' % player.capitalize(),
                                          attachements=player_attachments,
                                          dry_run=dry_run,
                                          gmail_password=gmail_password)

        print("----------FAKE--------------")
        _send_player_sheets_via_email(dry_run=True)  # ensure everything seems in place
        if False:
            print("----------REAL--------------")
            _send_player_sheets_via_email(dry_run=False)  # REALLY send stuffs
        STOP  # only do that

    # -------------

    # first the gamemaster manual
    if True:
        gm_data = all_data.copy()
        gm_data["gamemaster"] = True
        gm_data["current_player_id"] = master_login  # silent
        gm_data["current_player_password"] = gm_data["global_parameters"]["master_password"]
        build_mindstorm_pdf(GAMEMASTER_MANUAL_PARTS,
                            filename_base="chrysalis_mindstorm_gamemaster_manual", title="Maître de Jeu",
                            add_page_breaks=True, jinja_context=gm_data, toc_depth=2)

    # -------------

    # then the common LORE doc
    if True:
        build_mindstorm_pdf(COMMON_LORE_DOCS,
                            filename_base="common_lore_introduction", title="Univers du Jeu",
                            add_page_breaks=True, jinja_context=isolated_data)

    # -------------

    # then miscellaneous docs, eg. last-minute context, checklists (which might be included by other sheets)...
    if True:
        for filename_base, doc in sorted(ISOLATED_DOCS.items()):
            build_mindstorm_pdf([doc] if not isinstance(doc, (list, tuple)) else doc,
                                filename_base=filename_base,
                                title=None,
                                with_decorations=False,
                                jinja_context=isolated_data)

    # -------------

    def _get_player_context(_player_name):
        player_data = all_data.copy()
        player_data["current_player_id"] = _player_name
        _character_properties = all_data["character_properties"][_player_name]
        player_data["current_player_password"] = _character_properties["password"]
        player_data["current_player_account"] = _character_properties["account"]
        player_data["current_player_extra_goods"] = _character_properties["extra_goods"]
        player_data["permissions"] = _character_properties["permissions"]
        player_data["hide_anthropia_credentials"] = False  # by default
        return player_data

    # then character full sheets
    if True:
        for player in players_names:
            parts = [(part % dict(player_name=player) if not callable(part) else part)
                     for part in PLAYER_MANUAL_PARTS]
            #print("COMPILING", player, parts)
            character_displayed_name = (all_data["character_properties"][player]["official_name"]
                                        if player in all_data["character_properties"]
                                        else player)
            player_data = _get_player_context(player)
            build_mindstorm_pdf(parts, filename_base="player_%s_sheet_full" % player,
                                title="%s" % character_displayed_name, jinja_context=player_data)

    # then character cheat sheets
    if True:
        full_extracts_rst = ""
        for player in sorted(players_names_set_no_shark):
            parts = ["players/%(player_name)s_cheat_sheet.rst" % dict(player_name=player),
                     "players/%(player_name)s_specific_abilities.rst" % dict(player_name=player),
                     "common_anthropia_account_summary_displayer.rst",
                     # nested in the same "specific abilities" chapter
                     "common_cheat_sheet_footer.rst"]
            player_data = _get_player_context(player)
            player_data["is_cheat_sheet"] = True
            build_mindstorm_pdf(parts,
                                filename_base="player_%s_cheat_sheet" % player,
                                title=None,
                                with_decorations=False,
                                jinja_context=player_data)

    # -------------

    # then character sheet extracts for the gamemaster
    if True:
        full_extracts_rst = ""
        for player in players_names:
            if full_extracts_rst:
                full_extracts_rst += "\n----------\n\n"  # add separator
            player_data = _get_player_context(player)
            player_data["hide_anthropia_credentials"] = True  # else too verbose and sensitive
            parts = [
                "players/%(player_name)s_specific_abilities.rst" % dict(player_name=player),
                "common_anthropia_account_summary_displayer.rst",  # nested in the same "specific abilities" chapter
                #"players/%(player_name)s_misc_instructions.rst" % dict(player_name=player)
            ]
            player_rst = build_mindstorm_pdf(parts, filename_base=None,
                                             title=None, add_page_breaks=False, with_decorations=False,
                                             jinja_context=player_data, skip_pdf_output=True)
            full_extracts_rst += "\n\n\n%s\n#######################\n\n" % player.capitalize() + player_rst
        filepath_base = os.path.join(MAIN_OUTPUT_DIR, "gamemaster_players_extracts")
        rpg.convert_rst_content_to_pdf(filepath_base=filepath_base,
                                       rst_content=full_extracts_rst,
                                       conf_file="rst2pdf.conf",
                                       extra_args=STANDARD_EXTRA_ARGS)

    # -------------

    # then resolve fact/hint tags from the ODT clues file
    if True:
        print("Extracting ingame clues text from ODT file")
        content = _extract_ingame_clues_text_from_odt(ALL_CLUES_DOCUMENT)
        ##print(content[:1000].encode('ascii', 'ignore'))
        assert "Inutilisé" in content  # comments are well included

        # no need for variables nor rendered output
        rpg.render_with_jinja_and_fact_tags(
            content=content,
            jinja_env=jinja_env,
            jinja_context={})

    # -------------

    print("\nInline hints of scenario:")
    pprint(jinja_env.hints_registry)
    hints_registry_good_value = set(['needed', 'provided'])
    for k, v in jinja_env.hints_registry.items():
        assert v <= hints_registry_good_value, (k, v)  # no weird values
        if 'needed' in v and 'provided' not in v:
            print("!!!!! ERROR IN hints registry for key", k, ':', v, 'requires a provided hint')
            has_coherence_errors = True

    # -------------

    print("\nInline symbols of scenario:")
    pprint(jinja_env.symbols_registry)
    for k, v in jinja_env.symbols_registry.items():
        unique_values = set(x.strip().lower() for x in v)
        if len(unique_values) != 1:
            print("!!!!! ERROR IN symbols registry for key", k, ':', v)
            has_coherence_errors = True

    # -------------

    print("\nInline facts of scenario:")

    pprint(jinja_env.facts_registry)

    def _replace_all_players_set(names):
        """When all real players know a fact, replace their names by a symbol"""
        names_set = set(names)
        if players_names_set_no_shark <= names_set:
            new_set = (names_set - players_names_set_no_shark) | {"ALL-PLAYERS"}
        else:
            new_set = names_set
        return new_set

    def _check_fact_leaf(fact_name, player_id, fact_node):
        """Ensure that the knowledge of a single player over a single fact is coherent"""
        assert fact_node["in_normal_sheet"] or fact_node["in_cheat_sheet"], data
        if fact_node["in_cheat_sheet"]:
            if not fact_node["in_normal_sheet"]:  # all facts must be explained in normal sheets
                print("!!!!! ERROR IN fact leaf for key", fact_name, ':', player_id, fact_node)
                raise RuntimeError('See error above in logs')

    facts_items = sorted(jinja_env.facts_registry.items())

    for (fact_name, fact_data) in facts_items:
        for player_id, fact_node in fact_data.items():
            _check_fact_leaf(fact_name, player_id=player_id, fact_node=fact_node)

    facts_summary = [(fact_name,  #.replace("_", " "),
                      sorted((x, y) for (x, y) in fact_data.items()
                             if y["is_author"] and x != master_login),
                      sorted((x, y) for (x, y) in fact_data.items()
                             if not y["is_author"] and x != master_login))
                     for (fact_name, fact_data) in facts_items]

    if facts_summary:
        build_mindstorm_pdf(["gamemaster_facts_summary.rst"],
                            filename_base="gamemaster_facts_summary",
                            title=None,
                            with_decorations=False,
                            jinja_context=dict(facts_summary=facts_summary))
    else:
        print("!!! Aborting generation of gamemaster_facts_summary, since NO FACTS have been detected")

    if has_coherence_errors:
        print(">>>>>>>>>> PROBLEMS WITH SCRIPT COHERENCE, SEE OUTPUTS <<<<<<<<<<")
        sys.exit(1)
    else:
        print("Script Over")


def test_generation():
    # to use pytest with this builder, and get nifty stack traces
    generate_mindstorm_sheets()


if __name__ == "__main__":
    generate_mindstorm_sheets()
