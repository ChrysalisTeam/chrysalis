# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import logging

import argparse
import functools
import jinja2
import os
import re
import shlex
import subprocess
import sys
import textwrap
import yaml
from jinja2 import nodes, lexer, pass_context, Template
from jinja2.ext import Extension
from jinja2.runtime import Context
from markupsafe import Markup


##################################
#      LANGUAGE MANAGEMENT       #
##################################

SUPPORTED_LANGUAGES = ("fr", "en")
DEFAULT_LANGUAGE = "fr"

LANGUAGE_SUFFIX_REGEX = r"_(%s)\.\w+$" % "|".join(SUPPORTED_LANGUAGES)


def enter_docs_folder():
    """
    Paths of build scripts (fixtures, stylesheets, outputs...) are relative to this "docs/" folder.
    """
    os.chdir(os.path.dirname(os.path.abspath(__file__)))


def parse_build_arguments(with_clues_option=False):
    """
    Read the options of the build script command line.

    Under pytest, which has its own command line, options are read from the CHRYSALIS_LANG
    and CHRYSALIS_WITH_CLUES (set to "1") environment variables instead.
    """
    parser = argparse.ArgumentParser(
        description="Generate the RST and PDF documents of a game, from French script fixtures (unsuffixed or '_fr' "
                    "files) or English ones ('_en' files), into the 'output_<game>/<language>/' folder.")
    parser.add_argument("--lang", choices=SUPPORTED_LANGUAGES, default=DEFAULT_LANGUAGE,
                        help="Language of the script fixtures to use, and of the generated documents")
    if with_clues_option:
        parser.add_argument("--with-clues", action="store_true",
                            help="Also export the ingame clues ODT document into one PDF per clue (slow, requires LibreOffice)")
    if "pytest" in sys.modules:
        argv = ["--lang", os.environ.get("CHRYSALIS_LANG", DEFAULT_LANGUAGE)]
        if with_clues_option and os.environ.get("CHRYSALIS_WITH_CLUES") == "1":
            argv.append("--with-clues")
        return parser.parse_args(argv)
    return parser.parse_args()


def localize_filename(filename, language):
    """
    Turn "path/to/template.rst" into "path/to/template_<language>.rst", like script fixtures are named.
    """
    assert language in SUPPORTED_LANGUAGES, language
    assert not re.search(LANGUAGE_SUFFIX_REGEX, filename), filename  # must be a language-agnostic name
    base, ext = os.path.splitext(filename)
    return "%s_%s%s" % (base, language, ext)


def localize_source_filename(filename, language):
    """
    Some French sources (YAML loaded by the Pychronia game, ODT clues...) keep their unsuffixed name,
    while their translations are named "<name>_<language>.<ext>".
    """
    return filename if language == DEFAULT_LANGUAGE else localize_filename(filename, language)


def rebase_relative_image_paths(rst_content, extra_levels=1):
    """
    Image paths in RST are relative to the generated RST file, so when these files are
    output in a deeper folder (eg. a language subfolder), upward paths must climb more levels.
    """
    regex = r"^(\s*\.\.\s+(?:\|[^|]+\|\s+)?(?:image|figure)::\s+)(?=\.\./)"
    return re.sub(regex, lambda m: m.group(1) + "../" * extra_levels, rst_content, flags=re.MULTILINE)


##################################
#  LOAD AND WRIT YAML/RST FILES  #
##################################


