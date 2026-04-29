#!/usr/bin/env python3
"""Validate first-party Agent Skills in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_FIELDS = ("name", "description")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, [f"{path}: missing YAML frontmatter"]

    end = text.find("\n---", 4)
    if end == -1:
        return {}, [f"{path}: frontmatter is not closed"]

    fields: dict[str, str] = {}
    errors: list[str] = []
    for line_number, raw_line in enumerate(text[4:end].splitlines(), start=2):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{path}:{line_number}: expected 'key: value'")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")

    return fields, errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_name = skill_dir.name

    if not NAME_PATTERN.fullmatch(skill_name):
        errors.append(f"{skill_dir}: folder name must use lowercase kebab-case")

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"{skill_dir}: missing SKILL.md"]

    fields, frontmatter_errors = parse_frontmatter(skill_file)
    errors.extend(frontmatter_errors)

    for field in REQUIRED_FIELDS:
        if not fields.get(field):
            errors.append(f"{skill_file}: missing required frontmatter field '{field}'")

    name = fields.get("name", "")
    if name and name != skill_name:
        errors.append(f"{skill_file}: name must match folder '{skill_name}'")
    if name and not NAME_PATTERN.fullmatch(name):
        errors.append(f"{skill_file}: name must use lowercase kebab-case")

    description = fields.get("description", "")
    if description and not description.startswith("Use when"):
        errors.append(f"{skill_file}: description must start with 'Use when'")

    return errors


def validate_repo(root: Path) -> list[str]:
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return [f"{skills_dir}: missing skills directory"]

    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if not skill_dirs:
        return [f"{skills_dir}: no skill directories found"]

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repo(root)
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = len([path for path in (root / "skills").iterdir() if path.is_dir()])
    print(f"Validated {skill_count} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
