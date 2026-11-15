#!/usr/bin/env python3
"""Validate metadata for public study notes without external dependencies."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "notes"
REQUIRED = ("title", "description", "date", "slug", "area", "draft", "reviewed", "sensitivity")
KEY = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*?)\s*$")
SLUG = re.compile(r"^study-[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fields(path: Path) -> dict[str, str]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n") or "\n---\n" not in raw[4:]:
        raise ValueError("missing YAML frontmatter delimiters")
    front = raw[4:].split("\n---\n", 1)[0]
    result: dict[str, str] = {}
    for line in front.splitlines():
        match = KEY.match(line)
        if match:
            key, value = match.groups()
            result[key] = value.strip().strip("'\"")
    return result


def main() -> int:
    errors: list[str] = []
    seen: dict[str, str] = {}
    count, published = 0, 0
    for path in sorted(NOTES.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in (".md", ".mdx"):
            continue
        relative = path.relative_to(NOTES)
        if path.name.lower() == "readme.md" or any(x.startswith("_") for x in relative.parts):
            continue
        count += 1
        try:
            if path.is_symlink():
                raise ValueError("symlink notes are not supported")
            meta = fields(path)
            absent = [key for key in REQUIRED if not meta.get(key)]
            if absent:
                raise ValueError("missing metadata: " + ", ".join(absent))
            slug = meta["slug"]
            if not SLUG.fullmatch(slug):
                raise ValueError("slug must be unique, lowercase and start with study-")
            if slug in seen:
                raise ValueError(f"duplicate slug also used in {seen[slug]}")
            seen[slug] = str(relative)
            if not DATE.fullmatch(meta["date"]):
                raise ValueError("date must be YYYY-MM-DD")
            if meta["draft"] not in ("true", "false") or meta["reviewed"] not in ("true", "false"):
                raise ValueError("draft/reviewed must be explicit YAML booleans")
            if meta["sensitivity"] not in ("public", "sanitized", "private-source"):
                raise ValueError("unexpected sensitivity value")
            if meta["draft"] == "false":
                if meta["reviewed"] != "true" or meta["sensitivity"] != "public":
                    raise ValueError("published notes require reviewed: true and sensitivity: public")
                published += 1
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{relative}: {exc}")

    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    print(f"Checked {count} note(s): {published} public, {count - published} drafts.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
