# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import re

import rpg_sheet_generator as rpg
import sys
import textwrap
from collections import OrderedDict

from mysteryparty_common_utils import build_mysteryparty_pdf, _ensure_intial_game_data_dump_is_present, \
    _register_story_tags_from_clues_document, export_ingame_clues_pdfs, _send_character_sheets_via_email, \
    analyze_and_normalize_game_items, load_localized_rst_template
from rpg_sheet_generator import display_and_check_story_tags

rpg.enter_docs_folder()

BUILD_ARGUMENTS = rpg.parse_build_arguments(with_clues_option=True)  # eg. "--lang en --with-clues" on command line
LANGUAGE = BUILD_ARGUMENTS.lang

INITIAL_GAME_DATA_DUMP = os.path.join(os.path.dirname(__file__), "_initial_game_data_dump.yaml")

DISABLE_DECORATIONS = False

TEMPLATES_ROOT = os.path.abspath("../script_fixtures/mysteryparty_archives")
TEMPLATES_COMMON = os.path.abspath("../script_fixtures/mysteryparty_common")
ALL_CLUES_DOCUMENT = os.path.join(TEMPLATES_ROOT, "miscellaneous", "ingame_clues_archives.odt")  # French

STANDARD_EXTRA_ARGS = "--stylesheets=simple_tight"
DECORATIONS_EXTRA_ARGS = "--stylesheets=simple_large,dark_background_with_frame"  # Use --show-frame-boundary (if necessary to debug)
BIG_FONT_EXTRA_PARAMS = "--stylesheets=big_font"

MAIN_OUTPUT_DIR = os.path.join("output_archives", LANGUAGE)
DOCUMENTS_OUTPUT_DIR = os.path.join(MAIN_OUTPUT_DIR, "documents")

if not os.path.exists(DOCUMENTS_OUTPUT_DIR):
    os.makedirs(DOCUMENTS_OUTPUT_DIR)

jinja_env = rpg.load_jinja_environment([TEMPLATES_ROOT, TEMPLATES_COMMON], use_macro_tags=True, language=LANGUAGE)

DOCUMENT_TITLES = dict(
    fr=dict(game_title="Les archives secrètes des Maupertuis",
            common_lore_and_game_rules="Univers et Règles du Jeu ",
            common_npc_information="Compléments des Figurants",
            table_of_contents="Table des Matières"),
    en=dict(game_title="The Secret Archives of the Maupertuis",
            common_lore_and_game_rules="Game Universe and Rules",
            common_npc_information="NPC Actors' Supplements",
            table_of_contents="Table of Contents"),
)[LANGUAGE]

OFFICIAL_NAMES = dict(
    fr=dict(
        diakon_dispeller="Le désenvoûteur", diakon_exorcist="L'exorciste", diakon_invoker="L'invocateur",
        explorer_unveiler="Le dévoileur", explorer_anthropologist="L'anthropologue", explorer_runologist="Le runologue",
        parcival_alchemist="L'alchimiste", parcival_woodsman="Le gardien des bois", parcival_oracle="L'oracle",
        spy_lockpicker="Le crocheteur", spy_minesweeper="Le démineur", spy_sounder="Le sondeur",
        dragons="Les déchus",
        avatar_druid="Le druide", avatar_duchess="La duchesse", avatar_inventor="L'inventeur",
        phantom_archivist="L'archiviste", phantom_arkon="L'arkonte", phantom_octave="Octave",
        phantom_magus="Le Mage Mos Peratys", phantom_beast="La Bête", phantom_thief="Le voleur",
        god_ankou="L'Ankou", automaton_sentinel="L'automate de garde",
    ),
    en=dict(
        diakon_dispeller="The Dispeller", diakon_exorcist="The Exorcist", diakon_invoker="The Invoker",
        explorer_unveiler="The Unveiler", explorer_anthropologist="The Anthropologist", explorer_runologist="The Runologist",
        parcival_alchemist="The Alchemist", parcival_woodsman="The Woodsman", parcival_oracle="The Oracle",
        spy_lockpicker="The Lockpicker", spy_minesweeper="The Minesweeper", spy_sounder="The Sounder",
        dragons="The Fallen",
        avatar_druid="The Druid", avatar_duchess="The Duchess", avatar_inventor="The Inventor",
        phantom_archivist="The Archivist", phantom_arkon="The Arkon", phantom_octave="Octave",
        phantom_magus="The Magus Mos Peratys", phantom_beast="The Beast", phantom_thief="The Thief",
        god_ankou="The Ankou", automaton_sentinel="The Sentinel Automaton",
    ),
)[LANGUAGE]

