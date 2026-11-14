# Migration of Chrysalis PDF builds to Pychronia-storygen

Goal: replace `build_archives_pdfs.py`, `build_auction_pdfs.py`, `build_descent_pdfs.py` and
`build_mindstorm_pdfs.py` (plus their helpers `rpg_sheet_generator.py` and `mysteryparty_common_utils.py`)
with Pychronia-storygen projects, as is already the case for `mysteryparty_cromlech/scenario_fixtures`.
Also build the scenarios of `rpg_sentience` and `rpg_skeletons` (plain RST to PDF) with storygen.


## Decisions

- **Output names**: conform to storygen standards (`<group folders>/<sheet>_full_sheet.pdf`,
  `<sheet>_cheat_sheet.pdf`, ODT clues in a folder named after the ODT). An `output_name` option
  will only be added later, if it proves REALLY necessary. Nothing in Chrysalis or Pychronia
  consumes the current output names (the downloadable zips of the website are built by hand).
- **Python hook**: allowed, declared in the project configuration as `"<module>.<function>"`.
- **Theme**: keep the shared rst2pdf theme (`docs/assets/*.yaml` stylesheets and images,
  `Chrysalis/fonts/`) for now, if it works from storygen project folders.


## Current state

| Build | Size | Fit with storygen | Blockers |
|---|---|---|---|
| `rpg_sentience` | 1 plain RST per language | Almost ready | mandatory config sections |
| `rpg_skeletons` | 1 French RST in `Chrysalis Skeletons scenario 03.txt` | Almost ready | file renaming, mandatory config sections |
| Descent | 63 lines | Easy | YAML data files as variables |
| Auction | 83 lines | Easy | data files, section-joining template, unlinking of unknown RST targets |
| Archives | 626 lines | Medium | everything below |
| Mindstorm | 606 lines | Hardest | everything below, plus computed variables and special documents |


## Gaps in storygen

### G1 - Optional configuration sections

`cli.py` indexes `project_data_tree["document_generation"]`, `["inventory_generation"]` and
`["summary_generation"]` directly, so projects lacking them crash. `_generate_summary_files()` also
references `has_serious_errors1/2/3` even when the matching template is not configured.
Make all sections (and each summary template) optional.

### G2 - Extra template directories

Archives and Mindstorm load templates from `../mysteryparty_common/scenario_fixtures` too
(see the FIXME in `cli.py`). Add a `"template_dirs"` configuration entry, used both by the jinja2
loader and by macro registration (with the same language filtering and excluded build/output dirs).

### G3 - Data files loaded as variables

Add a `"data_files"` configuration entry mapping variable names (or the root namespace) to YAML files,
for example `descent_rpg_data_{lang}.yaml`, `gamemaster_manual_{lang}.yaml` (auction),
`_initial_game_data_dump.yaml` + its English partial overlay (port `deep_merge_localized_overlay()`),
the private `mysteryparty_common/scenario_fixtures/local.yaml` (must be allowed to be missing/optional).

### G4 - `{lang}` placeholder in configuration paths

Cromlech duplicates its whole configuration per language because its sheet names are localized.
Archives and Mindstorm keep English names in both languages, so a single `configuration.yaml` with
paths like `players/garnet_role_{lang}.rst` avoids duplicating ~50 sheet entries and ~80 clue entries.

### G5 - Python hook

Configuration entry `"variables_hook": "storygen_hooks.prepare_variables"`; the module is imported
from the project directory (inserted in `sys.path`). Called once per run, after data files are loaded,
with the root variables and the language; it returns (or mutates) the variables.
Covers the residual logic of the build scripts: merging `local.yaml` character overrides,
`full_official_title`, `spoiling_official_name`, `use_player_photos`, etc.

A per-sheet hook does NOT seem needed: the per-player Mindstorm variables (`current_player_password`,
`current_player_account`, `current_player_extra_goods`, `permissions`, `hide_anthropia_credentials`)
are only used by `common_anthropia_account_summary_displayer_{fr,en}.rst`, which can read
`character_properties[current_player_id]` instead.

### G6 - Port the Chrysalis ODT clue splitter

`mysteryparty_common_utils._generate_clues_pdfs_from_main_odt_document()` is more robust than storygen's
`split_odt_file_into_separate_documents()`: single LibreOffice export then pypdf split, check of the
total page count, check of a text snippet on the first page of each clue, `None` entries for skipped
pages, pruning of unused page resources, and check that gamemaster comments (story tags) were really
extracted (`comment_samples`). Extend `document_splitting` entries to `[name, page_count, snippet]`.

### G7 - RST post-processing parity

`rpg_sheet_generator.write_rst_file()` also replaces `" : "` by a non-breaking space in French and
strips BOMs of included templates; storygen only handles `" :\n"`.
Image paths `../assets/...` (relative to `docs/output_<game>/`) must become `{{ project_dir }}...`
paths, as in Cromlech (~12 image directives).

### G8 - Unlinking of unknown RST targets

Optional per-sheet setting, ported from `build_auction_pdfs.unlink_unknown_rst_targets()`, for the
truncated auction gamemaster manual.


## Story tag dialects (main risk)

