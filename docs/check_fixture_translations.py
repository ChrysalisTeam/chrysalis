# -*- coding: utf-8 -*-
"""
Check that each English "<name>_en.yaml" fixture of the Auction alternate reality game mirrors its
French "<name>_fr.yaml" source: same keys, same list lengths, same non-text values (numbers, booleans,
emails, file paths, identifiers...), and the same game markup inside texts (game file tags, template
variables, RST directives...), since the Pychronia game expects both languages to be interchangeable.

Usage (from the docs/ folder):  python check_fixture_translations.py [fixture files or folders...]
"""

import argparse
import collections
import glob
import os
import re
import sys

import yaml

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.join(THIS_DIR, "..", "script_fixtures", "alternate_reality_game_auction")

# lists of free texts, whose length may differ between languages (eg. encyclopedia keywords and their FR variants)
FREE_LENGTH_LIST_KEYS = {"keywords"}

# keys whose values are translated even though they look like identifiers (eg. answers players must guess from texts)
TRANSLATABLE_IDENTIFIER_KEYS = {"secret_answer"}

# strings which must stay verbatim in translations (unless they contain spaces, ie. real text)
IDENTIFIER_REGEX = re.compile(r"""^(
    \S+@\S+                                       # email
  | \S*\.(png|jpe?g|gif|mp3|ogg|wav|mp4|webm|flv|pdf|svg|txt|aiml|yaml|html?)  # file path
  | \S*/\S*                                       # path or url
  | [a-z0-9]+(_[a-z0-9]+)+                        # snake_case identifier
  | https?://\S+
)$""", re.VERBOSE | re.IGNORECASE)

# game markup which must be found identically in both languages
MARKUP_REGEXES = [
    re.compile(r"\[GAME_[A-Z_]+[^\]]*\]"),  # game file/url tags, their paths stay unchanged
    re.compile(r"\{\{\s*character_properties[^}]*\}\}"),  # resolved by the game
    re.compile(r"\{%[^%]*%\}"),  # template tags
    re.compile(r"\[(?:BR|NBSP)\]"),
    re.compile(r"\|(?:BR|NBSP)\|"),
    re.compile(r"^\s*\.\.\.?\s*[\w-]+::", re.MULTILINE),  # RST directives (or disabled ones with 3 dots)
    re.compile(r"^\s*:[\w-]+:", re.MULTILINE),  # RST directive options
]

# heuristic to spot French text left untranslated
FRENCH_HINT_REGEX = re.compile(r"\b(les|des|est|une|vous|nous|avec|dans|pour|qui|que|sont|leur|été|à)\b", re.IGNORECASE)


def load_yaml(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        raw = f.read()
    for lineno, line in enumerate(raw.split("\n"), start=1):
        if "\t" in line:
            raise ValueError("Forbidden tabulation at line %d of %s" % (lineno, path))
    return yaml.safe_load(raw)


def _type_name(value):
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, str):
        return "str"
    if isinstance(value, dict):
        return "dict"
    if isinstance(value, list):
        return "list"
    if value is None:
        return "null"
    return type(value).__name__


def _markup_counter(text):
    return collections.Counter(match for regex in MARKUP_REGEXES for match in regex.findall(text))


def compare_trees(fr, en, path, errors, warnings):
    location = ".".join(str(p) for p in path) or "<root>"

    if _type_name(fr) != _type_name(en):
        errors.append("%s: type %s in FR but %s in EN" % (location, _type_name(fr), _type_name(en)))
        return

    if isinstance(fr, dict):
        missing = [k for k in fr if k not in en]
        extra = [k for k in en if k not in fr]
        if missing:
            errors.append("%s: keys missing in EN: %s" % (location, missing))
        if extra:
            errors.append("%s: keys absent from FR: %s" % (location, extra))
        for key in fr:
            if key in en:
                compare_trees(fr[key], en[key], path + [key], errors, warnings)

    elif isinstance(fr, list):
        free_length = (path and path[-1] in FREE_LENGTH_LIST_KEYS and
                       all(isinstance(x, str) for x in fr + en))
        if free_length:
            if bool(fr) != bool(en):
                errors.append("%s: list emptiness differs" % location)
            return
        if len(fr) != len(en):
            errors.append("%s: list of %d items in FR but %d in EN" % (location, len(fr), len(en)))
            return
        for index, (fr_item, en_item) in enumerate(zip(fr, en)):
            compare_trees(fr_item, en_item, path + [index], errors, warnings)

    elif isinstance(fr, str):
        if fr != en and IDENTIFIER_REGEX.match(fr.strip()) and not (path and path[-1] in TRANSLATABLE_IDENTIFIER_KEYS):
            errors.append("%s: identifier-like value changed: %r -> %r" % (location, fr, en))
        if _markup_counter(fr) != _markup_counter(en):
            diff_fr = _markup_counter(fr) - _markup_counter(en)
            diff_en = _markup_counter(en) - _markup_counter(fr)
            errors.append("%s: game markup differs (only FR: %s, only EN: %s)" % (location, dict(diff_fr), dict(diff_en)))
        if fr == en and len(fr) > 25 and " " in fr and len(FRENCH_HINT_REGEX.findall(fr)) >= 2:
            warnings.append("%s: text seems untranslated: %r" % (location, fr[:70]))

    else:
        if fr != en:
            errors.append("%s: value %r in FR but %r in EN" % (location, fr, en))


def find_french_fixtures(entries):
    result = []
    for entry in entries:
        if os.path.isdir(entry):
            result.extend(sorted(glob.glob(os.path.join(entry, "**", "*_fr.yaml"), recursive=True)))
        else:
            result.append(entry if entry.endswith("_fr.yaml") else re.sub(r"(_en)?\.yaml$", "_fr.yaml", entry))
    return result


def check_fixture(fr_file, show_warnings):
    en_file = fr_file[:-len("_fr.yaml")] + "_en.yaml"
    name = os.path.relpath(en_file, os.path.join(THIS_DIR, "..", "script_fixtures"))
    if not os.path.exists(en_file):
        print("MISSING %s" % name)
        return False
    errors, warnings = [], []
    try:
        compare_trees(load_yaml(fr_file), load_yaml(en_file), [], errors, warnings)
    except Exception as e:
        errors.append("can't load the fixtures: %r" % e)
    print("%s %s (%d errors, %d warnings)" % ("OK     " if not errors else "ERRORS ", name, len(errors), len(warnings)))
    for error in errors:
        print("    ERROR %s" % error)
    if show_warnings:
        for warning in warnings:
            print("    WARNING %s" % warning)
    return not errors


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", default=[DEFAULT_ROOT], help="French or English fixture files, or folders")
    parser.add_argument("--no-warnings", action="store_true", help="hide warnings about possibly untranslated texts")
    args = parser.parse_args()

    results = [check_fixture(fr_file, show_warnings=not args.no_warnings)
               for fr_file in find_french_fixtures(args.paths)]
    if not results:
        sys.exit("No French fixture found")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
