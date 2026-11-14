# Migration of Chrysalis PDF builds to Pychronia-storygen

Goal: replace `build_archives_pdfs.py`, `build_auction_pdfs.py`, `build_descent_pdfs.py` and
`build_mindstorm_pdfs.py` (plus their helpers `rpg_sheet_generator.py` and `mysteryparty_common_utils.py`)
with Pychronia-storygen projects, as is already the case for `mysteryparty_cromlech/scenario_fixtures`.
Also build the scenarios of `rpg_sentience` and `rpg_skeletons` (plain RST to PDF) with storygen.


## Decisions

- **Output names**: conform to storygen standards (`<group folders>/<sheet>_full_sheet.pdf`,
  `<sheet>_cheat_sheet.pdf`, ODT clues in a folder named after the ODT). An `output_name` option
  will only be added later, if it proves REALLY necessary. Nothing in Chrysalis or Pychronia
  consumes the current output names (the downloadable zips of the website are built by hand;
  only `Readme.rst` and the disabled email-sending code mention them).
- **Python hook**: allowed, declared in the project configuration as `"<module>.<function>"`.
- **Theme**: keep the shared rst2pdf theme (`docs/assets/*.yaml` stylesheets and images,
  `Chrysalis/fonts/`) for now; see "Shared theme" for the adjustments it needs. Background-dependent
  stylesheets get temporary storygen copies until the old scripts are deleted.
- **Descent location** (G11): the storygen project is `rpg_descent/` itself (one level above
  `scenario_fixtures/`, which Pychronia loads as a whole), so no `--config` option is needed.
- **Checklists**: the hook computes `murder_party_items` and the per-crate structure as today, templates
  unchanged; converting to storygen inventories can come later.
- **ODT tags**: renamed by a script editing the ODTs' `content.xml`, then checked by re-extracting their text;
  no `hint` alias in storygen.
- **French sources without suffix** (`ingame_clues_<game>.odt`, `gamemaster_assets_checklist.yaml`):
  renamed with `_fr`.
- **`rpg_skeletons/scenario_fixtures/*.pdf`**: left as they are, out of scope.


## Current state

| Build | Size | Fit with storygen | Blockers |
|---|---|---|---|
| `rpg_sentience` | 1 plain RST per language | Almost ready | mandatory config sections |
| `rpg_skeletons` | 1 French RST in `Chrysalis Skeletons scenario 03.txt` | Almost ready | file renaming, mandatory config sections |
| Descent | 63 lines | Easy | data file as variables, player data spread at template root, config location (see G11) |
| Auction | 83 lines | Easy | data file, section-joining template, unlinking of unknown RST targets |
| Archives | 626 lines | Medium | everything below |
| Mindstorm | 606 lines | Hardest | everything below, plus computed variables, custom filter and special documents |

No RST source of sentience, skeletons or the Descent master script contains `{{`, `{%` or `{#`,
so rendering them through jinja2 is safe.


## Gaps in storygen

### G1 - Optional configuration sections

`cli.py` indexes `project_data_tree["sheet_generation"]`, `["document_generation"]`, `["inventory_generation"]`
and `["summary_generation"]` directly (cli.py:317-340), each group requires a `"sheets"` key (cli.py:60),
each inventory requires its 5 keys (cli.py:135-144), and each summary its 6 keys (cli.py:189-215).
`_generate_summary_files()` also references `has_serious_errors1/2/3` / `error_messages1/2/3` even when the
matching template is not configured (cli.py:230-231, `UnboundLocalError`).
Make all sections, keys (and each summary template) optional.

### G2 - Extra template directories

Archives and Mindstorm load templates from `../mysteryparty_common/scenario_fixtures` too
(see the FIXME at cli.py:295). Add a `"template_dirs"` configuration entry, appended AFTER the project dir
(same lookup order as the build scripts: game templates first), used both by the jinja2 loader and by
macro registration (with the same language filtering; build/output exclusions only apply to the project dir).
Checked: no template path exists in both a game folder and `mysteryparty_common`, and `mysteryparty_common`
declares no macro, so no "Macro already declared" collision (jinja_macro_tags.py:115-117) is expected today.
The `.txt` scanning of storygen is harmless: these fixture folders contain no `.txt` file.

### G3 - Data files loaded as variables

