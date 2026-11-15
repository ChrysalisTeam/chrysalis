# -*- coding: utf-8 -*-
"""
Variables hook of the Archives mystery party ("storygen_hooks.prepare_variables" in configuration.yaml).

It ports the residual logic of the former docs/build_archives_pdfs.py: official character names, document titles,
merge of the (private) local.yaml character overrides, and the computation of the game props structures of the
gamemaster checklists.
"""
import re
from collections import OrderedDict

# Login of the game master: configuration.yaml can't reference variables, so it repeats this value for the
# "current_player_id" of the gamemaster manual, whose story tags are then masked in the facts summary
MASTER_LOGIN = "system"

DEFAULT_LANGUAGE = "fr"

IMPORTANT_MARKER = " IMPORTANT"

DOCUMENT_TITLES = dict(
    fr=dict(game_title="Les archives secrètes des Maupertuis",
            common_lore_and_game_rules="Univers et Règles du Jeu ",
            common_npc_information="Compléments des Figurants",
            table_of_contents="Table des Matières"),
    en=dict(game_title="The Secret Archives of the Maupertuis",
            common_lore_and_game_rules="Game Universe and Rules",
            common_npc_information="NPC Actors' Supplements",
            table_of_contents="Table of Contents"),
)

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
)

# Playing characters (they have full sheets), then NPCs
PLAYER_NAMES = """
    diakon_dispeller diakon_exorcist diakon_invoker
    explorer_unveiler explorer_anthropologist explorer_runologist
    parcival_alchemist parcival_woodsman parcival_oracle
    spy_lockpicker spy_minesweeper spy_sounder
    dragons
""".split()

NPC_NAMES = """
    avatar_druid avatar_duchess avatar_inventor
    phantom_archivist phantom_arkon phantom_octave
    phantom_magus phantom_beast phantom_thief
    god_ankou automaton_sentinel
""".split()


def analyze_and_normalize_game_items(game_items_raw, important_marker: str):
    """Detect game items as normal or important, and build a data tree including this information"""
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
    if not any(item["item_is_important"] for (_section, items) in game_items for item in items):
        # checklists without any marker must not get ALL their items de-emphasized (italic)
        for (_section, items) in game_items:
            for item in items:
                item["item_is_important"] = True
    return game_items


def _extract_crate(_title):
    """Split a title starting with a "@CRATE " marker into (crate or None, title without the marker)"""
    crate = None
    new_title = _title
    assert new_title, repr(new_title)
    match = re.search(r"^@\S+\s", _title)
    if match:
        crate = match.group(0)
        new_title = new_title.replace(crate, "")
        crate = crate.strip()  # Remove trailing spaces
    return crate, new_title


def group_game_items_per_crate(murder_party_items):
    """Sort items between crates depending on @CRATE start markers, return (sorted (crate, items) pairs, items count)"""
    murder_party_items_per_crate = OrderedDict()
    total_item_entry_count = 0
    for murder_party_item_group in murder_party_items:

        if len(murder_party_item_group) != 2:
            raise ValueError("Value should be a PAIR: %s" % murder_party_items)

        section, item_details_list = murder_party_item_group
        crate, section = _extract_crate(section)
        default_crate = crate or section
        for item_details in item_details_list:
            item_label = item_details["item_label"]
            item_is_important = item_details["item_is_important"]
            item_crate, item_label = _extract_crate(item_label)
            item_crate = item_crate or default_crate
            assert item_crate, repr(item_crate)
            murder_party_items_per_crate.setdefault(item_crate, [])
            murder_party_items_per_crate[item_crate].append((item_label, item_is_important))
            total_item_entry_count += 1

    return sorted(murder_party_items_per_crate.items()), total_item_entry_count


def prepare_variables(variables, *, language, jinja_env):
    language = language or DEFAULT_LANGUAGE

    all_data = variables

    # Game props, from the raw checklist data file
    murder_party_items = analyze_and_normalize_game_items(all_data.pop("murder_party_items_raw"),
                                                          important_marker=IMPORTANT_MARKER)
    all_data["murder_party_items"] = murder_party_items
    murder_party_items_per_crate, total_item_entry_count = group_game_items_per_crate(murder_party_items)
    print(">>>> COUNT OF GAME ASSET ITEMS SEEN:", total_item_entry_count)
    all_data["murder_party_items_per_crate"] = murder_party_items_per_crate

    # BEWARE - sensitive data specific to a murder party game, see local.yaml.example
    local_character_overrides = all_data.pop("_CHARACTER_OVERRIDES_")
    local_npc_overrides = all_data.pop("_NPC_OVERRIDES_")

    official_names = OFFICIAL_NAMES[language]
    for names, local_overrides in [(PLAYER_NAMES, local_character_overrides), (NPC_NAMES, local_npc_overrides)]:
        for name in names:
            properties = all_data.setdefault("character_properties", {}).setdefault(name, {})
            properties["official_name"] = official_names[name]
            properties.update(real_life_identity="", real_life_email="")
            properties.update(local_overrides[name])  # Real names and emails

    all_data["player_names"] = list(PLAYER_NAMES)
    all_data["npc_names"] = list(NPC_NAMES)
    all_data["master_login"] = MASTER_LOGIN  # To mask it in the facts summary
    all_data["document_titles"] = DOCUMENT_TITLES[language]
    return all_data
