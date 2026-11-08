# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import io
import os
import re
import rpg_sheet_generator as rpg
import sys

import docutils.core

LANGUAGE = rpg.get_build_language()  # use "--lang en" on command line for English documents

DOC_DIR = os.path.dirname(os.path.abspath(__file__))
# The French manual is also loaded by the Pychronia game, so it keeps its unsuffixed name
YAML_FILE = ("../script_fixtures/gamemaster_manual.yaml" if LANGUAGE == "fr" else
             rpg.localize_filename("../script_fixtures/gamemaster_manual.yaml", LANGUAGE))
TEMP_DIR = os.path.join("output_auction", LANGUAGE)

if not os.path.exists(YAML_FILE):
    sys.exit("No gamemaster manual is available for language %r (missing %s)" % (LANGUAGE, YAML_FILE))
PDFTK_EXE = r'''C:\Program Files (x86)\pdftk4all\pdftk.exe'''

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


def generate_manual(sections, output_file_template, remove_second_page, unlink_unknown_targets=False):
    all_data = rpg.load_yaml_file(YAML_FILE)
    data = all_data["gamemaster_manual"]

    version = data["version"]

    sections_texts = [data[section] for section in sections]

    rst_file = os.path.join(TEMP_DIR, (output_file_template % version) + ".rst")
    rpg.write_rst_file(rst_file, data=sections_texts, language=LANGUAGE)
    if unlink_unknown_targets:
        unlink_unknown_rst_targets(rst_file)

    pdf_file = os.path.join(TEMP_DIR, (output_file_template % version) + ".pdf.tmp")

    rpg.convert_rst_file_to_pdf(rst_file, pdf_file,
                                conf_file=RST2PDF_CONF_FILE,
                                extra_args=EXTRA_ARGS)

    pdf_file_improved = pdf_file[:-4]  # without ".tmp"

    if remove_second_page:
        # you can use a printer like cutePdf to print pages 1, 3-41 of the manual and thus remove the nasty blank page, or just use this:
        if os.path.isfile(PDFTK_EXE):

            # this is buggy if multiple '"' in command line...
            cmd = ''' "%s" %s cat 1 3-end output %s dont_ask ''' % (PDFTK_EXE, pdf_file, pdf_file_improved)
            os.system(cmd)
        else:
            print(
                "WARNING, couldn't remove blank pdf pages from '%s' using pdftk.exe, please do it manually" % pdf_file)
    else:
        if os.path.exists(pdf_file_improved):
            os.remove(pdf_file_improved)
        os.rename(pdf_file, pdf_file_improved)


generate_manual(["pdf_prefix", "public_content", "spoiler_content"],
                output_file_template="chrysalis_auction_gamemaster_manual_%s_full",
                remove_second_page=False)

# Some RST links are broken in this extract, since it lacks some sections, so we unlink them
generate_manual(["pdf_prefix", "public_content", "truncation_message"],
                output_file_template="chrysalis_auction_gamemaster_manual_%s_extract",
                remove_second_page=False,
                unlink_unknown_targets=True)

print("Script Over")
