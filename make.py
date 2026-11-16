#!/usr/bin/env python
"""
Build or clean the storygen projects (the "scenario_fixtures/" folders) of the Chrysalis games.

    python make.py build [<game folder>] [--lang fr|en] [<storygen options>...]
    python make.py clean [<game folder>] [--lang fr|en] [<storygen options>...]

Without game folder, all games are processed. Without --lang, all languages are processed.
Other options (e.g. --no-pdf, --skip-document-splitting, --variable decorations=false, --dry-run)
are passed as-is to the "pychronia_storygen build|clean" command.

Python code released under the MIT license.
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
PROJECT_FOLDER_NAME = "scenario_fixtures"
LANGUAGES = ("fr", "en")

# Invoke the command line of storygen with the current interpreter, so that the storygen of its virtualenv is used
STORYGEN_COMMAND = [sys.executable, "-m", "pychronia_storygen.cli"]


def find_all_projects():
    """Return the storygen project folders of all games (those with a configuration file), relative to the repo root."""
    return sorted(config_file.parent.relative_to(REPO_ROOT)
                  for config_file in REPO_ROOT.glob("*/%s/configuration*.yaml" % PROJECT_FOLDER_NAME)
                  if not config_file.parent.parent.name.startswith("_"))


def resolve_project(folder):
    """Return the storygen project folder of a game folder (or of a project folder given directly)."""
    folder = Path(folder).resolve()
    for candidate in (folder / PROJECT_FOLDER_NAME, folder):
        if any(candidate.glob("configuration*.yaml")):
            try:
                return candidate.relative_to(REPO_ROOT)
            except ValueError:
                return candidate
    raise SystemExit("No storygen project (%s/configuration.yaml) found in folder %s" % (PROJECT_FOLDER_NAME, folder))


def run_storygen(command, project, extra_args):
    """Run a storygen command on a project, and return whether it succeeded."""
    full_command = STORYGEN_COMMAND + [command, project.as_posix()] + list(extra_args)
    print("\n>>> %s" % subprocess.list2cmdline(["pychronia_storygen"] + full_command[len(STORYGEN_COMMAND):]),
          flush=True)
    return subprocess.call(full_command, cwd=REPO_ROOT) == 0


def main():
    parser = argparse.ArgumentParser(
        allow_abbrev=False,  # Don't mistake storygen options for abbreviations of ours
        usage="%(prog)s {build,clean} [folder] [--lang {fr,en}] [storygen options...]",
        description="Build or clean the storygen projects of the Chrysalis games. The optional folder, right after "
                    "the command, is a game folder (e.g. 'rpg_descent') or its '%s' subfolder; all games are "
                    "processed if it is omitted." % PROJECT_FOLDER_NAME,
        epilog="Other options are passed to 'pychronia_storygen build|clean', "
               "e.g. --no-pdf, --skip-document-splitting, --variable decorations=false, --only \"*amethyst*\", "
               "--dry-run.")
    parser.add_argument("command", choices=["build", "clean"])
    parser.add_argument("--lang", choices=LANGUAGES, action="append",
                        help="Language to process (can be repeated); all languages if omitted")

    # The folder is only taken right after the command, so that values of storygen options aren't mistaken for it
    argv = sys.argv[1:]
    has_folder = len(argv) >= 2 and argv[0] in ("build", "clean") and not argv[1].startswith("-")
    folder = argv.pop(1) if has_folder else None
    args, storygen_args = parser.parse_known_args(argv)

    projects = [resolve_project(folder)] if folder else find_all_projects()

    if args.command == "build":
        languages = args.lang or LANGUAGES  # Translated projects must be built once per language
    else:
        languages = args.lang or [None]  # Without language, storygen cleans the files of all languages

    start_time = time.monotonic()
    failures = []
    for project in projects:
        for language in languages:
            lang_args = ["--variable", "lang=%s" % language] if language else []
            if not run_storygen(args.command, project, lang_args + storygen_args):
                failures.append("%s%s" % (project.as_posix(), " (%s)" % language if language else ""))

    total_count = len(projects) * len(languages)
    print("\n%s: %d/%d storygen run(s) succeeded, in %.0fs" % (
        args.command, total_count - len(failures), total_count, time.monotonic() - start_time))
    for failure in failures:
        print("  FAILED: %s" % failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
