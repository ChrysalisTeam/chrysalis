# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import io
import os
import re
import rpg_sheet_generator as rpg
import sys

import docutils.core

rpg.enter_docs_folder()

LANGUAGE = rpg.parse_build_arguments().lang  # use "--lang en" on command line for English documents

# Both manuals are also loaded by the Pychronia game, depending on the language of each game instance
YAML_FILE = rpg.localize_filename("../alternate_reality_game_auction/scenario_fixtures/gamemaster_manual.yaml", LANGUAGE)
TEMP_DIR = os.path.join("output_auction", LANGUAGE)

if not os.path.exists(YAML_FILE):
    sys.exit("No gamemaster manual is available for language %r (missing %s)" % (LANGUAGE, YAML_FILE))

EXTRA_ARGS = "--stylesheets=shiny"
RST2PDF_CONF_FILE = "./rst2pdf.conf"


def unlink_unknown_rst_targets(rst_file):
    """
    Turn references to missing targets (eg. sections absent from a truncated manual) into plain text,
    since recent rst2pdf versions abort on "Unknown target name" errors.
    """
    with open(rst_file, "r", encoding="utf8") as f:
        rst_content = f.read()

    warning_stream = io.StringIO()
    docutils.core.publish_doctree(rst_content, settings_overrides=dict(halt_level=5, report_level=3,
                                                                       warning_stream=warning_stream))
    unknown_targets = set(re.findall(r'Unknown target name: "(.+?)"\.', warning_stream.getvalue()))
    if not unknown_targets:
        return

    print("Unlinking unknown RST targets in %s: %s" % (rst_file, sorted(unknown_targets)))

    def _unlink(matchobj):
        name = matchobj.group(1)
        normalized_name = " ".join(name.split()).lower()  # like docutils.nodes.fully_normalize_name()
        return name if normalized_name in unknown_targets else matchobj.group(0)

    rst_content = re.sub(r'`([^`<>]+)`_(?!_)', _unlink, rst_content)
    with open(rst_file, "w", encoding="utf8") as f:
        f.write(rst_content)


def generate_manual(sections, output_file_template, unlink_unknown_targets=False):
    all_data = rpg.load_yaml_file(YAML_FILE)
    data = all_data["gamemaster_manual"]

    version = data["version"]

    sections_texts = [data[section] for section in sections]

    rst_file = os.path.join(TEMP_DIR, (output_file_template % version) + ".rst")
    rpg.write_rst_file(rst_file, data=sections_texts, language=LANGUAGE)
    if unlink_unknown_targets:
        unlink_unknown_rst_targets(rst_file)

    pdf_file = os.path.join(TEMP_DIR, (output_file_template % version) + ".pdf")

    rpg.convert_rst_file_to_pdf(rst_file, pdf_file,
                                language=LANGUAGE,
                                conf_file=RST2PDF_CONF_FILE,
                                extra_args=EXTRA_ARGS)


generate_manual(["pdf_prefix", "public_content", "spoiler_content"],
                output_file_template="chrysalis_auction_gamemaster_manual_%s_full")

# Some RST links are broken in this extract, since it lacks some sections, so we unlink them
generate_manual(["pdf_prefix", "public_content", "truncation_message"],
                output_file_template="chrysalis_auction_gamemaster_manual_%s_extract",
                unlink_unknown_targets=True)

print("Script Over")
