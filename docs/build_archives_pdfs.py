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

from mysteryparty_common_utils import build_mysteryparty_pdf, _ensure_intial_game_data_dump_is_present, \
    _extract_ingame_clues_text_from_odt, _generate_clues_pdfs_from_main_odt_document
from rpg_sheet_generator import display_and_check_story_tags

IS_STANDALONE = True

INITIAL_GAME_DATA_DUMP = os.path.join(os.path.dirname(__file__), "_initial_game_data_dump.yaml")

DISABLE_DECORATIONS = False

TEMPLATES_ROOT = os.path.abspath("../script_fixtures/mysteryparty_archives")
TEMPLATES_COMMON = os.path.abspath("../script_fixtures/mysteryparty_common")
ALL_CLUES_DOCUMENT = os.path.join(TEMPLATES_ROOT, "miscellaneous", "ingame_clues_archives.odt")

DOC_DIR = os.path.dirname(os.path.abspath(__file__))
STANDARD_EXTRA_ARGS = "--stylesheets=simple_tight"
DECORATIONS_EXTRA_ARGS = "--stylesheets=simple_large,dark_background_with_cover"

MAIN_OUTPUT_DIR = "output_archives"
DOCUMENTS_OUTPUT_DIR = os.path.join(MAIN_OUTPUT_DIR, "documents")

if not os.path.exists(DOCUMENTS_OUTPUT_DIR):
    os.mkdir(DOCUMENTS_OUTPUT_DIR)



jinja_env = rpg.load_jinja_environment([TEMPLATES_ROOT, TEMPLATES_COMMON], use_macro_tags=True)

EXCLUDED_CHARACTERS = []  # mystery-party has no sheet for these characters, for now

_asset_path = lambda x: os.path.join(DOCUMENTS_OUTPUT_DIR, x)


CHARACTER_OVERRIDES = dict(  # ALL must have an "email_attachments" here
    diakon_dispeller=dict(email_attachments=[]),
    diakon_exorcist=dict(email_attachments=[]),
    diakon_invoker=dict(email_attachments=[]),

    explorer_analyser=dict(email_attachments=[]),
    explorer_anthropologist=dict(email_attachments=[]),
    explorer_runologist=dict(email_attachments=[]),

    parcival_alchemist=dict(email_attachments=[]),
    parcival_woodsman=dict(email_attachments=[]),
    parcival_oracle=dict(email_attachments=[]),

    spy_lockpicker=dict(email_attachments=[]),
    spy_minesweeper=dict(email_attachments=[]),
    spy_sounder=dict(email_attachments=[]),
)

players_names = set(CHARACTER_OVERRIDES.keys())


GAMEMASTER_MANUAL_PARTS = [
    "gamemaster_manual_archives.rst",
]

PLAYER_MANUAL_PARTS = [
    "players/%(player_name)s_role.rst",
]

COMMON_LORE_DOCS = [
    #"context_intro.rst",
    #"context_details.rst",
    #"common_guests_gallery.rst",
    "game_rules.rst",
]

# BEWARE, be careful when regenerating PDF clues, that their titles and content match well!

INGAME_CLUES_PARTS = [  # content of ingame clues ODT document, as (filename, number_of_mages)
    ("recipe_flex_elixir_and_clarity_lotion", 1),
    ("recipe_pyrolitis_tincture", 1),
    ("recipe_rejuvenation_cocktail", 1),
    ("thanatologue_extract", 2),
    ("meredice_diary_extract", 1),
    ("parcival_oracle_vision_about_water_mill", 1),
    ("parcival_oracle_vision_about_necromancers_and_scepter_amplificans", 1),
    ("parcival_oracle_vision_about_maupertuis_father_twin_books", 1),
    ("secret_codes", 1),
]