Add a `"data_files"` configuration entry mapping variable names (or the root namespace) to YAML files,
for example `descent_rpg_data_{lang}.yaml`, `gamemaster_manual_{lang}.yaml` (auction),
`gamemaster_assets_checklist_{lang}.yaml` (Archives, Mindstorm),
`_initial_game_data_dump.yaml` + its English partial overlay (port `deep_merge_localized_overlay()`;
`force_resolve_symbol_tags()` needs no port: the dumps contain no symbol tag and all other data files are translated),
the private `mysteryparty_common/scenario_fixtures/local.yaml`. The latter must be allowed to be missing,
but then fall back to `local.yaml.example`: Mindstorm templates need its `telephone_exchange_number` and
`anthropia_portal_url` (`common_anthropia_account_summary_displayer_*.rst`, `miscellaneous/anthropia_portal_*.rst`),
and StrictUndefined would fail without them. Supporting a list of candidate files (first existing wins) covers it.

### G4 - `{lang}` placeholder in configuration paths

Cromlech duplicates its whole configuration per language because its sheet names are localized.
Archives and Mindstorm keep English names in both languages, so a single `configuration.yaml` with
paths like `players/garnet_role_{lang}.rst` avoids duplicating ~50 sheet entries and ~80 clue entries.
Apply it to every path-valued entry (sheet parts, `data_files`, `inventory_data`, `document_source`).
French sources without suffix (`ingame_clues_<game>.odt`, `gamemaster_assets_checklist.yaml`) must be renamed
with `_fr` (nothing else loads them), except the game data dump (base + overlay, see G3).
Translated projects must always be built with `--lang`: without it, macros of both languages are registered
and collide (document_formats.py:146-151).

### G5 - Python hook

Configuration entry `"variables_hook": "storygen_hooks.prepare_variables"`; the module is imported
from the project directory (inserted in `sys.path`, along with the `template_dirs`, so that Archives and
Mindstorm can share a helper module in `mysteryparty_common`). Called once per run, after data files are loaded,
with the root variables, the language and the jinja environment; it returns (or mutates) the variables.
Covers the residual logic of the build scripts: merging `local.yaml` character overrides and Archives
`OFFICIAL_NAMES` into `character_properties`, `full_official_title`, `spoiling_official_name`,
`use_player_photos`, Mindstorm `player_names` (+ "shark"), the checklist structures (see "Mapping"),
and the registration of the Mindstorm-only `strip_pychronia_page_markup` filter
(build_mindstorm_pdfs.py:44, used by 3 templates per language).

A per-sheet hook does NOT seem needed: the per-player Mindstorm variables (`current_player_password`,
`current_player_account`, `current_player_extra_goods`, `permissions`, `hide_anthropia_credentials`)
are only used by `common_anthropia_account_summary_displayer_{fr,en}.rst` (plus the orphan, never built
`miscellaneous/all_specific_abilities_details_*.rst`), which can read `character_properties[current_player_id]`
instead; `hide_anthropia_credentials` defaults to false, the players extracts set it with `{% with %}`.

### G6 - Port the Chrysalis ODT clue splitter

`mysteryparty_common_utils._generate_clues_pdfs_from_main_odt_document()` is more robust than storygen's
`split_odt_file_into_separate_documents()`: single LibreOffice export then pypdf split (storygen runs
LibreOffice once per clue, ~50 runs for Mindstorm), check of the total page count, check of a text snippet
on the first page of each clue, `None` entries for skipped pages, pruning of unused page resources
(else each clue embeds the images of all others), and check that gamemaster comments (story tags) were really
extracted (`comment_samples`). Extend `document_splitting` entries to `[name|null, page_count, snippet]`;
with a single configuration (G4), snippets and the comment sample must be per-language mappings
(`{fr: "...", en: "..."}`, or `null` for pages without text).

### G7 - RST and PDF conversion parity

- `rpg_sheet_generator.write_rst_file()` also replaces `" : "` by a non-breaking space in French and
  strips BOMs (98 Archives/Mindstorm templates start with one, and storygen renders each part separately,
  so they end up in the middle of the RST); storygen only handles `" :\n"`.
- Image paths `../assets/...` (relative to `docs/output_<game>/`, and `../../assets/...` for docs output in a
  `documents/` subfolder) must become `{{ project_dir }}...` paths, as in Cromlech, since rst2pdf resolves them
  relative to the RST file in `_build/<lang>/<groups>/`. 16 directives (8 per language), including
  `../../alternate_reality_game_auction/...` (Mindstorm auction program and guests gallery) and
  `../trombinoscope/...` (guests gallery), plus the decoration image appended by `build_mindstorm_pdfs.py`.
