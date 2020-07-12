# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import rpg_sheet_generator as rpg
import sys

DOC_DIR = os.path.dirname(os.path.abspath(__file__))
YAML_FILE = "../script_fixtures/gamemaster_manual.yaml"
TEMP_DIR = "output_auction"
PDFTK_EXE = r'''C:\Program Files (x86)\pdftk4all\pdftk.exe'''

EXTRA_ARGS = "--stylesheets=shiny"
RST2PDF_CONF_FILE = "./rst2pdf.conf"


def generate_manual(sections, output_file_template, remove_second_page):
    all_data = rpg.load_yaml_file(YAML_FILE)
    data = all_data["gamemaster_manual"]

    version = data["version"]

    sections_texts = [data[section] for section in sections]

    rst_file = os.path.join(TEMP_DIR, (output_file_template % version) + ".rst")
    rpg.write_rst_file(rst_file, data=sections_texts)

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

# It is normal to have "Unknown target name" errors with this extract, since some RST links are broken in it...
generate_manual(["pdf_prefix", "public_content", "truncation_message"],
                output_file_template="chrysalis_auction_gamemaster_manual_%s_extract",
                remove_second_page=False)

print("Script Over")
