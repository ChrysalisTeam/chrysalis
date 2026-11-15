# -*- coding: utf-8 -*-
"""
Variables hook of the Mindstorm storygen project (see "variables_hook" in configuration.yaml).

It ports what docs/build_mindstorm_pdfs.py computed besides rendering sheets: game data normalization, per-language
titles and abilities, character names/titles, player list, items checklist, and a jinja2 filter.
"""
import glob
import logging
import os
import re


# Values of the "game_type" root variable (see configuration.yaml), mapped to the "standalone" flag of templates;
# the "*.postauction.custom_*.rst" files are placeholders to customize for each game
GAME_TYPES = {"anteauction.standalone": True, "postauction.custom": False}

EXCLUDED_CHARACTERS = []  # mystery-party has no sheet for these characters, for now

IMPORTANT_MARKER = " IMPORTANT"

DOCUMENT_TITLES = dict(
    fr=dict(gamemaster_manual="Maître de Jeu", common_lore="Univers du Jeu", table_of_contents="Table des Matières"),
    en=dict(gamemaster_manual="Game Master", common_lore="The Game Universe", table_of_contents="Table of Contents"),
)

# Maps required permissions to ability descriptions
AVAILABLE_ANTHROPIA_ABILITIES = dict(
    fr={
        "access_mercenaries_hiring": "Embauche de mercenaires dans une grande ville de la planète",
        ###"access_wiretapping": "Mise sur écoute d'un autre compte Anthropia (et protection contre les écoutes adverses)",
        "access_runic_translation": "Traduction de runes akarites à partir de leur transcription",
        "access_matter_analysis": "Analyse biophysique d'un objet",
        "access_world_scan": "Recherche par scanner mondial des clones d'un objet",
        "access_house_reports": "Rapports de vidéosurveillance du manoir de Loyd Georges",
        "access_geoip_location": "Géolocalisation de l'émetteur d'un message email",
        ###(xxx, "Tiers de confiance numérique (à mettre en copie des messages contractuels)"),
    },
    en={
        "access_mercenaries_hiring": "Mercenary hiring in a major city of the planet",
        "access_runic_translation": "Translation of Akarith runes from their transcription",
        "access_matter_analysis": "Biophysical analysis of an object",
        "access_world_scan": "World-scanner search for clones of an object",
        "access_house_reports": "CCTV reports of Loyd Georges' manor",
        "access_geoip_location": "Geolocation of the sender of an email message",
    },
)


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
        # checklists without any marker (e.g. Mindstorm) must not get ALL their items de-emphasized (italic)
        for (_section, items) in game_items:
            for item in items:
                item["item_is_important"] = True
    return game_items


def _strip_gamemaster_hints(record):
    if record.get("gamemaster_hints"):
        record["gamemaster_hints"] = record["gamemaster_hints"].strip()


def _find_auction_game_file(game_files_root, subfolder, filename):
    """
    Return the path, relative to game_files_root, of the SINGLE file "filename" in its subfolder tree, like
    utilities.find_game_file() of Pychronia; a filename which is already a relative path is only checked.
    """
    if os.path.basename(filename) != filename:
        if not os.path.exists(os.path.join(game_files_root, filename)):
            raise RuntimeError("Game file %r not found in %r" % (filename, game_files_root))
        return filename
    matches = glob.glob(os.path.join(glob.escape(game_files_root), subfolder, "**", glob.escape(filename)),
                        recursive=True)
    if len(matches) != 1:
        raise RuntimeError("Expected a single game file %r in %r, found %r" % (filename, subfolder, matches))
    return os.path.relpath(matches[0], game_files_root).replace(os.sep, "/")


def normalize_portal_game_data(variables, game_files_root):
    """
    Normalize the game data of the Anthropia portal (Auction fixtures deep-merged with the Mindstorm overrides, see
    configuration.yaml) like the Pychronia datamanager and its Mindstorm fixture script do, for the fields used by
    templates.
    """
    for character in variables["character_properties"].values():
        if character.get("avatar"):  # A file name, searched like utilities.find_game_file("images", ...) does
            character["avatar"] = _find_auction_game_file(game_files_root, "images", character["avatar"])
        for field in ("real_life_identity", "real_life_email"):
            if character.get(field) is None:
                character[field] = ""  # Instead of None, for display (sensitive values come from local.yaml)
        if character.get("secret_question") is None:
            character["secret_question"] = ""
        if character.get("extra_goods") is None:
            character["extra_goods"] = ""
        if character.get("permissions") is None:
            character["permissions"] = []
        _strip_gamemaster_hints(character)

    for item in variables["game_items"].values():
        item["auction"] = item.get("auction") or ""
        if len(item["auction"]) != 1:
            item["auction"] = ""  # Only the single-letter lots (A, B...) are auctioned in Mindstorm
        item["total_price"] = item.get("total_price") or 0
        if item.get("image") and not item["image"].startswith(("http://", "https://")):
            item["image"] = _find_auction_game_file(game_files_root, "images", item["image"])
        _strip_gamemaster_hints(item)

    for page in variables["static_pages"].values():
        _strip_gamemaster_hints(page)
    for report in variables["abilities"]["house_reports"]["settings"]["reports"].values():
        _strip_gamemaster_hints(report)


