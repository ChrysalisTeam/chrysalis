# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import re
import rpg_sheet_generator as rpg
import sys
import textwrap
from collections import OrderedDict

from mysteryparty_common_utils import build_mysteryparty_pdf, _ensure_intial_game_data_dump_is_present, \
    _extract_ingame_clues_text_from_odt, _generate_clues_pdfs_from_main_odt_document, _send_character_sheets_via_email
from rpg_sheet_generator import display_and_check_story_tags

IS_STANDALONE = True

INITIAL_GAME_DATA_DUMP = os.path.join(os.path.dirname(__file__), "_initial_game_data_dump.yaml")

DISABLE_DECORATIONS = False

TEMPLATES_ROOT = os.path.abspath("../script_fixtures/mysteryparty_archives")
TEMPLATES_COMMON = os.path.abspath("../script_fixtures/mysteryparty_common")
ALL_CLUES_DOCUMENT = os.path.join(TEMPLATES_ROOT, "miscellaneous", "ingame_clues_archives.odt")

DOC_DIR = os.path.dirname(os.path.abspath(__file__))
STANDARD_EXTRA_ARGS = "--stylesheets=simple_tight"
DECORATIONS_EXTRA_ARGS = "--stylesheets=simple_large,dark_background_with_frame"  # Use --show-frame-boundary (if necessary to debug)
BIG_FONT_EXTRA_PARAMS = "--stylesheets=big_font"

MAIN_OUTPUT_DIR = "output_archives"
DOCUMENTS_OUTPUT_DIR = os.path.join(MAIN_OUTPUT_DIR, "documents")

if not os.path.exists(DOCUMENTS_OUTPUT_DIR):
    os.mkdir(DOCUMENTS_OUTPUT_DIR)



jinja_env = rpg.load_jinja_environment([TEMPLATES_ROOT, TEMPLATES_COMMON], use_macro_tags=True)

EXCLUDED_CHARACTERS = []  # mystery-party has no sheet for these characters, for now

_asset_path = lambda x: os.path.join(DOCUMENTS_OUTPUT_DIR, x)


CHARACTER_OVERRIDES = dict(  # ALL must have an "email_attachments" here
    diakon_dispeller=dict(official_name="Le désenvouteur", email_attachments=[]),
    diakon_exorcist=dict(official_name="L'exorciste", email_attachments=[]),
    diakon_invoker=dict(official_name="L'invocateur", email_attachments=[]),

    explorer_unveiler=dict(official_name="Le dévoileur", email_attachments=[]),
    explorer_anthropologist=dict(official_name="L'anthropologue", email_attachments=[]),
    explorer_runologist=dict(official_name="Le runologue", email_attachments=[]),

    parcival_alchemist=dict(official_name="L'alchimiste", email_attachments=[]),
    parcival_woodsman=dict(official_name="Le gardien des bois", email_attachments=[]),
    parcival_oracle=dict(official_name="L'oracle", email_attachments=[]),

    spy_lockpicker=dict(official_name="Le crocheteur", email_attachments=[]),
    spy_minesweeper=dict(official_name="Le démineur", email_attachments=[]),
    spy_sounder=dict(official_name="Le sondeur", email_attachments=[]),
)

NPC_OVERRIDES = dict(
    avatar_druid=dict(official_name="Le druide", email_attachments=[]),
    avatar_duchess=dict(official_name="La duchesse", email_attachments=[]),
    avatar_inventor=dict(official_name="L'inventeur", email_attachments=[]),

    phantom_archivist=dict(official_name="L'archiviste", email_attachments=[]),
    phantom_arkon=dict(official_name="L'arkonte", email_attachments=[]),
    phantom_octave=dict(official_name="Octave", email_attachments=[]),
    #phantom_magus=dict(official_name="Défunt Mage Mos Peratys", email_attachments=[]),
    #phantom_beast=dict(official_name="La Bête", email_attachments=[]),
    #phantom_thief=dict(official_name="Le voleur", email_attachments=[]),

    #god_ankou=dict(official_name="L'Ankou", email_attachments=[]),
)

