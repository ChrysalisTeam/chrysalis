# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import functools
import jinja2
import os
import re
import sys
import textwrap
import yaml
from jinja2 import nodes, lexer, contextfilter, Template
from jinja2.ext import Extension
from jinja2.runtime import Context
from markupsafe import Markup


##################################
#  LOAD AND WRIT YAML/RST FILES  #
##################################


def load_yaml_file(yaml_file):
    with open(yaml_file, "r", encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


def load_rst_file(rst_file):
    with open(rst_file, "r", encoding="utf8") as f:
        data = f.read()
        return data


def write_rst_file(rst_file, data):
    """
    Also converts [BR] to pdf spacings, on the fly.
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


def load_jinja_environment(templates_root: list, use_macro_tags: bool):
    # IMPORTANT - we refuse undefined template vars: exceptions get raised instead
    jinja_env = jinja2.Environment(undefined=jinja2.StrictUndefined,
                                   loader=jinja2.FileSystemLoader(templates_root),
                                   trim_blocks=False,
                                   lstrip_blocks=False,
                                   extensions=[StoryChecksExtension])

    @contextfilter
    def dangerous_render(context, value):
        return render_with_jinja_and_fact_tags(content=value, jinja_env=jinja_env, jinja_context=context)

    jinja_env.filters['dangerous_render'] = dangerous_render

    if use_macro_tags:
        # requires https://github.com/frascoweb/jinja-macro-tags
        from jinja_macro_tags import configure_environment
        configure_environment(jinja_env)

        # we do similarly to jinja_env.macros.register_from_environment(), but for RST files!
        try:
            templates = jinja_env.macros.environment.list_templates(extensions=("rst",))
        except TypeError:
            pass
        for tpl in templates:
            #print("jinja_env.macros.register_from_template -->", tpl)
            jinja_env.macros.register_from_template(tpl)

    return jinja_env


def render_with_jinja_and_fact_tags(content, jinja_env, jinja_context):
    """
    Renders content and analyses/removes the {% fact %} markers from output.
    """
    assert isinstance(jinja_context, (dict, Context)), type(jinja_context)
    #print("<<<RENDERING CONTENT>>>\n %s" % content[:1000].encode("ascii", "ignore"))
    template = jinja_env.from_string(content)
    output_tagged = template.render(jinja_context)
    output = jinja_env.extract_facts(output_tagged)  # must exist
    return output


MARKER_FORMAT = r'{#>%(fact_name)s|%(as_what)s|%(player_id)s|%(is_cheat_sheet)s<#}'
MARKER_REGEX = r'\{#>(?P<fact_name>.*?)\|(?P<as_what>.*?)\|(?P<player_id>.*?)\|(?P<is_cheat_sheet>.*?)<#\}'


class StoryChecksExtension(Extension):
    """
    With this extension, used via render_with_jinja_and_fact_tags(), coherence of
    the script can be checked. Some duplicates might be found in registries, because jinja
    templates are loaded multiple times (when importing macros, especially).

    The tag {% fact "my_fact_description" [as "author"] %} gathers facts and their authors,
    and exposes the resulting data in jinja_env.facts_registry.

    Similarly, a tag {% symbol "value" for "name" %} ensures unicity of a value amongst
    different text files, and encountered values are exposed in jinja_env.symbols_registry.

    Last but not least, a tag {% hint "letter_from_x" is [needed/provided] %} exposes values in
    jinja_env.hints_registry, to check that hints required to solve enigmas are well listed in
    gamemaster checklists.
    """
    # a set of names that trigger the extension.
    tags = set(['fact', 'symbol', 'hint'])

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
            extract_facts=functools.partial(extract_facts, facts_registry=self.facts_registry)
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

        player_id = context.get("current_player_id", "<master>")
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
        symbols_list = self.symbols_registry.setdefault(symbol_name, set())
        symbols_list.add(symbol_value)
        return symbol_value  # output the symbol itself

    def _hint_processing(self, hint_name, hint_status, context):
        hint_statuses = self.hints_registry.setdefault(hint_name, set())
        hint_statuses.add(hint_status)
        return ""  # empty output


def extract_facts(source, facts_registry):
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

    extra_args = extra_args or ""

    vars = dict(rst_file=rst_file,
                pdf_file=pdf_file,
                conf_file=conf_file,
                extra_args=extra_args)

    # fit-background-mode=scale doesn't work in config file, at the moment...
    # other options: --very-verbose --show-frame-boundary or just "-v"
    command = r'''python -m rst2pdf.createpdf "%(rst_file)s" -o "%(pdf_file)s" --config=%(conf_file)s --fit-background-mode=scale --first-page-on-right --smart-quotes=2 --break-side=any  -e dotted_toc --fit-literal-mode=shrink %(extra_args)s''' % vars

    #print("Current directory: %s" % os.getcwd())
    print("Executing command: %s" % command)

    res = os.system(command)

    assert res == 0, "Error when calling rst2pdf"


def convert_rst_content_to_pdf(filepath_base, rst_content, conf_file="", extra_args=""):
    """
    We use an intermediate RST file, both for simplicity and debugging.
    """
    rst_file = filepath_base + ".rst"
    pdf_file = filepath_base + ".pdf"

    write_rst_file(rst_file, data=rst_content)
    convert_rst_file_to_pdf(rst_file, pdf_file, conf_file=conf_file, extra_args=extra_args)
