# -*- coding: utf-8 -*-
"""
Check that the English sources of the Chrysalis games contain no accented letters: English texts write names and
loanwords without accents (Josephine, Selene, cafe, fiance...). The checked files are the "<name>_en.<ext>" texts
(rst, txt, yaml) and OpenDocument files (odt, odp, odg) of the repository.

Some accented texts are legitimate, and left untouched:

- jinja2 tags other than "symbol" ones, and jinja2 comments: their strings are French data keys
  ({% xfact "..." %}, {% if section == "..." %}...), which must match those of French sources;
- the texts of ALLOWED_ACCENTED_TEXTS below;
- in OpenDocument files, everything but the texts of the document (e.g. style names).

Usage (from any folder):  python common_assets/tools/check_english_accents.py [--fix] [files or folders...]

Without --fix, accented words are listed and the exit code is 1 if any is found; with --fix, accents are removed in
place (other characters, line endings and BOMs are kept as is).
"""

import argparse
import os
import re
import sys
import unicodedata
import zipfile

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.join(THIS_DIR, "..", "..")

TEXT_EXTENSIONS = (".rst", ".txt", ".yaml", ".yml")
OPENDOCUMENT_EXTENSIONS = (".odt", ".odp", ".odg")
OPENDOCUMENT_XML_PARTS = ("content.xml", "styles.xml")
EXCLUDED_DIRS = {".git", ".claude", "___Trash", "_build", "_output", "savegames"}

# Accented texts which must stay as is in English sources
ALLOWED_ACCENTED_TEXTS = [
    "Ventes Privées d'Alphonse",  # Mindstorm: data key of a document section, in English sources too
    '"é", "è", "ê"',  # Mindstorm duel of honour rules: examples of accented letters
    "Pour le jour où je l'oublierai",  # Archives clues: French caption of a picture, quoted in a gamemaster comment
]

# Jinja2 tags (except "symbol" ones, whose value is displayed) and comments
PROTECTED_TAG_REGEX = re.compile(r"\{%-?(?!\s*symbol\b).*?%\}|\{#.*?#\}", re.DOTALL)
WORD_REGEX = re.compile(r"[^\W\d_]+")


def remove_accent(char):
    """Return the character without its accents (diacritics), e.g. "é" -> "e"; "½", "²" or "œ" are kept."""
    decomposed = unicodedata.normalize("NFD", char)
    stripped = "".join(c for c in decomposed if unicodedata.category(c) != "Mn")
    return unicodedata.normalize("NFC", stripped) if stripped else char


def has_accent(char):
    return ord(char) > 127 and remove_accent(char) != char


def get_protected_mask(text, only_xml_text_nodes=False):
    """Return a list of booleans, True for the characters of text which must not be modified."""
    protected = [False] * len(text)
    spans = [m.span() for m in PROTECTED_TAG_REGEX.finditer(text)]
    for allowed in ALLOWED_ACCENTED_TEXTS:
        variants = {allowed, allowed.replace('"', "&quot;").replace("'", "&apos;")}
        spans += [m.span() for variant in variants for m in re.finditer(re.escape(variant), text)]
    if only_xml_text_nodes:
        spans += [m.span() for m in re.finditer(r"<[^>]*>", text)]  # markup, attributes included
    for start, end in spans:
        protected[start:end] = [True] * (end - start)
    return protected


def process_text(text, fix, only_xml_text_nodes=False):
    """Return (new text, list of (offset, accented word)) for the unprotected accented letters of text."""
    if not any(has_accent(c) for c in text):
        return text, []
    protected = get_protected_mask(text, only_xml_text_nodes=only_xml_text_nodes)
    findings = []
    for m in WORD_REGEX.finditer(text):
        if any(has_accent(text[i]) and not protected[i] for i in range(*m.span())):
            findings.append((m.start(), m.group(0)))
    if fix and findings:
        text = "".join(remove_accent(c) if (not protected[i] and has_accent(c)) else c for i, c in enumerate(text))
    return text, findings


def process_text_file(path, fix):
    data = open(path, "rb").read().decode("utf-8")  # a BOM, if any, is kept as a character
    new_data, findings = process_text(data, fix=fix)
    report = ["%s:%d: %s" % (path, data.count("\n", 0, offset) + 1, word) for offset, word in findings]
    if fix and new_data != data:
        open(path, "wb").write(new_data.encode("utf-8"))
    return report


def process_opendocument_file(path, fix):
    report = []
    new_parts = {}
    with zipfile.ZipFile(path) as archive:
        for part in OPENDOCUMENT_XML_PARTS:
            if part not in archive.namelist():
                continue
            xml = archive.read(part).decode("utf-8")
            new_xml, findings = process_text(xml, fix=fix, only_xml_text_nodes=True)
            report += ["%s [%s]: %s" % (path, part, word) for _offset, word in findings]
            if new_xml != xml:
                new_parts[part] = new_xml.encode("utf-8")
        if fix and new_parts:
            tmp_path = path + ".tmp"
            with zipfile.ZipFile(tmp_path, "w") as new_archive:
                for info in archive.infolist():  # same order, "mimetype" first and uncompressed
                    new_archive.writestr(info, new_parts.get(info.filename, archive.read(info.filename)),
                                         compress_type=info.compress_type)
    if fix and new_parts:
        os.replace(tmp_path, path)
    return report


def iter_english_files(paths):
    for path in paths:
        if os.path.isfile(path):
            yield path
            continue
        for dirpath, dirnames, filenames in os.walk(path):
            dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDED_DIRS)
            for filename in sorted(filenames):
                stem, extension = os.path.splitext(filename)
                if stem.endswith("_en") and extension.lower() in TEXT_EXTENSIONS + OPENDOCUMENT_EXTENSIONS:
                    yield os.path.join(dirpath, filename)


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--fix", action="store_true", help="remove accents in place")
    parser.add_argument("paths", nargs="*", help="files or folders to check (default: the whole repository)")
    args = parser.parse_args()
    sys.stdout.reconfigure(errors="backslashreplace")  # consoles may not support all characters

    report = []
    for path in iter_english_files([os.path.normpath(p) for p in args.paths] or [os.path.normpath(DEFAULT_ROOT)]):
        if path.lower().endswith(OPENDOCUMENT_EXTENSIONS):
            report += process_opendocument_file(path, fix=args.fix)
        else:
            report += process_text_file(path, fix=args.fix)

    for line in report:
        print(line)
    if args.fix:
        print("%d accented words fixed" % len(report))
        return 0
    print("%d accented words found" % len(report))
    return 1 if report else 0


if __name__ == "__main__":
    sys.exit(main())