# FIXME rename to "character"
PLAYER_INITIAL_EMAIl_TEMPLATE = """\
## Message exclusivement destiné à %(real_life_identity)s (%(real_life_email)s) ##

Bonjour,

Voici votre feuille de personnage pour la soirée mystère "Les archives secrètes des Maupertuis".

Un document à lire et relire sans modération !

Des informations sur l'univers du jeu et les règles, cruciales, sont aussi incluses !

IMPORTANT - Nous vous remercions de bien vouloir :
- acquitter bonne réception de cet email
- signaler toute incohérence ou lacune que vous verriez dans ces documents

Bonne lecture !

Amicalement,
Les Organisateurs
"""


AUTOMATA_INITIAL_EMAIl_TEMPLATE = """
Bonjour,

Voici des informations sur l'univers du jeu et les règles, pour la soirée mystère "Les archives secrètes des Maupertuis"

En tant que figurants automates, vous n'avez pas de fiche de personnage avec un rôle spécifique, mais vous pourrez suivre les joueurs dans leurs aventures.

Seule la section "Fonctionnement des différents mondes" du "Compléments des Figurants" est importante pour vous, le reste est uniquement là à titre informatif.

IMPORTANT - Nous vous remercions de bien vouloir :
- acquitter bonne réception de cet email
- signaler toute incohérence ou lacune que vous verriez dans ces documents

Bonne lecture !

Amicalement,
Les Organisateurs
"""


player_names = set(CHARACTER_OVERRIDES.keys())
npc_names = set(NPC_OVERRIDES.keys())

GAMEMASTER_MANUAL_PARTS = [
    "gamemaster_manual_archives.rst",
]

PLAYER_MANUAL_PARTS = [
    "players/%(player_name)s_role.rst",
]

COMMON_NPC_DOCS = [
    "common_npc_sheet.rst",
]

COMMON_LORE_AND_RULES = [
    "common_lore_sheet.rst",
    "game_rules.rst",
]

# BEWARE, be careful when regenerating PDF clues, that their titles and content match well!

INGAME_CLUES_PARTS = [  # content of ingame clues ODT document, as (filename, number_of_mages)
    ("recipe_flex_elixir_and_clarity_lotion", 1),
    ("recipe_pyrolitis_tincture", 1),
    ("recipe_rejuvenation_cocktail", 1),
    ("thanatologue_extract", 3),
    ("meredice_diary_extract", 1),
    ("parcival_oracle_vision_about_water_mill", 1),
    ("parcival_oracle_vision_about_necromancers_and_ring_amplificans", 1),
    ("parcival_oracle_vision_about_maupertuis_father_twin_books", 1),
    ("parcival_oracle_shared_vision_about_world_threat", 3),
    ("parcival_oracle_vision_chaos_novel_tome_3", 1),
    ("secret_codes_converters", 1),
    ("unreadable_runes", 2),
    ("antic_akarith_runes", 1),
    ("maupertuis_father_chest_code_anamorphosis_enigma", 1),
    ("maupertuis_whispering_box_enigma", 1),
    ("octave_diary_on_his_tomb", 1),
    ("avatar_novel_summaries", 2),
    ("conspiracy_anti_arkoon_letter_with_coast_of_arms", 1),
    ("book_shelf_labels_for_library", 2),
    ("maupertuis_caduceus_symbol", 1),
    ("coffee_mill_stereogram", 1),
    ("miscellaneous_secret_messages", 1),
    ("trap_and_property_markers", 2),
]

# documents without decorations, typically ; one can provide a LIST of RST files as value
ISOLATED_DOCS = {
    # GAMEMASTER DOCS
    "gamemaster_assets_checklist": ("gamemaster_assets_checklist.rst", "gamemaster"),
    "gamemaster_crates_listing_big": ("gamemaster_crates_listing.rst", "gamemaster"),

    # NPCs
    "npc_avatar_druid_sheet": ("npcs/avatar_druid_sheet.rst", "avatar_druid"),
    "npc_avatar_inventor_sheet": ("npcs/avatar_inventor_sheet.rst", "avatar_inventor"),
    "npc_avatar_duchess_sheet": ("npcs/avatar_duchess_sheet.rst", "avatar_duchess"),

    "npc_god_ankou_sheet": ("npcs/god_ankou_sheet.rst", "god_ankou"),

    "npc_phantom_archivist_sheet": ("npcs/phantom_archivist_sheet.rst", "phantom_archivist"),
    "npc_phantom_arkon_sheet": ("npcs/phantom_arkon_sheet.rst", "phantom_arkon"),
    "npc_phantom_octave_sheet": ("npcs/phantom_octave_sheet.rst", "phantom_octave"),
    "npc_phantom_thief_sheet": ("npcs/phantom_thief_sheet.rst", "phantom_thief"),
    "npc_phantom_beast_sheet": ("npcs/phantom_beast_sheet.rst", "phantom_beast"),
    "npc_phantom_magus_sheet": ("npcs/phantom_magus_sheet.rst", "phantom_magus"),

    # SPECIFIC PLANNINGS
    "planning_of_prophecies": ("miscellaneous/planning_of_prophecies.rst", "anyone"),
}