def load_yaml_file(yaml_file):
    with open(yaml_file, "r", encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


JINJA_STRING_LITERAL_REGEX = r"""(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')"""
SYMBOL_TAG_REGEX = r"""\{%%\s*symbol\s+(?P<value>%s)\s+for\s+%s\s*%%\}""" % ((JINJA_STRING_LITERAL_REGEX,) * 2)


def _unescape_jinja_string_literal(literal):
    return literal[1:-1].encode("ascii", "backslashreplace").decode("unicode-escape")  # like jinja2.lexer


def force_resolve_symbol_tags(data):
    """
    Replace {% symbol "value" for "name" %} tags by their value, recursively, without registering them.
    """
    if isinstance(data, str):
        data = re.sub(SYMBOL_TAG_REGEX, lambda m: _unescape_jinja_string_literal(m.group("value")), data)
        assert not re.search(r"\{%[-+]?\s*symbol\b", data), data  # unsupported symbol tag syntax
        return data
    if isinstance(data, dict):
        return {k: force_resolve_symbol_tags(v) for (k, v) in data.items()}
    if isinstance(data, (list, tuple)):
        return type(data)(force_resolve_symbol_tags(v) for v in data)
    return data


def load_localized_yaml_file(yaml_file, language):
    """
    Load "<name>_<language>.yaml" if it exists, else the untranslated (French) "<name>.yaml".

    In the latter case, symbol tags are resolved without registration, since their
    values would clash with those of translated templates.
    """
    localized_yaml_file = localize_source_filename(yaml_file, language)
    if os.path.exists(localized_yaml_file):
        return load_yaml_file(localized_yaml_file)
    print("!!! No translated %s found, using untranslated data" % localized_yaml_file)
    return force_resolve_symbol_tags(load_yaml_file(yaml_file))


def load_rst_file(rst_file):
    with open(rst_file, "r", encoding="utf8") as f:
        data = f.read()
        return data


def write_rst_file(rst_file, data, language=DEFAULT_LANGUAGE):
    """
    Also converts [BR] to pdf spacings, on the fly.

    Image paths of templates are relative to "output_xxx/", but RST files are written into "output_xxx/<language>/".
    """

    if isinstance(data, (tuple, list)):
        full_rst = "\n\n".join(data)
    else:
        assert isinstance(data, str), type(data)
        full_rst = data

    full_rst = full_rst.replace("[BR]",  # for stuffs coming from yaml fixtures
                                textwrap.dedent("""

                                        .. raw:: pdf

                                           Spacer 0 15

                                           """))

    full_rst = rebase_relative_image_paths(full_rst)

    # BOMs of included templates break RST headings and inline markup in recent rst2pdf versions
    full_rst = full_rst.replace("\ufeff", "")

    if language == "fr":
        # basic fixing of orphan punctuation marks for FR language...
        full_rst = (full_rst.replace(" !", u"\u00A0!")
                    .replace(" ?", u"\u00A0?")
                    .replace(" :\n", u"\u00A0:\n"))  # beware about RST directives here...

    # autocreate missing folders
    folder = os.path.dirname(rst_file)
    assert folder  # else, naked file basename, it's not good
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(rst_file, "w", encoding="utf8") as f:
        f.write(full_rst)


####################################
#     PROCESS DATA WITH JINJA2     #
####################################


def load_jinja_environment(templates_root: list, use_macro_tags: bool, language: str):
    # IMPORTANT - we refuse undefined template vars: exceptions get raised instead
    jinja_env = jinja2.Environment(undefined=jinja2.StrictUndefined,
                                   loader=jinja2.FileSystemLoader(templates_root),
                                   trim_blocks=False,
                                   lstrip_blocks=False,
                                   extensions=[StoryChecksExtension])

    @pass_context
    def dangerous_render(context, value):
        return render_with_jinja_and_fact_tags(content=value, jinja_env=jinja_env, jinja_context=context)

    jinja_env.filters['dangerous_render'] = dangerous_render

    if use_macro_tags:
        # requires https://github.com/frascoweb/jinja-macro-tags
        from jinja_macro_tags import configure_environment
        configure_environment(jinja_env)

        # we do similarly to jinja_env.macros.register_from_environment(), but for RST files!
        templates = jinja_env.macros.environment.list_templates(extensions=("rst",))
        for tpl in templates:
            match = re.search(LANGUAGE_SUFFIX_REGEX, tpl)
            if match and match.group(1) != language:
                continue  # translations of a template declare the same macro names
            #print("jinja_env.macros.register_from_template -->", tpl)
            jinja_env.macros.register_from_template(tpl)

    return jinja_env


def render_with_jinja_and_fact_tags(content, jinja_env, jinja_context):
    """
    Renders content and analyses/removes the {% fact %} markers from output.
    """
    assert isinstance(jinja_context, (dict, Context)), type(jinja_context)
    assert isinstance(content, (str, bytes)), repr(content)
    #print("<<<RENDERING CONTENT>>>\n %s" % content[:1000].encode("ascii", "ignore"))
    template = jinja_env.from_string(content)
    output_tagged = template.render(jinja_context)
    output = jinja_env.extract_facts_from_intermediate_markup(output_tagged)  # must exist
    return output


MARKER_FORMAT = r'{#>%(fact_name)s|%(as_what)s|%(player_id)s|%(is_cheat_sheet)s<#}'
MARKER_REGEX = r'\{#>(?P<fact_name>.*?)\|(?P<as_what>.*?)\|(?P<player_id>.*?)\|(?P<is_cheat_sheet>.*?)<#\}'


class StoryChecksExtension(Extension):
    """
    With this extension, used via render_with_jinja_and_fact_tags(), coherence of
    the script can be checked. Some duplicates might be found in registries, because jinja
    templates are loaded multiple times (when importing macros, especially).

    The tag {% fact "my_fact_description" [as author] %} gathers facts and their authors,
    and exposes the resulting data in jinja_env.facts_registry.

    Similarly, a tag {% symbol "value" for "name" %} ensures unicity of a value amongst
    different text files, and encountered values are exposed in jinja_env.symbols_registry.
    Rendering with a False "register_symbols" context variable outputs values without registering them.

    Last but not least, a tag {% hint "letter_from_x" is [needed/provided] %} exposes values in
    jinja_env.hints_registry, to check that hints required to solve enigmas are well listed in
    gamemaster checklists.
    """
    # a set of names that trigger the extension.
    tags = set(['fact', 'symbol', 'hint'])

    # facts rendered without "current_player_id" in context, i.e. those of the ingame clues document
    UNKNOWN_PLAYER_NAME = "ingame_clues"

    def __init__(self, environment):
        super(StoryChecksExtension, self).__init__(environment)

        self.facts_registry = {}
        self.symbols_registry = {}
        self.hints_registry = {}

        ## add registries to the environment
        environment.extend(
            facts_registry=self.facts_registry,  # (fact_name -> fact_data_dict) mapping
            symbols_registry=self.symbols_registry,  # (symbol_name -> symbol_values_set) mapping
            hints_registry=self.hints_registry,  # (hint_name -> hint_statuses_set) mapping
            extract_facts_from_intermediate_markup=functools.partial(extract_facts_from_intermediate_markup, facts_registry=self.facts_registry)
        )

    def parse(self, parser):

        template_name = parser.name
        #character_name = template_name.split("_")[0]

        # the first token is the token that started the tag.
        # We get the line number so that we can give
        # that line number to the nodes we create by hand.
        tag_name = next(parser.stream)  # gives a Token(lineno, type, value)
        lineno = tag_name.lineno
        context = nodes.ContextReference()

        if tag_name.value == 'fact':

            # now we parse a single expression
            fact_name = parser.parse_primary()

            token = parser.stream.current

            as_what_value = None
            if token.test('name:as'):
                next(parser.stream)
                as_what_value = parser.stream.expect(lexer.TOKEN_NAME).value  # eg "author"
            as_what = nodes.Const(as_what_value)

            #if "mytest" in fact_name.value:
            #    print(">> ENCOUNTERED FACT", fact_name.value, as_what.value, lineno, "in", parser.name)
            """
            # if there is a comma, the user provided a timeout.  If not use
            # None as second parameter.
            if parser.stream.skip_if('comma'):
                args.append(parser.parse_expression())
            else:
                args.append(nodes.Const(None))
    
            # now we parse the body of the cache block up to `endcache` and
            # drop the needle (which would always be `endcache` in that case)
            body = parser.parse_statements(['name:endcache'], drop_needle=True)
    
            # now return a `CallBlock` node that calls our _cache_support
            # helper method on this extension.
            return nodes.CallBlock(self.call_method('_cache_support', args),
                                   [], [], body).set_lineno(lineno)
            """

            #if parser.name:
            # IMPORTANT: we're not rendering from a string but from a template file,
            # so we assume we're in a macro import, so we DO NOT execute the Fact Tag!
            #return nodes.Output([])  # no output

            call = self.call_method('_fact_processing', [fact_name, as_what, context], [], lineno=lineno)

        elif tag_name.value == 'symbol':

            symbol_value = parser.parse_primary()

            for_token = parser.stream.expect('name:for').value
            #token = parser.stream.current
            #if not token.test('name:for'):
            #    raise

            symbol_name = parser.parse_primary()

            call = self.call_method('_symbol_processing', [symbol_name, symbol_value, context], [], lineno=lineno)

        else:

            assert tag_name.value == 'hint'

            hint_name = parser.parse_primary()

            is_token = parser.stream.expect('name:is').value

            hint_status_value = parser.stream.expect(lexer.TOKEN_NAME).value  # eg. "needed" or "provided"
            hint_status = nodes.Const(hint_status_value)

            call = self.call_method('_hint_processing', [hint_name, hint_status, context], [], lineno=lineno)

        return nodes.Output([call], lineno=lineno)  # or nodes.CallBlock

    def _fact_processing(self, fact_name, as_what, context):

        player_id = context.get("current_player_id", self.UNKNOWN_PLAYER_NAME)
        is_cheat_sheet = context.get("is_cheat_sheet", False)

        #if "mytest" in fact_name:
        #    print(">> >> PROCESSING FACT", fact_name, as_what, player_id)
        #    import traceback
        #    traceback.print_stack()

        if player_id is None:
            return ""  # we abort registration of fact

        as_what = as_what or "viewer"  # default status
        marker = MARKER_FORMAT % dict(fact_name=fact_name, as_what=as_what,
                                      player_id=player_id, is_cheat_sheet=int(is_cheat_sheet))
        return marker  # special marker for final extraction

    def _symbol_processing(self, symbol_name, symbol_value, context):
        assert symbol_name, (symbol_name, symbol_value)
        if context.get("register_symbols", True):
            symbols_list = self.symbols_registry.setdefault(symbol_name, set())
            symbols_list.add(symbol_value)
        return symbol_value  # output the symbol itself

    def _hint_processing(self, hint_name, hint_status, context):
        hint_statuses = self.hints_registry.setdefault(hint_name, set())
        hint_statuses.add(hint_status)
        return ""  # empty output


def extract_facts_from_intermediate_markup(source, facts_registry):
    """
    Browse a transformed output, and extract facts from the special markup left in it by StoryChecksExtension.
    """

    def process_fact(matchobj):

        fact_name = matchobj.group("fact_name")
        as_what = matchobj.group("as_what")
        player_id = matchobj.group("player_id")
        is_cheat_sheet = int(matchobj.group("is_cheat_sheet"))

        if as_what not in ("author", "viewer"):
            raise RuntimeError("Abnormal fact status: %r in %r" % (as_what, matchobj.group(0)))
        is_author = (as_what == "author")

        fact_params = facts_registry.setdefault(fact_name, {})
        player_params = fact_params.setdefault(player_id, {})

        if player_params:
            assert player_params['is_author'] == is_author, (fact_name, player_id)
        player_params['is_author'] = player_params.get('is_author') or is_author

        player_params['in_cheat_sheet'] = player_params.get('in_cheat_sheet') or is_cheat_sheet
        player_params['in_normal_sheet'] = player_params.get('in_normal_sheet') or not is_cheat_sheet

        return ""  # REMOVE OUTPUT

    cleaned_source = re.sub(MARKER_REGEX, process_fact, source, flags=0)
    return cleaned_source


def _display_and_check_story_hints(jinja_env):
    from pprint import pprint

    print("\nInline hints of scenario:")
    pprint(jinja_env.hints_registry)

    has_coherence_errors = False
    hints_registry_good_value = set(['needed', 'provided'])
    for k, v in sorted(jinja_env.hints_registry.items()):
        assert v <= hints_registry_good_value, (k, v)  # no weird values
        if 'needed' in v and 'provided' not in v:
            print("!!!!! ERROR IN hints registry for key", repr(k), ':', v, 'requires a provided hint')
            has_coherence_errors = True
        if 'provided' in v and 'needed' not in v:
            print("!!!!! WARNING IN hints registry for key", repr(k), ':', v, 'normally requires a needed hint')
            # It's not a blocking coherence error, do don't set has_coherence_errors here

    return has_coherence_errors

def _display_and_check_story_symbols(jinja_env):
    from pprint import pprint

    print("\nInline symbols of scenario:")
    pprint(jinja_env.symbols_registry)

    has_coherence_errors = False
    for k, v in jinja_env.symbols_registry.items():
        unique_values = set(x.strip().lower().replace("\n", "") for x in v)
        if len(unique_values) != 1:
            print("!!!!! ERROR IN symbols registry for key", k, ':', v)
            has_coherence_errors = True
    return has_coherence_errors


def _display_and_check_story_facts(jinja_env, masked_user_names):
    from pprint import pprint
    assert isinstance(masked_user_names, (set, tuple, list)), repr(masked_user_names)

    facts_registry_stripped = [(k, sorted(v)) for (k, v) in jinja_env.facts_registry.items()]

    print("\nInline facts of scenario:")
    pprint(facts_registry_stripped)

    '''
    def __UNUSED_replace_all_players_set(names):
        """When all real players know a fact, replace their names by a symbol"""
        names_set = set(names)
        if all_player_names <= names_set:
            new_set = (names_set - all_player_names) | {"ALL-PLAYERS"}
        else:
            new_set = names_set
        return new_set
    '''

    has_coherence_errors = False

    def _check_fact_leaf(fact_name, player_id, fact_node):
        """Ensure that the knowledge of a single player over a single fact is coherent"""
        assert fact_node["in_normal_sheet"] or fact_node["in_cheat_sheet"], fact_node
        _has_coherence_errors = False
        if fact_node["in_cheat_sheet"]:
            if not fact_node["in_normal_sheet"]:  # all facts must be explained in normal sheets
                print("!!!!! ERROR IN fact leaf for key", fact_name, ':', player_id, fact_node)
                _has_coherence_errors = True
        return _has_coherence_errors

    facts_items = sorted(jinja_env.facts_registry.items())

    for (fact_name, fact_data) in facts_items:
        for player_id, fact_node in fact_data.items():
            has_coherence_errors = _check_fact_leaf(fact_name, player_id=player_id, fact_node=fact_node) or has_coherence_errors

    facts_summary = [(fact_name,  #.replace("_", " "),
                      sorted((x, y) for (x, y) in fact_data.items()
                             if y["is_author"] and x not in masked_user_names),
                      sorted((x, y) for (x, y) in fact_data.items()
                             if not y["is_author"] and x not in masked_user_names))
                     for (fact_name, fact_data) in facts_items]

    return has_coherence_errors, facts_summary


def display_and_check_story_tags(jinja_env, masked_user_names):

    has_coherence_errors1, facts_summary = _display_and_check_story_facts(jinja_env, masked_user_names=masked_user_names)
    has_coherence_errors2 = _display_and_check_story_symbols(jinja_env)
    has_coherence_errors3 = _display_and_check_story_hints(jinja_env)

    has_any_coherence_error = has_coherence_errors1 or has_coherence_errors2 or has_coherence_errors3

    return has_any_coherence_error, facts_summary




####################################
#      CONVERT MARKUP TO PDF       #
####################################

def convert_rst_file_to_pdf(rst_file, pdf_file, conf_file="", extra_args=""):
    """
    Use rst2pdf executable to convert rst file to pdf.

    IMPORTANT : you can output default styles with "rst2pdf --print-stylesheet"
    """

    conf_file = conf_file or ""
    assert not conf_file or os.path.exists(conf_file), conf_file  # must be in CWD

    # fit-background-mode=scale doesn't work in config file, at the moment...
    # other options: --very-verbose --show-frame-boundary or just "-v"
    command = [sys.executable, "-m", "rst2pdf.createpdf", rst_file, "-o", pdf_file, "--config=%s" % conf_file,
               "--fit-background-mode=scale", "--first-page-on-right", "--smart-quotes=2", "--break-side=any",
               "-e", "dotted_toc_compat", "--fit-literal-mode=shrink"] + shlex.split(extra_args or "")

    logging.debug("Executing command: %s" % command)

    # rst2pdf exits with code 0 even when it logs errors (eg. missing images), so we check its logs too
    res = subprocess.run(command, stderr=subprocess.PIPE, encoding="utf8", errors="replace")
    sys.stderr.write(res.stderr)
    if res.returncode:
        raise RuntimeError("Error %s when calling rst2pdf on %s" % (res.returncode, rst_file))
    error_lines = [line for line in res.stderr.splitlines() if "[ERROR]" in line]
    if error_lines:
        raise RuntimeError("rst2pdf reported errors on %s:\n%s" % (rst_file, "\n".join(error_lines)))


def convert_rst_content_to_pdf(filepath_base, rst_content, conf_file="", extra_args="", language=DEFAULT_LANGUAGE):
    """
    We use an intermediate RST file, both for simplicity and debugging.
    """
    rst_file = filepath_base + ".rst"
    pdf_file = filepath_base + ".pdf"

    write_rst_file(rst_file, data=rst_content, language=language)
    convert_rst_file_to_pdf(rst_file, pdf_file, conf_file=conf_file, extra_args=extra_args)