_asset_path = lambda x: os.path.join(DOCUMENTS_OUTPUT_DIR, x)

CHARACTER_OVERRIDES = dict(  # ALL must have an "email_attachments" here
    diakon_dispeller=dict(email_attachments=[]),
    diakon_exorcist=dict(email_attachments=[]),
    diakon_invoker=dict(email_attachments=[]),

    explorer_unveiler=dict(email_attachments=[]),
    explorer_anthropologist=dict(email_attachments=[]),
    explorer_runologist=dict(email_attachments=[_asset_path("antic_akarith_runes.pdf"),
                                                _asset_path("secret_codes_converters.pdf")]),

    parcival_alchemist=dict(email_attachments=[]),
    parcival_woodsman=dict(email_attachments=[]),
    parcival_oracle=dict(email_attachments=[]),

    spy_lockpicker=dict(email_attachments=[]),
    spy_minesweeper=dict(email_attachments=[]),
    spy_sounder=dict(email_attachments=[]),

    dragons=dict(email_attachments=[]),
)

NPC_OVERRIDES = dict(
    avatar_druid=dict(email_attachments=[]),
    avatar_duchess=dict(email_attachments=[]),
    avatar_inventor=dict(email_attachments=[]),

    phantom_archivist=dict(email_attachments=[]),
    phantom_arkon=dict(email_attachments=[]),
    phantom_octave=dict(email_attachments=[]),

    phantom_magus=dict(email_attachments=[]),
    phantom_beast=dict(email_attachments=[]),
    phantom_thief=dict(email_attachments=[]),
    god_ankou=dict(email_attachments=[]),
    automaton_sentinel=dict(email_attachments=[]),
)

for _name, _overrides in list(CHARACTER_OVERRIDES.items()) + list(NPC_OVERRIDES.items()):
    _overrides["official_name"] = OFFICIAL_NAMES[_name]

# FIXME rename to "character" template
PLAYER_INITIAL_EMAIL_TEMPLATE = dict(
fr="""\
## Message exclusivement destiné à %(real_life_identity)s (%(real_life_email)s) ##

Bonjour,

Voici votre feuille de personnage pour la soirée mystère "Les archives secrètes des Maupertuis" du *%(mystery_party_date)s*.

Un document à lire et relire sans modération !

Des informations sur l'univers du jeu et les règles, importantes, sont aussi incluses.

Nous vous remercions de bien vouloir :
- acquitter bonne réception de cet email
- signaler toute incohérence ou manque que vous verriez dans ces documents

Bonne lecture !

Amicalement,
Les Organisateurs
""",
en="""\
## Message exclusively intended for %(real_life_identity)s (%(real_life_email)s) ##

Hello,

Here is your character sheet for the mystery evening "The Secret Archives of the Maupertuis" of *%(mystery_party_date)s*.

A document to read and reread without moderation!

Important information about the game universe and the rules is also included.

Please kindly:
- acknowledge receipt of this email
- report any inconsistency or omission you might notice in these documents

Enjoy your reading!

Best regards,
The Organisers
""",
)[LANGUAGE]

AUTOMATA_INITIAL_EMAIl_TEMPLATE = dict(
fr="""
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
""",
en="""
Hello,

Here is some information about the game universe and the rules, for the mystery evening "The Secret Archives of the Maupertuis".

As automaton NPC actors, you don't have a character sheet with a specific role, but you will be able to follow the players in their adventures.

Only the section "How the different worlds work" of the "NPC Actors' Supplements" is important for you, the rest is only there for information.

IMPORTANT - Please kindly:
- acknowledge receipt of this email
- report any inconsistency or gap you might notice in these documents

Enjoy your reading!

Best regards,
The Organisers
""",
)[LANGUAGE]