| Chrysalis tag | storygen equivalent | Occurrences (archives + mindstorm) |
|---|---|---|
| `{% fact "x" %}` (no output) | `{% xfact "x" %}` | ~1270 |
| `{% hint "x" is needed %}` (no output) | `{% xitem "x" is needed %}` | ~640 |
| `{% symbol "v" for "x" %}` | same | ~860 |
| context var `register_symbols=False` | unsupported | only for French ODT fallback, obsolete since English ODTs exist |

Semantic differences to watch:
- storygen lowercases fact and item names, and errors when a character is both author and viewer of a fact.
- Chrysalis normalizes symbol values with `.strip().lower().replace("\n", "")`, storygen only with `.lower()`:
  symbols extracted from ODTs may raise new false errors, so storygen's normalization should probably be aligned.
- Facts rendered without `current_player_id` are attributed to `"ingame_clues"` in Chrysalis, `"<master>"` in storygen.
- The `gamemaster_facts_summary_{fr,en}.rst` templates use `facts_summary` / `aggregated_facts_summary`;
  they must be rewritten for storygen's `facts_registry` (or replaced by storygen's summary templates).

The renaming itself is mechanical; the safety net is to compare coherence reports of the old and new builds.


## Mapping of build script logic

| Build script logic | Destination |
|---|---|
| `OFFICIAL_NAMES`, `DOCUMENT_TITLES`, `AVAILABLE_ANTHROPIA_ABILITIES` | YAML variables (per language config or data files) |
| `GAMEMASTER_MANUAL_PARTS`, `PLAYER_MANUAL_PARTS`, `ISOLATED_DOCS`, `COMMON_*` lists | `sheet_generation` groups and sheets |
| Mindstorm cheat sheets | `cheat_sheet` entries of player sheets (storygen sets `is_cheat_sheet` itself) |
| "shark" special player (no cheat sheet) | sheet with only a `full_sheet` |
| Title + table of contents header, trailing decoration image | `layouts/` templates added as first/last sheet parts |
| Page breaks between parts, `spacer` | `[PAGEBREAK]` / `[BR]` markers in layout templates |
| Decorated vs undecorated vs big font stylesheets | hierarchical `settings.rst2pdf_extra_args` per group/sheet |
| Archives `_extract_crate()` / items per crate | storygen `inventory_generation` (per-section and per-crate templates) |
| `INGAME_CLUES_PARTS` + `export_ingame_clues_pdfs()` | `document_generation` (after G6) |
| `_register_story_tags_from_clues_document()` | storygen `document_generation` (already renders ODT text for tags) |
| `display_and_check_story_tags()` + facts summary | storygen `summary_generation` |
| Mindstorm `gamemaster_players_extracts` | one template looping on players, with `{% include %}` of per-player parts |
| Mindstorm surveillance reports (`.official_name` -> `.spoiling_official_name` + double rendering) | `spoiler_mode` variable in templates, or `dangerous_render` filter |
| `local.yaml` real identities | optional data file + hook |
| `_ensure_intial_game_data_dump_is_present()` (starts Django) | separate command; dump stored next to the game files |
| Email sending (`if False` blocks) | out of scope: separate tool, or deleted |
| `--with-clues` option | storygen `-t documents` / other `-t` selections |


## Shared theme

storygen chdirs into the project directory, and every Chrysalis project sits at the same depth
(`Chrysalis/<game>/scenario_fixtures/`), so a shared `docs/rst2pdf_storygen.conf` can use
`stylesheet_path="../../docs/assets"` and `font_path="../../fonts"`, referenced by each project as
`"rst2pdf_conf_file": "../../docs/rst2pdf_storygen.conf"`.
To verify: that rst2pdf resolves these configuration paths relative to the current directory
(as Cromlech's `./themes/` suggests), and not relative to the configuration file.


## Expected output layout (example: Mindstorm, French)

```
mysteryparty_mindstorm/scenario_fixtures/_output/fr/
    gamemaster/gamemaster_manual_full_sheet.pdf
    gamemaster/players_extracts_full_sheet.pdf
    common/lore_introduction_full_sheet.pdf
    players/garnet_full_sheet.pdf
    players/garnet_cheat_sheet.pdf
    npcs/alphonse_full_sheet.pdf
    miscellaneous/ingame_clues_mindstorm/<clue>.pdf
    inventories/...
    summaries/...
```

Generated `_build/` and `_output/` folders must be git-ignored for all projects.


## Phases

1. **storygen core** - G1 (optional sections), G2 (template dirs), G3 (data files), G4 (`{lang}`).
2. **Small games**, each one validating a feature cheaply:
   - `rpg_sentience`: configuration with a single sheet, shared theme.
   - `rpg_skeletons`: rename the scenario to `skeletons_scenario_fr.rst`, French-only configuration.
   - Descent: data file + one sheet per player (listed in configuration), master script sheet.
   - Auction: data file, section-joining templates for full/extract manuals, G8.
3. **Clue splitter port (G6), RST parity (G7), tag dialect renaming** - compare coherence reports
   between the old and new builds.
4. **Archives**, then **Mindstorm** with the hook (G5) and the special documents.
5. **Cleanup** - delete the build scripts and the unused parts of `rpg_sheet_generator.py` /
   `mysteryparty_common_utils.py` (`check_fixture_translations.py` may still need some helpers),
   possibly move `docs/assets` and fonts to a dedicated shared theme folder.

Each phase: build FR and EN with both systems where possible, and compare PDF page counts and
coherence reports before deleting the old script.
