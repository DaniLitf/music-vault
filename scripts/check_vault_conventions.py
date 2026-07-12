#!/usr/bin/env python3
"""
Checks changed markdown files in this vault against the conventions in CLAUDE.md.

This does NOT try to verify facts (dates, discography accuracy, etc.) -- that
still needs a human or an agent doing research. It only catches mechanical,
structural mistakes that are cheap to automate:

  - Index.md was edited (it's Dataview-generated and must never be hand-edited)
  - file sits in the wrong letter subfolder for its name
  - frontmatter keys use spaces instead of underscores
  - required frontmatter keys are missing for the page type
  - date fields aren't YYYY or YYYY-MM-DD
  - wikilinks to Artists/Members/Producers/Studios are missing the subfolder
  - page is missing a "## Sources" section

Usage:
  python3 check_vault_conventions.py <file1.md> <file2.md> ...
  python3 check_vault_conventions.py --file-list changed_files.txt

The --file-list form reads one path per line, which is the safe option since
filenames in this vault often contain spaces (e.g. "50 Cent.md") that would
be mangled by shell word-splitting if passed as separate arguments.

Exits 1 if any errors were found, 0 otherwise. Writes a markdown report to
stdout and, if GITHUB_STEP_SUMMARY is set, appends the same report there.
"""

import os
import re
import sys
import unicodedata

TRACKED_ROOTS = {
    "Artists": {
        "required": ["genre", "also_known_as"],
    },
    "Members": {
        "required": ["real_name", "also_known_as", "birth_date", "death_date", "nationality"],
    },
    "Producers": {
        "required": ["real_name", "also_known_as", "birth_date", "death_date", "nationality"],
    },
    "Studios": {
        "required": ["location", "active_years"],
    },
}

DATE_RE = re.compile(r"^\d{4}(-\d{2}-\d{2})?$")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(\|[^\]]+)?\]\]")


def expected_subfolder(name):
    """First character of the filename -> expected subfolder name."""
    if not name:
        return "0-9"
    ch = name[0]
    if ch.isdigit():
        return "0-9"
    decomposed = unicodedata.normalize("NFKD", ch)
    base = "".join(c for c in decomposed if not unicodedata.combining(c))
    if base.isalpha() and base.isascii():
        return base.upper()
    return "0-9"


def parse_frontmatter(text):
    """Small YAML-ish frontmatter parser: handles scalars, empty values,
    and simple '- item' lists. Good enough for this vault's flat frontmatter."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    fm_block, body = parts[1], parts[2]

    fields = {}
    current_key = None
    for line in fm_block.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z0-9_ ]+):\s*(.*)$", line)
        if m and not line.startswith(" "):
            key, val = m.group(1), m.group(2).strip()
            current_key = key
            if val in ('""', "''"):
                val = ""
            if val == "":
                fields[key] = []
            else:
                fields[key] = val
        elif line.strip().startswith("- ") and current_key is not None:
            item = line.strip()[2:].strip()
            if not isinstance(fields.get(current_key), list):
                fields[current_key] = []
            fields[current_key].append(item)
    return fields, body


def check_file(path):
    errors = []
    name = os.path.basename(path)
    stem = os.path.splitext(name)[0]
    parts = path.replace("\\", "/").split("/")

    if name == "Index.md" and len(parts) == 1:
        errors.append("Index.md is Dataview-generated and must never be hand-edited.")
        return errors

    if not parts or parts[0] not in TRACKED_ROOTS:
        return errors

    root = parts[0]
    rules = TRACKED_ROOTS[root]

    if len(parts) != 3:
        errors.append(
            "Path `%s` doesn't match the `%s/<Letter>/<Name>.md` convention." % (path, root)
        )
    else:
        actual_sub = parts[1]
        expected_sub = expected_subfolder(stem)
        if actual_sub != expected_sub:
            errors.append(
                "`%s` is in subfolder `%s`, expected `%s` (first character of `%s`)."
                % (path, actual_sub, expected_sub, stem)
            )

    if not os.path.exists(path):
        errors.append("`%s` was deleted or renamed -- skipping content checks." % path)
        return errors

    with open(path, "r", encoding="utf-8-sig") as f:
        text = f.read()

    fields, body = parse_frontmatter(text)
    if fields is None:
        errors.append("`%s` has no YAML frontmatter block (expected `---` ... `---`)." % path)
        fields, body = {}, text

    for key in fields:
        if " " in key.strip():
            errors.append("`%s` frontmatter key `%s` contains a space -- use underscores." % (path, key))

    for req in rules["required"]:
        if req not in fields:
            errors.append("`%s` is missing required frontmatter key `%s:`." % (path, req))

    for date_key in ("birth_date", "death_date"):
        if date_key in fields:
            val = fields[date_key]
            if isinstance(val, str) and val and not DATE_RE.match(val):
                errors.append("`%s` field `%s: %s` isn't `YYYY` or `YYYY-MM-DD`." % (path, date_key, val))

    for match in WIKILINK_RE.finditer(body):
        target = match.group(1)
        target_root = target.split("/")[0]
        if target_root in TRACKED_ROOTS:
            segments = target.split("/")
            if len(segments) < 3:
                errors.append(
                    "`%s` has wikilink `[[%s]]` missing its subfolder (should be `%s/<Letter>/Name`)."
                    % (path, target, target_root)
                )

    if root in TRACKED_ROOTS and "## Sources" not in body:
        errors.append("`%s` is missing a `## Sources` section." % path)

    return errors


def read_file_list(list_path):
    with open(list_path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


def main(argv):
    if argv and argv[0] == "--file-list":
        if len(argv) < 2:
            print("Error: --file-list requires a path argument.")
            return 2
        files = [f for f in read_file_list(argv[1]) if f.endswith(".md")]
    else:
        files = [f for f in argv if f.endswith(".md")]

    all_errors = {}
    for path in files:
        errs = check_file(path)
        if errs:
            all_errors[path] = errs

    lines = ["# Vault convention check\n"]
    if not files:
        lines.append("No markdown files changed.\n")
    elif not all_errors:
        lines.append("Checked %d file(s). No convention issues found.\n" % len(files))
    else:
        total = sum(len(v) for v in all_errors.values())
        lines.append("Checked %d file(s). Found %d issue(s) in %d file(s):\n" % (len(files), total, len(all_errors)))
        for path, errs in all_errors.items():
            lines.append("\n### `%s`" % path)
            for e in errs:
                lines.append("- %s" % e)
    report = "\n".join(lines) + "\n"

    print(report)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(report)

    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