EMAIL_SUBJECTS = dict(
    fr=dict(player="Soirée Mystère Archives - votre fiche de joueur pour %s",
            npc="Soirée Mystère Archives - votre fiche de figurant pour %s"),
    en=dict(player="Archives Mystery Evening - your player sheet for %s",
            npc="Archives Mystery Evening - your NPC actor sheet for %s"),
)[LANGUAGE]

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

# Content of ingame clues ODT document, as (filename or None to skip, number_of_pages, first_page_snippets):
# snippets are texts that the first page of each clue must contain, per language (or None for pages without text)
INGAME_CLUES_PARTS = [
    ("recipe_flex_elixir_and_clarity_lotion", 1, dict(fr="Elixir Flexifiant Dans", en="Flexifying Elixir In")),
    ("recipe_pyrolitis_tincture", 1, dict(fr="Teinture Pyrolitis -", en="Pyrolitis Tincture -")),
    ("recipe_rejuvenation_cocktail", 1, dict(fr="Cocktail de Réjuvénation", en="Rejuvenation Cocktail Sovereign")),
    ("extra_alchemy_recipes", 1, dict(fr="Notes d’Alchimie Atomique", en="Notes on Atomic Alchemy")),
    ("thanatologue_extract", 4, dict(fr="... alors que la défaite", en="... as defeat seemed")),
    ("meredice_diary_extract", 1, dict(fr="Cher journal, cette", en="Dear diary, this fifth")),
    ("chromacryptographic_messages", 2, None),
    ("parcival_oracle_vision_about_water_mill", 1, None),
    ("parcival_oracle_vision_about_necromancers_and_ring_amplificans", 1, None),
    ("parcival_oracle_vision_about_maupertuis_father_twin_books", 1, None),
    ("parcival_oracle_shared_vision_about_world_threat", 3, None),
    ("parcival_oracle_vision_about_chaos_novel_tome_3", 1, dict(fr="CHAOS T3 ZOOLOGIE", en="CHAOS V3 ZOOLOGY GASTRONOMY")),
    ("secret_codes_converters", 1, dict(fr="Codes Secrets Connus", en="Known Secret Codes")),
    ("unreadable_runes", 2, None),
    ("antic_akarith_runes", 1, dict(fr="Deux Cryptorunes Akarites", en="Two Antique Akarith")),
    ("maupertuis_father_chest_code_anamorphosis_enigma", 1, None),
    ("maupertuis_whispering_box_enigma", 1, dict(fr="(Énigme de la Boite", en="(Whispering Box Riddle)")),
    ("octave_diary_on_his_tomb", 1, dict(fr="Cher journal intime,", en="Dear diary, For ages")),
    ("letters_to_maupertuis_parents", 2, dict(fr="Le 23 Septemaire 500", en="23 Septemaire 500")),
    ("octave_instructions_for_initiation", 1, dict(fr="Octave, voici les", en="Octave, here are the")),
    ("avatar_novel_summaries", 2, dict(fr="Roman « Les cygnes", en="Novel \"The Pond Swans\"")),
    ("conspiracy_anti_arkon_letter_with_coast_of_arms", 1, dict(fr="Mon cher Fils dans", en="My dear Son in the Yods,")),
    ("archivist_diary_in_his_case", 4, dict(fr="8 octobaire 500 Ô que", en="8 octobaire 500 O,")),
    ("book_shelf_labels_for_library1", 1, dict(fr="RAYON ZOOLOGIE RAYON", en="ZOOLOGY SHELF GASTRONOMY")),
    ("skeleton_danger_symbol", 1, None),
    ("book_shelf_labels_for_library2", 1, dict(fr="GRIMOIRES TEINTURES GRIMOIRES", en="TINCTURE GRIMOIRES PHILTRE")),
    ("maupertuis_caduceus_symbol", 1, None),
    ("coffee_mill_stereogram", 1, None),
    ("miscellaneous_secret_messages", 2, dict(fr="écriteau descriptif pour", en="descriptive sign for")),
    ("trap_and_property_markers", 8, dict(fr="POISON POISON", en="POISON POISON")),
    (None, 1, dict(fr="TRASH PAGE", en="TRASH PAGE")),  # "TRASH PAGE" of document
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
    "npc_automaton_sentinel_sheet": ("npcs/automaton_sentinel_sheet.rst", "automaton_sentinel"),

    # SPECIFIC INSTRUCTIONS
    "planning_details_for_game": ("miscellaneous/planning_details_for_game.rst", "anyone"),
    "planning_of_prophecies": ("miscellaneous/planning_of_prophecies.rst", "anyone"),
    "ingame_speeches": ("miscellaneous/ingame_speeches.rst", "anyone"),
    "enigma_solutions": ("miscellaneous/enigma_solutions.rst", "anyone"),
    "last_minute_instructions_for_participants": (
    "miscellaneous/last_minute_instructions_for_participants.rst", "anyone"),
    "complement_for_diakons": ("miscellaneous/complement_for_diakons.rst", "anyone"),
    "complement_for_explorers": ("miscellaneous/complement_for_explorers.rst", "anyone"),
    "complement_for_parcival": ("miscellaneous/complement_for_parcival.rst", "anyone"),
    "complement_for_spies": ("miscellaneous/complement_for_spies.rst", "anyone"),
    "main_quest_tracking_sheets": ("miscellaneous/main_quest_tracking_sheets.rst", "anyone"),
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
    %s
    #######################################################################################

    %s
    ################################################################ 


    .. raw:: pdf

       PageBreak standardPage

    .. XXX contents:: %s
    ..    :depth: %s

    """) % (DOCUMENT_TITLES["game_title"], title, DOCUMENT_TITLES["table_of_contents"], toc_depth)

    for part in parts:
        if callable(part):
            new_data = part(jinja_context=jinja_context)  # builder function
        else:
            new_data = load_localized_rst_template(part, [TEMPLATES_ROOT, TEMPLATES_COMMON], LANGUAGE)
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
        extra_args = DECORATIONS_EXTRA_ARGS if with_decorations else STANDARD_EXTRA_ARGS

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
        toc_depth=toc_depth,
        language=LANGUAGE,
    )


def generate_archives_sheets():
    _ensure_intial_game_data_dump_is_present(INITIAL_GAME_DATA_DUMP)  # IMPORTANT

    all_data = dict()

    data = rpg.load_localized_yaml_file(INITIAL_GAME_DATA_DUMP, LANGUAGE)  # no translated dump exists for now
    all_data.update(data)

    murder_party_items_raw = rpg.load_localized_yaml_file(os.path.join(TEMPLATES_ROOT, "gamemaster_assets_checklist.yaml"), LANGUAGE)

    important_marker = " IMPORTANT"
    murder_party_items = analyze_and_normalize_game_items(murder_party_items_raw, important_marker=important_marker)

    all_data["murder_party_items"] = murder_party_items

    # pprint(murder_party_items)

    # Sort items between crates dependong on @CRATE start markers
    murder_party_items_per_crate = OrderedDict()

    def _extract_crate(_title):
        crate = None
        new_title = _title
        assert new_title, repr(new_title)
        # print(">>>>> SEARCHING CRATE IN TITLE", _title)
        match = re.search(r"^@\S+\s", _title)
        if match:
            crate = match.group(0)
            new_title = new_title.replace(crate, "")
            crate = crate.strip()  # Remove trailing spaces
        return crate, new_title

    total_item_entry_count = 0
    for murder_party_item_group in murder_party_items:

        if len(murder_party_item_group) != 2:
            raise ValueError("Value should be a PAIR: %s" % murder_party_items)

        section, item_details_list = murder_party_item_group
        crate, section = _extract_crate(section)
        default_create = crate or section
        for item_details in item_details_list:
            item_label = item_details["item_label"]
            item_is_important = item_details["item_is_important"]
            # if item_details["item_is_important"]:
            # print(repr(item_label))
            # item_label = "*%s*" % item_label
            item_crate, item_label = _extract_crate(item_label)
            item_crate = item_crate or default_create
            assert item_crate, repr(item_crate)
            murder_party_items_per_crate.setdefault(item_crate, [])
            murder_party_items_per_crate[item_crate].append((item_label, item_is_important))
            ##print(item_label)
            total_item_entry_count += 1

    murder_party_items_per_crate = OrderedDict(sorted(murder_party_items_per_crate.items()))
    print(">>>> COUNT OF GAME ASSET ITEMS SEEN:", total_item_entry_count)

    # pprint(murder_party_items_per_crate)
    all_data["murder_party_items_per_crate"] = murder_party_items_per_crate.items()

    # BEWARE - sensitive data specific to a murder party game
    data = rpg.load_yaml_file("../script_fixtures/local.yaml")  # must exist, see local.yaml.example
    local_character_overrides = data.pop("_CHARACTER_OVERRIDES_")
    local_npc_overrides = data.pop("_NPC_OVERRIDES_")
    all_data.update(data)

    all_data["player_names"] = player_names
    # print("-------->", player_names)

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

    if False:  # BEWARE DANGEROUS EMAIL SENDING

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

            ###### SECOND SESSION : npc_names = ["phantom_arkon", "phantom_archivist", "phantom_octave", "avatar_inventor"]

            forced_recipient_email = "chambon.pascal@gmail.com"
            _send_character_sheets_via_email(all_data=all_data, player_names=player_names,
                                             forced_recipient_email=forced_recipient_email,
                                             subject=EMAIL_SUBJECTS["player"],
                                             email_template=PLAYER_INITIAL_EMAIL_TEMPLATE,
                                             default_email_attachments=default_player_attachments,
                                             allow_duplicate_emails=True,
                                             dry_run=dry_run)  # ensure everything seems in place
            # _send_character_sheets_via_email(all_data=all_data, player_names=npc_names, forced_recipient_email=forced_recipient_email,
            #                              subject=EMAIL_SUBJECTS["npc"],
            #                              email_template=PLAYER_INITIAL_EMAIL_TEMPLATE,
            #                              default_email_attachments=default_npc_attachments, allow_duplicate_emails=True, dry_run=dry_run)  # ensure everything seems in place

        print("----------FAKE--------------")
        _send_everything(dry_run=True)

        if False:
            print("----------REAL--------------")
            _send_everything(dry_run=False)  # REALLY send stuffs

        print(">> STOPPING AFTER SUCCESSFUL EMAIL TREATMENT <<")
        sys.exit()  # only do that, always

    # -------------

    if BUILD_ARGUMENTS.with_clues:
        export_ingame_clues_pdfs(ALL_CLUES_DOCUMENT, clues_parts=INGAME_CLUES_PARTS,
                                 output_dir=DOCUMENTS_OUTPUT_DIR, language=LANGUAGE)

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
    if True:
        isolated_data["current_player_id"] = "everyone"
        build_archives_pdf(COMMON_LORE_AND_RULES,
                           filename_base="common_lore_and_game_rules", title=DOCUMENT_TITLES["common_lore_and_game_rules"],
                           add_page_breaks=True, jinja_context=isolated_data)

        isolated_data["current_player_id"] = "npcs"
        build_archives_pdf(COMMON_NPC_DOCS,
                           filename_base="common_npc_information", title=DOCUMENT_TITLES["common_npc_information"],
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

    # -------------

    def _get_player_context(_player_name):
        player_data = all_data.copy()
        player_data["current_player_id"] = _player_name
        # _character_properties = all_data["character_properties"][_player_name]
        return player_data

    # then character full sheets
    if True:
        for player in player_names:
            parts = [(part % dict(player_name=player) if not callable(part) else part)
                     for part in PLAYER_MANUAL_PARTS]
            # print("COMPILING", player, parts)
            character_displayed_name = (all_data["character_properties"][player].get("official_name", player)
                                        if player in all_data["character_properties"]
                                        else player)
            player_data = _get_player_context(player)
            build_archives_pdf(parts, filename_base="player_%s_sheet_full" % player,
                               title="%s" % character_displayed_name, jinja_context=player_data)

    # -------------

    # then resolve fact/hint tags from the ODT clues file
    if True:
        _register_story_tags_from_clues_document(ALL_CLUES_DOCUMENT, jinja_env=jinja_env, language=LANGUAGE,
                                                 comment_samples=dict(fr="petite sœur des Parcival",
                                                                      en="cure the Parcivals' little sister"))

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
        print("Script over, all is coherent")


def test_generation():
    # to use pytest with this builder, and get nifty stack traces
    generate_archives_sheets()


if __name__ == "__main__":
    generate_archives_sheets()