def generate_archives_rst_from_parts(parts, title, add_page_breaks, with_decorations, toc_depth=1, jinja_context=None):
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
    Les archives secrètes des Maupertuis
    #######################################################################################

    %s
    ################################################################ 


    .. raw:: pdf
   
       PageBreak standardPage
       
    .. XXX contents:: Table des Matières
    ..    :depth: %s
       
    """) % (title, toc_depth)

    for part in parts:
        if callable(part):
            new_data = part(jinja_context=jinja_context)  # builder function
        else:
            rst_filepath1 = os.path.join(TEMPLATES_ROOT, part)
            rst_filepath2 = os.path.join(TEMPLATES_COMMON, part)
            rst_filepath = rst_filepath1 if os.path.exists(rst_filepath1) else rst_filepath2
            assert os.path.exists(rst_filepath), rst_filepath
            new_data = rpg.load_rst_file(rst_filepath)
        full_data += new_data
        if add_page_breaks:
            full_data += "\n\n.. raw:: pdf\n\n    PageBreak\n\n"
        full_data += "\n\n"

    '''
    if with_decorations:
        full_data += textwrap.dedent("""
            .. raw:: pdf
            
               PageBreak
               
               Spacer 0 80
               
            .. image:: ../assets/some_image.png
                :align: center
                :width: 80%
        """)
    '''

    return full_data


def build_archives_pdf(parts, filename_base, title,
                        with_decorations=True,
                        add_page_breaks=False,
                        jinja_context=None,
                        skip_pdf_output=False,
                        toc_depth=1):

    with_decorations = with_decorations and not DISABLE_DECORATIONS

    big_font = filename_base.endswith("_big")
    if big_font:
        # Ignore with_decoration!
        extra_args = BIG_FONT_EXTRA_PARAMS
    else:
        extra_args = extra_args=DECORATIONS_EXTRA_ARGS if with_decorations else STANDARD_EXTRA_ARGS

    return build_mysteryparty_pdf(
        parts=parts,
        filename_base=filename_base,
        title=title,
        output_dir=MAIN_OUTPUT_DIR,
        generate_rst_from_parts=generate_archives_rst_from_parts,
        jinja_env=jinja_env,
        extra_args=extra_args,
        with_decorations=with_decorations,
        add_page_breaks=add_page_breaks,
        jinja_context=jinja_context,
        skip_pdf_output=skip_pdf_output,
        toc_depth=toc_depth
    )




def generate_archives_sheets():
    _ensure_intial_game_data_dump_is_present(INITIAL_GAME_DATA_DUMP)  # IMPORTANT

    all_data = dict(use_player_photos=True)

    data = rpg.load_yaml_file(INITIAL_GAME_DATA_DUMP)
    all_data.update(data)

    murder_party_items = rpg.load_yaml_file(os.path.join(TEMPLATES_ROOT, "gamemaster_assets_checklist.yaml"))
    all_data["murder_party_items"] = murder_party_items

    # Sort items between crates dependong on @CRATE start markers
    murder_party_items_per_crate = OrderedDict()

    def _extract_crate(_title):
        crate = None
        new_title = _title
        #print(">>>>> SEARCHING CRATE IN TITLE", _title)
        match = re.search(r"^@\S+\s", _title)
        if match:
            crate = match.group(0)
            new_title = new_title.replace(crate, "")
        return crate, new_title

    for (section, item_titles) in murder_party_items:
        crate, section = _extract_crate(section)
        default_create = crate or section
        for item_title in item_titles:
            crate, item_title = _extract_crate(item_title)
            crate = crate or default_create
            assert crate, repr(crate)
            murder_party_items_per_crate.setdefault(crate, [])
            murder_party_items_per_crate[crate].append(item_title)
    all_data["murder_party_items_per_crate"] = murder_party_items_per_crate.items()

    # BEWARE - sensitive data specific to a murder party game
    data = rpg.load_yaml_file("../script_fixtures/local.yaml")  # must exist, see local.yaml.example
    local_character_overrides = data.pop("_CHARACTER_OVERRIDES_")
    local_npc_overrides = data.pop("_NPC_OVERRIDES_")
    all_data.update(data)

    all_data["player_names"] = player_names
    #print("-------->", player_names)

    master_login = all_data["global_parameters"]["master_login"]

    for k, v in CHARACTER_OVERRIDES.items():
        all_data["character_properties"].setdefault(k, {})  # Create (player) character if necessary
        all_data["character_properties"][k].update(v)  # We override official names mainly
        all_data["character_properties"][k].update(local_character_overrides[k])  # Override real names and emails

    for k, v in NPC_OVERRIDES.items():
        all_data["character_properties"].setdefault(k, {})  # Create (NPC) character if necessary
        all_data["character_properties"][k].update(v)  # We override official names mainly
        all_data["character_properties"][k].update(local_npc_overrides[k])  # Override real names and emails


    # for standalone docs
    isolated_data = all_data.copy()
    isolated_data["current_player_id"] = None

    # -------------

    if False:  # BEWARE DANGEROUS

        default_player_attachments = [
                                         os.path.join(MAIN_OUTPUT_DIR, "common_lore_and_game_rules.pdf"),
                                         os.path.join(MAIN_OUTPUT_DIR, "player_%(player)s_sheet_full.pdf"),
                                     ]
        default_npc_attachments = [
                                         os.path.join(MAIN_OUTPUT_DIR, "common_lore_and_game_rules.pdf"),
                                         os.path.join(MAIN_OUTPUT_DIR, "common_npc_information.pdf"),
                                         os.path.join(MAIN_OUTPUT_DIR, "npc_%(player)s_sheet.pdf"),
                                     ]
        def _send_everything(dry_run):
            _send_character_sheets_via_email(all_data=all_data, player_names=player_names,
                                          subject='Soirée Mystère Archives - votre fiche de joueur pour %s',
                                          email_template=PLAYER_INITIAL_EMAIl_TEMPLATE,
                                          default_player_attachments=default_player_attachments, allow_duplicate_emails=True, dry_run=dry_run)  # ensure everything seems in place
            _send_character_sheets_via_email(all_data=all_data, player_names=npc_names,
                                          subject='Soirée Mystère Archives - votre fiche de figurant pour %s',
                                          email_template=PLAYER_INITIAL_EMAIl_TEMPLATE,
                                          default_player_attachments=default_npc_attachments, allow_duplicate_emails=True, dry_run=dry_run)  # ensure everything seems in place

        print("----------FAKE--------------")
        _send_everything(dry_run=True)

        if False:
            print("----------REAL--------------")
            _send_everything(dry_run=False)  # REALLY send stuffs

        STOP  # only do that

    # -------------

    if True:
        # export clues into a myriad of small PDFs
        _generate_clues_pdfs_from_main_odt_document(input_doc=ALL_CLUES_DOCUMENT,
                                                    clues_parts=INGAME_CLUES_PARTS,
                                                    output_dir=DOCUMENTS_OUTPUT_DIR)

    # -------------

    # first the gamemaster manual
    if True:
        gm_data = all_data.copy()
        gm_data["current_player_id"] = master_login  # silent
        build_archives_pdf(GAMEMASTER_MANUAL_PARTS,
                            filename_base="chrysalis_archives_gamemaster_manual", title=None,
                            add_page_breaks=True, jinja_context=gm_data, toc_depth=2, with_decorations=False)

    # -------------

    # then the common DOCS for participants
    if False:

        isolated_data["current_player_id"] = "everyone"
        build_archives_pdf(COMMON_LORE_AND_RULES,
                            filename_base="common_lore_and_game_rules", title="Univers et Règles du Jeu ",
                            add_page_breaks=True, jinja_context=isolated_data)

        isolated_data["current_player_id"] = "npcs"
        build_archives_pdf(COMMON_NPC_DOCS,
                            filename_base="common_npc_information", title="Compléments des Figurants",
                            add_page_breaks=True, jinja_context=isolated_data)

        isolated_data["current_player_id"] = None  # Restore this!

    # -------------

    # then miscellaneous docs, eg. NPC sheets, last-minute context, checklists (which might be included by other sheets)...
    if True:
        for filename_base, docs_and_player_id in sorted(ISOLATED_DOCS.items()):
            doc, player_id = docs_and_player_id
            isolated_data["current_player_id"] = player_id
            build_archives_pdf([doc] if not isinstance(doc, (list, tuple)) else doc,
                                filename_base=filename_base,
                                title=None,
                                with_decorations=False,
                                jinja_context=isolated_data)
            isolated_data["current_player_id"] = None

    ##AAAAAA
    # -------------

    def _get_player_context(_player_name):
        player_data = all_data.copy()
        player_data["current_player_id"] = _player_name
        #_character_properties = all_data["character_properties"][_player_name]
        return player_data

    # then character full sheets
    if True:
        for player in player_names:
            parts = [(part % dict(player_name=player) if not callable(part) else part)
                     for part in PLAYER_MANUAL_PARTS]
            #print("COMPILING", player, parts)
            character_displayed_name = (all_data["character_properties"][player].get("official_name", player)
                                        if player in all_data["character_properties"]
                                        else player)
            player_data = _get_player_context(player)
            build_archives_pdf(parts, filename_base="player_%s_sheet_full" % player,
                                title="%s" % character_displayed_name, jinja_context=player_data)

    # then character cheat sheets - USELESS HERE????
    if False:
        for player in sorted(player_names_set_no_shark):
            parts = ["players/%(player_name)s_cheat_sheet.rst" % dict(player_name=player),
                     "players/%(player_name)s_specific_abilities.rst" % dict(player_name=player),
                     "common_anthropia_account_summary_displayer.rst",
                     # nested in the same "specific abilities" chapter
                     "common_cheat_sheet_footer.rst"]
            player_data = _get_player_context(player)
            player_data["is_cheat_sheet"] = True
            build_archives_pdf(parts,
                                filename_base="player_%s_cheat_sheet" % player,
                                title=None,
                                with_decorations=False,
                                jinja_context=player_data)
    # -------------

    # then resolve fact/hint tags from the ODT clues file
    if True:
        print("Extracting ingame clues text from ODT file")
        content = _extract_ingame_clues_text_from_odt(ALL_CLUES_DOCUMENT)
        #print(content[:10000].encode('ascii', 'ignore'))
        assert "petite sœur des Parcival" in content  # comments are well included

        # no need for variables nor rendered output, we just fill fact-check registries
        rpg.render_with_jinja_and_fact_tags(
            content=content,
            jinja_env=jinja_env,
            jinja_context={})

    # -------------

    # perform full checkup of story checks now that all has been processed
    has_any_coherence_error, facts_summary = display_and_check_story_tags(jinja_env, masked_user_names=[master_login])

    if facts_summary:
        aggregated_facts_summary = [(fact, sorted(authors + viewers)) for (fact, authors, viewers) in facts_summary]
        build_archives_pdf(["gamemaster_facts_summary.rst"],
                            filename_base="gamemaster_facts_summary",
                            title=None,
                            with_decorations=False,
                            jinja_context=dict(aggregated_facts_summary=aggregated_facts_summary))
    else:
        print("!!! Aborting generation of gamemaster_facts_summary, since NO FACTS have been detected")


    if has_any_coherence_error:
        print(">>>>>>>>>> PROBLEMS WITH SCRIPT COHERENCE, SEE OUTPUTS <<<<<<<<<<")
        sys.exit(1)
    else:
        print("Script Over")



def test_generation():
    # to use pytest with this builder, and get nifty stack traces
    generate_archives_sheets()


if __name__ == "__main__":
    generate_archives_sheets()