- Smart quotes: Chrysalis passes `--smart-quotes=0` and relies on `docs/docutils.conf` (`smart_quotes = yes`,
  language-aware, eg. « » in French); storygen hardcodes `--smart-quotes=2` (English rules only) and docutils
  only reads `./docutils.conf` from the CWD (the project dir) or `$DOCUTILSCONFIG`.
  Add a setting for the docutils configuration file (or let projects override the smart-quotes option).
- rst2pdf exits with code 0 on many errors (missing image or background, see "Shared theme"):
  port the stderr scan and the removal of stale/broken PDFs of `rpg_sheet_generator.convert_rst_file_to_pdf()`;
  storygen only checks the return code (document_formats.py:295-297). Needed BEFORE any comparison of outputs.

### G8 - Unlinking of unknown RST targets

Optional per-sheet setting, ported from `build_auction_pdfs.unlink_unknown_rst_targets()`, for the
truncated auction gamemaster manual (applied on the final RST, after jinja rendering).

### G9 - Per-sheet `current_player_id`

storygen always sets `current_player_id` to the sheet name, and it overrides any sheet variable of the same name
(`ChainMap.new_child(variables, **kwargs)` updates `variables` with the kwargs, cli.py:70-73).
But Chrysalis renders many documents with another id: `None` (no fact registration) for all Mindstorm
isolated docs, `"anyone"`, `"everyone"`, `"npcs"` or `"gamemaster"` for Archives ones, `master_login`
(masked from the facts summary) for both gamemaster manuals.
Make the sheet name only a default, overridable by `variables.current_player_id` (null allowed,
`_fact_processing()` already skips registration for `None`).

### G10 - Coherence check usability

- Coherence errors are only logged (cli.py:235-240), whereas the build scripts exit with code 1:
  exit non-zero when `has_serious_errors`.
- Summaries are only generated without `-t` (cli.py:262-266), and the documents step always splits the ODTs with
  LibreOffice, so every coherence check costs a full clue export; the build scripts always register the ODT tags
  but only export the clues with `--with-clues`. Allow registering document tags without splitting
  (eg. a `--skip-document-splitting` option, or splitting only with `-t documents`).

### G11 - Configuration location for Descent

Pychronia loads `rpg_descent/scenario_fixtures` as a whole fixture directory (Pychronia `common_settings.py:111,305`;
`load_yaml_fixture()` merges every `*.yaml` and `*/*.yaml` not starting with `_`), so a storygen `configuration.yaml`
there would be merged into the Mindstorm game data. Decided: the Descent storygen project is `rpg_descent/`
itself, its `configuration.yaml` referencing templates and data as `scenario_fixtures/...` (the project dir is
the jinja2 root, so no `template_dirs` is even needed); `_build/` and `_output/` then live in `rpg_descent/`.
Auction is not affected (Pychronia lists its root fixture files one by one).


## Story tag dialects (main risk)

| Chrysalis tag | storygen equivalent | Occurrences (Archives + Mindstorm, FR + EN) |
|---|---|---|
| `{% fact "x" %}` (no output) | `{% xfact "x" %}` (`fact` outputs the name) | 1438 in RST, 20 in checklist YAMLs, 44 in ODTs |
| `{% hint "x" is needed %}` (no output) | `{% xitem "x" is needed %}` | 380 in RST, 383 in checklist YAMLs, 71 in ODTs |
| `{% symbol "v" for "x" %}` | same | 940 in RST, 100 in checklist YAMLs, 46 in ODTs |
| context var `register_symbols=False` | unsupported | only for French ODT fallback, obsolete since English ODTs exist |

The 4 ODTs (`ingame_clues_{archives,mindstorm}[_en].odt`) hold tags in gamemaster comments: `hint` must be renamed
there too (else jinja2 raises an unknown tag error), which is not a text replacement: decided as a scripted edit
of `content.xml` (tags may be split across XML spans), then a re-check with the text extractor that tag counts
match the baseline. A leftover `{% fact %}` in RST/YAML
would silently print the fact name in PDFs: check with grep that none remains.

Semantic differences to watch:
- storygen strips and lowercases fact, item AND symbol names (story_tags.py:204,214,237); Chrysalis keeps them
  verbatim, so names differing only by case get merged. Both refuse a character being author and viewer
  of a fact (Chrysalis even asserts, rpg_sheet_generator.py:457-458), so merges are the only new source of such errors.