# documents without decorations, typically ; one can provide a LIST of RST files as value
ISOLATED_DOCS = {
    # GAMEMASTER DOCS
    #"gamemaster_assets_checklist": "gamemaster_assets_checklist.rst",
    # NPCS
    "npc_avatar_druid_sheet": "npcs/avatar_druid_sheet.rst",
    "npc_avatar_inventor_sheet": "npcs/avatar_inventor_sheet.rst",
    "npc_avatar_princess_sheet": "npcs/avatar_princess_sheet.rst",
    "npc_phantom_archivist_sheet": "npcs/phantom_archivist_sheet.rst",
    "npc_phantom_arkon_sheet": "npcs/phantom_arkon_sheet.rst",
    "npc_phantom_octave_sheet": "npcs/phantom_octave_sheet.rst",
    "npc_phantom_thief_sheet": "npcs/phantom_thief_sheet.rst",

    # FACTIONS
    "faction_diakon_sheet.rst": "factions/diakon_group_sheet.rst",
    "faction_explorer_sheet.rst": "factions/explorer_group_sheet.rst",
    "faction_parcival_sheet.rst": "factions/parcival_group_sheet.rst",
    "faction_spy_sheet.rst": "factions/spy_group_sheet.rst",
    # INFORMATION
    "documents/knowledge_about_phantoms.rst": "miscellaneous/knowledge_about_phantoms.rst",

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
    HIDDEN ARCHIVES
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

    return build_mysteryparty_pdf(
        parts=parts,
        filename_base=filename_base,
        title=title,
        output_dir=MAIN_OUTPUT_DIR,
        generate_rst_from_parts=generate_archives_rst_from_parts,
        jinja_env=jinja_env,
        extra_args= DECORATIONS_EXTRA_ARGS if with_decorations else STANDARD_EXTRA_ARGS,
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

    # BEWARE - sensitive data specific to a murder party game
    data = rpg.load_yaml_file("../script_fixtures/local.yaml")  # must exist, see local.yaml.example
    all_data.update(data)

    all_data["players_names"] = players_names
    #print("-------->", players_names)

    master_login = all_data["global_parameters"]["master_login"]

    for k, v in CHARACTER_OVERRIDES.items():
        all_data["character_properties"].setdefault(k, {})  # Create character if necessary
        all_data["character_properties"][k].update(v)  # we override official names mainly

    ''' UNUSED
    for k, v in all_data["character_properties"].items():
        #print("HANDLING CHARACTER", k)

        # additional variables to DRY display
        official_name = all_data["character_properties"][k]["official_name"]
        full_official_title = "%s, %s" % (official_name,
                                          all_data["character_properties"][k]["official_role"])
        all_data["character_properties"][k]["full_official_title"] = full_official_title
    '''

    # for standalone docs
    isolated_data = all_data.copy()
    isolated_data["current_player_id"] = None

    # -------------

    if False:
        # export clues into a myriad of small PDFs
        _generate_clues_pdfs_from_main_odt_document(input_doc=ALL_CLUES_DOCUMENT,
                                                    clues_parts=INGAME_CLUES_PARTS,
                                                    output_dir=DOCUMENTS_OUTPUT_DIR)
    # -------------

    if False:  # BEWARE DANGEROUS

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
        gm_data["current_player_id"] = master_login  # silent
        build_archives_pdf(GAMEMASTER_MANUAL_PARTS,
                            filename_base="chrysalis_archives_gamemaster_manual", title="Maître de Jeu",
                            add_page_breaks=True, jinja_context=gm_data, toc_depth=2)

    # -------------

    # then the common LORE doc
    if True:
        build_archives_pdf(COMMON_LORE_DOCS,
                            filename_base="common_lore_introduction", title="Univers du Jeu",
                            add_page_breaks=True, jinja_context=isolated_data)

    # -------------

    # then miscellaneous docs, eg. NPC sheets, last-minute context, checklists (which might be included by other sheets)...
    if True:
        for filename_base, doc in sorted(ISOLATED_DOCS.items()):
            build_archives_pdf([doc] if not isinstance(doc, (list, tuple)) else doc,
                                filename_base=filename_base,
                                title=None,
                                with_decorations=False,
                                jinja_context=isolated_data)

    # -------------

    def _get_player_context(_player_name):
        player_data = all_data.copy()
        player_data["current_player_id"] = _player_name
        #_character_properties = all_data["character_properties"][_player_name]
        return player_data

    # then character full sheets
    if False:
        for player in players_names:
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
        for player in sorted(players_names_set_no_shark):
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

    '''
    if facts_summary:
        build_mindstorm_pdf(["gamemaster_facts_summary.rst"],
                            filename_base="gamemaster_facts_summary",
                            title=None,
                            with_decorations=False,
                            jinja_context=dict(facts_summary=facts_summary))
    else:
        print("!!! Aborting generation of gamemaster_facts_summary, since NO FACTS have been detected")
    '''

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
