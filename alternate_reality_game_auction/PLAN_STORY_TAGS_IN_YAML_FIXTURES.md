# Story tags (fact/symbol/item) in Pychronia YAML fixtures

Status: plan only, not implemented yet (2026-11-28). Until it is, don't put story tags in the YAML fixtures: they
would show up raw in the portal.

## Context

You want to put storygen story tags (`{% fact %}`, `{% symbol %}`, `{% item %}` and their `x*` variants) in the
Pychronia YAML fixtures of `Chrysalis/alternate_reality_game_auction/scenario_fixtures/`. The goal is for storygen
to check them against the rst/txt sheets, while portal instances only show clean text.

**Today this isn't possible:**
- **Pychronia shows the tags raw.** `utilities.load_yaml_fixture()` (`pychronia_game/utilities/__init__.py:833`)
  stores the parsed strings in ZODB unchanged, at instance creation (`datamanager_core.py:185`). Docutils then prints
  `{% fact "x" %}` literally. House-report `surveillance_analysis` is rendered by Django `Template()`, where an
  unknown `fact` tag raises `TemplateSyntaxError`.
- **Storygen never processes tags in YAML.** `data_files` values are inserted as plain values (see the comment in
  `scenario_fixtures/configuration.yaml`). The only tag-aware path is the `dangerous_render` filter, which renders the
  whole string as jinja. That fails on the Django syntax already in the fixtures (`{{ official_title }}`,
  `{{character_properties…}}`), since the env uses `StrictUndefined`.

**Approach:** both tools match only the story tags with a regex and never render the whole string.
- Storygen renders each matched tag on its own through the existing `StoryChecksExtension`, so the registries and the
  coherence analysis come for free.
- Pychronia replaces each tag with what storygen would output: the first argument, or nothing for `x*` tags.

Decisions taken: only YAML is added (rst/txt sheets already support tags). YAML facts count for `<master>` by default
(same as ODT documents), and each scanned-files entry can override `current_player_id`.

## Allowed tag syntax in YAML

The tags are literal-only: the first argument (and the `for` argument) must be a quoted string, not an expression.
```
{% fact "name" [as author|viewer] %}   {% symbol "value" for "name" %}   {% item "name" is needed|provided %}
```
plus `xfact` / `xsymbol` / `xitem` and jinja's `{%-` / `-%}` whitespace control.

Both tools fail loudly on any `{% fact|symbol|item…` left over after matching (non-literal or malformed tag). The
error names the file and the key path, so a typo can't reach the portal.

YAML authoring rules, to add to the README:
- Write tags inside block scalars (`|`). A plain scalar can't start with `{`.
- Inside double-quoted scalars, use single quotes for the tag arguments.

## 1. Pychronia: strip the tags when loading fixtures

File: `pychronia_game/utilities/__init__.py`
- Add `STORY_TAG_REGEX` and `STORY_TAG_LEFTOVER_REGEX`.
- Add `strip_story_tags(text)`. It replaces each tag with its first argument (`symbol` → the value; `fact`/`item` →
  the name, with newlines removed like `StoryChecksExtension._normalize_title_string(normalize_case=False)`) or with
  `""` for `x*` tags. It honours `-` whitespace trimming, and raises `ValueError` on leftovers.
- Add `strip_story_tags_from_tree(data, source)`. It walks dicts and lists, rewrites string values (not keys), and
  adds the file and key path to errors.
- In `load_yaml_fixture()`, apply it to each `part` right after `load_yaml_file(yaml_file)` (line 873).
  `load_yaml_file()` itself stays unchanged, so savegame backups are untouched.
- Pychronia keeps no dependency on pychronia_storygen. The prod server doesn't install it, so the ~25 lines of regex
  are duplicated on purpose, and both repos test the same cases.

Tests: `pychronia_game/tests/test_game.py`, next to `test_load_yaml_fixture` (~l.766–812, same tmp_dir pattern):
- each tag form, `x*` variants, quote styles and `{%- -%}`;
- Django `{{ … }}` and `{% other %}` syntax left intact;
- a leftover/malformed tag raises an error naming the file.

## 2. pychronia-storygen: scan YAML fixtures and strip in templates

Repo: `P:\Workspace\Pychronia-storygen`

`src/pychronia_storygen/story_tags.py`
- Add the same `STORY_TAG_REGEX` / leftover regex and `strip_story_tags(text)`.
- Add `scan_story_tags_in_data(data, *, jinja_env, jinja_context, source)`. It walks the tree and runs
  `render_with_jinja_and_fact_tags(content=<matched tag>, …)` on each match, which fills
  `facts/symbols/items_registry`. Leftovers raise `StorygenConfigError` with the file and key path.

`src/pychronia_storygen/cli.py`
- Add a config section `story_tag_scanning`: a list of `{"files": [glob patterns with {lang} placeholders],
  "current_player_id": optional}`.
- Process it in `build()` after documents and before `_generate_summary_files()`.
- Model it on `_generate_document_files`: analysis only, skipped when `selection.listing`.
- Load files with `document_formats.load_yaml_file`, expand paths with `expand_path_placeholders`, and fail if a
  pattern matches nothing.
- The jinja context gets `current_player_id` only when it is configured, so the extension defaults to `<master>`.

`src/pychronia_storygen/document_formats.py` (`load_jinja_environment`)
- Register a `strip_story_tags` jinja filter. Templates that print YAML values (e.g. the gamemaster manual) can then
  output clean text without rendering the Django syntax: `{{ manual.x.y|strip_story_tags }}`.

Also:
- `README.rst`: document the section, the filter, the literal-only rule and the YAML quoting rules (§ "Story tags and
  coherence analysis").
- Tests in `tests/`: scanning registers facts/symbols/items and leaves Django syntax alone; a symbol conflict between
  a YAML file and a template is reported; leftover-tag errors; `current_player_id` override; the filter.

## 3. Chrysalis: turn it on for the auction game

`alternate_reality_game_auction/scenario_fixtures/configuration.yaml`
- Add a scan section that mirrors the files Pychronia loads (see `config/settings/game.py` ~l.100–136):
  ```yaml
  "story_tag_scanning":
    - "files": ["*_{lang}.yaml", "global_data.yaml", "messaging/*_{lang}.yaml", "encyclopedia/*_{lang}.yaml"]
  ```
  `configuration.yaml` itself must not match.
- Update the header comment: YAML texts may now contain story tags.
- If the manual is to contain tags, add `|strip_story_tags` in `storygen/manual_*.txt`.
- Bump the storygen dependency (`requirements.txt` → git URL) once storygen is pushed.

## Verification

1. Pychronia: `uv run pytest pychronia_game/tests/test_game.py -k "yaml or story_tag"`, then the full suite.
2. Storygen: `poetry run pytest` in `Pychronia-storygen`.
3. End to end:
   - Add a test `{% symbol 'X' for 'probe' %}` to one auction messaging YAML and a conflicting value elsewhere.
     `python make.py build alternate_reality_game_auction --lang en` must exit 1 with "Game symbol 'probe' has several
     different values".
   - Fix the conflict: the build passes.
   - Create or reset a local game instance (dev server from `tests/manage.py`) and check that the message shows `X`,
     not the raw tag.
   - Revert the probe.