- Chrysalis normalizes symbol values with `.strip().lower().replace("\n", "")`, storygen only with `.lower()`:
  symbols extracted from ODTs may raise new false errors, so storygen's normalization should probably be aligned.
- Facts rendered without `current_player_id` are attributed to `"ingame_clues"` in Chrysalis, `"<master>"` in storygen
  (documents, and inventories/summaries, which get no `current_player_id`).
- The `gamemaster_facts_summary_{fr,en}.rst` templates use `aggregated_facts_summary` (Archives) /
  `facts_summary` (Mindstorm), with `master_login` masked; they must be rewritten for storygen's
  `facts_registry` (or replaced by storygen's summary templates).

The renaming itself is mechanical for RST/YAML; the old scripts can no longer parse the templates afterwards,
so their baseline (registries printed by `display_and_check_story_tags()`, RST outputs, PDF page counts)
must be captured BEFORE renaming.


## Mapping of build script logic

| Build script logic | Destination |
|---|---|
| `OFFICIAL_NAMES`, `DOCUMENT_TITLES`, `AVAILABLE_ANTHROPIA_ABILITIES` | YAML variables (per-language mappings or data files); `OFFICIAL_NAMES` merged into `character_properties` by the hook |
| `GAMEMASTER_MANUAL_PARTS`, `PLAYER_MANUAL_PARTS`, `ISOLATED_DOCS`, `COMMON_*` lists | `sheet_generation` groups and sheets, with `current_player_id` overrides (G9) |
| Mindstorm `GAME_TYPE` / `IS_STANDALONE` | `standalone: true` variable, parts like `players/garnet.anteauction.standalone_{lang}.rst` (storygen's language regex handles these names) |
| Mindstorm cheat sheets | `cheat_sheet` entries of player sheets (storygen sets `is_cheat_sheet` itself) |
| "shark" special player (no cheat sheet) | sheet with only a `full_sheet` |
| Player list computed from the dump (non-NPC characters) | explicit sheets in configuration; check them against the dump once |
| Title + table of contents header, trailing decoration image | `layouts/` templates added as first/last sheet parts (title from `character_properties[current_player_id].official_name` or a sheet variable, toc depth as variable) |
| Page breaks after each part (`add_page_breaks`), `spacer` | `[PAGEBREAK]` / `[BR]` markers in layout templates, eg. a `layouts/page_break.rst` part interleaved in the parts lists |
| Decorated vs undecorated vs big font stylesheets | hierarchical `settings.rst2pdf_extra_args` per group/sheet (an override replaces the whole string) |
| Checklist `murder_party_items` and Archives `_extract_crate()` / items per crate | hook computing both structures as today (ported code), templates and regular sheets unchanged; see below |
| `INGAME_CLUES_PARTS` + `export_ingame_clues_pdfs()` | `document_generation` (after G6) |
| `_register_story_tags_from_clues_document()` | storygen `document_generation` (already renders ODT text for tags; G10 to skip splitting) |
| `display_and_check_story_tags()` + facts summary | storygen `summary_generation` (+ G10 exit code) |
| Mindstorm `gamemaster_players_extracts` | one template looping on `player_names`, with `{% with current_player_id=p, hide_anthropia_credentials=true %}{% include %}` of per-player parts (check facts are attributed to each player) |
| Mindstorm surveillance reports (`.official_name` -> `.spoiling_official_name` + double rendering) | in `gamemaster_manor_surveillance_reports_meta_*.rst`: `{{ x \| replace(".official_name", ".spoiling_official_name") \| dangerous_render \| indent(...) }}` |
| `strip_pychronia_page_markup` filter | registered by the hook (G5) |
| `local.yaml` real identities, `use_player_photos` (`docs/trombinoscope/`) | optional data file with fallback (G3) + hook |
| `_ensure_intial_game_data_dump_is_present()` (starts Django) | separate command; dump stored next to the game files |
| Email sending (`if False` blocks) | out of scope: separate tool, or deleted |
| `--with-clues` option | document splitting step (G10) |

storygen's `inventory_generation` is NOT a drop-in replacement for the checklist logic:
it expects a YAML mapping, whereas the checklists are lists of `[section, items]` pairs (inventory.py:32 vs
mysteryparty_common_utils.py:16-18); it strips `@` from crate names and keeps insertion order, whereas Archives
keeps `@CRATE` and sorts crates (build_archives_pdfs.py:425,451; the glossary relies on these codes); it strips the crate
prefix from per-section labels; it names labels `item_title` instead of `item_label`; it lacks the "no IMPORTANT marker
at all means all important" fallback that the Mindstorm checklist relies on; and its variables only exist in inventory
templates, whereas Mindstorm's regular `miscellaneous/alphonse_special_sales_*.rst` loops on `murder_party_items` too.
Hence the hook approach; converting to storygen inventories can come later.


## Shared theme

storygen chdirs into the project directory, and every Chrysalis project sits at the same depth
(`Chrysalis/<game>/scenario_fixtures/`), so a shared `docs/rst2pdf_storygen.conf` can use
`stylesheet_path="../../docs/assets"` and `font_path="../../fonts"`, referenced by each project as
`"rst2pdf_conf_file": "../../docs/rst2pdf_storygen.conf"`.
Verified: rst2pdf uses these configuration values as-is, ie. relative to its CWD (the project dir), not to the
configuration file (rst2pdf `createpdf.py:1291-1338`, `styles.py:98-121`).

But background images inside stylesheets are also resolved relative to the CWD (rst2pdf `createpdf.py:1085-1088`),
and `dark_background*.yaml` / `shiny.yaml` use `assets/<image>.jpg` (relative to `docs/`): from a project dir,
rst2pdf only logs "Missing background image file" and exits 0. Until the old scripts are deleted, use storygen
copies of these stylesheets with `../../docs/assets/...` backgrounds (eg. in `docs/assets/storygen/`).
Same CWD issue for `docs/docutils.conf` (G7).


## Expected output layout (example: Mindstorm, French)

```
mysteryparty_mindstorm/scenario_fixtures/_output/fr/
    gamemaster/gamemaster_manual_full_sheet.pdf
    gamemaster/players_extracts_full_sheet.pdf
    gamemaster/assets_checklist_full_sheet.pdf
    common/lore_introduction_full_sheet.pdf
    players/garnet_full_sheet.pdf
    players/garnet_cheat_sheet.pdf
    npcs/alphonse_full_sheet.pdf
    documents/alphonse_special_sales_full_sheet.pdf
    miscellaneous/ingame_clues_mindstorm/<clue>.pdf
    summaries/...
```

Generated `_build/` and `_output/` folders must be git-ignored for all projects (per-project `.gitignore`, as Cromlech).


## Phases

1. **storygen core** - G1 (optional sections), G2 (template dirs), G3 (data files), G4 (`{lang}`),
   G7 rst2pdf error detection and smart quotes, G9 (`current_player_id`), G10.
   Verify: Cromlech FR/EN outputs unchanged.
2. **Small games**, each one validating a feature cheaply:
   - `rpg_sentience`: configuration with a single sheet, shared theme (stylesheet copies, docutils config).
   - `rpg_skeletons`: rename the scenario to `skeletons_scenario_fr.rst`, French-only configuration
     (`--lang fr`); delete `generate_pdf_from_rst.py` (the committed PDFs stay as they are).
   - Descent: project in `rpg_descent/` (G11), data file + one sheet per player (sheet names = YAML player keys),
     template rewritten to read `descent_rpg.players[current_player_id]` and `descent_rpg.common_equipments`,
     master script sheet.
   - Auction: data file, section-joining templates for full/extract manuals, G8.
3. **Clue splitter port (G6), RST parity (rest of G7), tag dialect renaming**:
   capture old baselines for FR and EN first, then rename in RST, checklist YAMLs and ODTs in one go.
4. **Archives**, then **Mindstorm** with the hook (G5) and the special documents.
5. **Cleanup** - delete the build scripts, `rpg_sheet_generator.py`, `mysteryparty_common_utils.py`
   (`check_fixture_translations.py` imports neither), `odt2txt.py`, `unoconv.py`, `dotted_toc_compat.py`,
   `rst2pdf.conf`, `output_*/`; update `Readme.rst` (build instructions, `trombinoscope/` location) and the
   glossary/`PROBLEMS_TO_SOLVE.txt` mentions of `build_archives_pdfs.py`; point the original stylesheets to their new
   location and drop the copies; possibly move `docs/assets` and fonts to a dedicated shared theme folder.

Each phase: build FR and EN with both systems where possible, then diff the intermediate RST
(`docs/output_<game>/<lang>/*.rst` vs `_build/<lang>/**/*.txt`), and compare PDF page counts, rst2pdf error logs
and coherence reports before deleting the old script.