def strip_pychronia_page_markup(text):
    """
    Make a static page of the game data (pychronia RST flavour) embeddable in a sheet, whatever its language:
    drops [BR] tags, demotes section underlines, comments out image directives (their options become part of the
    comment) and drops a bold caption paragraph which immediately precedes an image directive.
    """
    text = text.replace("[BR]", "")
    text = re.sub(r"^[ \t]*\*\*[^\n]*\*\*[ \t]*\n(?:[ \t]*\n)*(?=[ \t]*\.\. image::)", "", text, flags=re.MULTILINE)
    text = text.replace("image::", "brokenimage")
    text = text.replace("=", "-").replace("#", "+")
    return text


def prepare_variables(variables, *, language, jinja_env):
    project_dir = variables["project_dir"]
    assert language in DOCUMENT_TITLES, "Mindstorm must be built with --variable lang=fr|en, not %r" % language

    game_type = variables.get("game_type")
    assert game_type in GAME_TYPES, "Variable 'game_type' must be one of %s, not %r" % (sorted(GAME_TYPES), game_type)
    variables["standalone"] = GAME_TYPES[game_type]

    game_files_root = os.path.join(project_dir, "..", "..", "alternate_reality_game_auction")
    normalize_portal_game_data(variables, game_files_root=game_files_root)

    variables["document_titles"] = DOCUMENT_TITLES[language]
    variables["available_anthropia_abilities"] = AVAILABLE_ANTHROPIA_ABILITIES[language]

    variables["murder_party_items"] = analyze_and_normalize_game_items(
        variables.pop("murder_party_items_raw"), important_marker=IMPORTANT_MARKER)

    # BEWARE - sensitive data specific to a murder party game, see local.yaml.example
    local_character_overrides = variables.pop("_CHARACTER_OVERRIDES_", None) or {}
    variables.pop("_NPC_OVERRIDES_", None)  # only used by other games
    character_properties = variables["character_properties"]
    for k, v in local_character_overrides.items():
        if k in character_properties:  # local.yaml may also contain characters of other games
            character_properties[k].update(v)  # Override real names and emails

    # (the email attachments of the former CHARACTER_OVERRIDES are now in the "email_generation" of configuration.yaml)

    master_login = variables["global_parameters"]["master_login"]
    # configuration.yaml gives this id to the gamemaster manual, whose story tags are masked in the facts summary
    assert master_login == "system", master_login
    variables["master_login"] = master_login  # to mask it in the facts summary

    player_names = sorted(k for (k, v) in character_properties.items()
                          if not v["is_npc"] and k not in EXCLUDED_CHARACTERS)
    assert "shark" not in player_names
    variables["player_names"] = player_names + ["shark"]  # special player

    # Real photos of guests (see Readme) are optional, avatars are used instead
    photos_dir = os.path.join(project_dir, "..", "..", "common_assets", "trombinoscope")
    player_photos = [os.path.join(photos_dir, "%s-%s.jpg" % (k.capitalize(), v["real_life_identity"]))
                     for (k, v) in character_properties.items() if not v["is_npc"]]
    variables["use_player_photos"] = all(os.path.exists(photo) for photo in player_photos)
    if not variables["use_player_photos"]:
        logging.warning("Some player photos are missing in common_assets/trombinoscope/, using avatars in guests gallery")

    for k, v in character_properties.items():
        # additional variables to DRY display
        official_name = v["official_name"]
        v["full_official_title"] = "%s, %s" % (official_name, v["official_role"])
        v["spoiling_official_name"] = "%s (%s)" % (official_name, k.capitalize())

    jinja_env.filters["strip_pychronia_page_markup"] = strip_pychronia_page_markup  # for texts of the game data

    return variables
