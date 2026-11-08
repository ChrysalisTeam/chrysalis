# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import rpg_sheet_generator as rpg
import sys

LANGUAGE = rpg.get_build_language()  # use "--lang en" on command line for English documents

TEMPLATES_ROOT = os.path.abspath("../script_fixtures/descent_rpg")
YAML_FILE = os.path.abspath("../script_fixtures/descent_rpg/descent_rpg_data.yaml")
MASTER_SCRIPT = os.path.abspath(rpg.localize_filename("../script_fixtures/descent_rpg/master_script.rst", LANGUAGE))
OUTPUT_DIR = os.path.join("output_descent", LANGUAGE)
RST2PDF_CONF_FILE = "./rst2pdf.conf"
EXTRA_ARGS_FOR_MASTER_SCRIPT = "--stylesheets=simple_tight"
EXTRA_ARGS_FOR_PLAYER_SHEETS = "--stylesheets=simple_large,dark_background"

jinja_env = rpg.load_jinja_environment(TEMPLATES_ROOT, use_macro_tags=True, language=LANGUAGE)


def generate_player_sheets():
    all_data = rpg.load_localized_yaml_file(YAML_FILE, LANGUAGE)
    data = all_data["descent_rpg"]

    for player_id, player_data in data["players"].items():
        context = {}
        context.update(player_data)
        context.update(dict(common_equipments=data["common_equipments"]))

        assert isinstance(player_data, dict)
        template = jinja_env.get_template(rpg.localize_filename('player_sheet_template.rst', LANGUAGE))
        rst_content = template.render(context)

        output_basename = "player_sheet_%s" % player_id

        print("Generating player file %s" % output_basename)

        filepath_base = os.path.join(OUTPUT_DIR, output_basename)
        rpg.convert_rst_content_to_pdf(filepath_base,
                                       rst_content=rst_content,
                                       conf_file=RST2PDF_CONF_FILE,
                                       extra_args=EXTRA_ARGS_FOR_PLAYER_SHEETS,
                                       language=LANGUAGE)


def generate_master_script():
    output_basename = "chrysalis_descent_master_script"
    print("Generating master file %s" % output_basename)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    pdf_file = os.path.join(OUTPUT_DIR, output_basename + ".pdf")

    rpg.convert_rst_file_to_pdf(MASTER_SCRIPT,
                                pdf_file,
                                conf_file=RST2PDF_CONF_FILE,
                                extra_args=EXTRA_ARGS_FOR_MASTER_SCRIPT)


if __name__ == "__main__":
    generate_player_sheets()
    generate_master_script()
    print("Script Over")
