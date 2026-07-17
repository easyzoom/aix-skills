#!/usr/bin/env python3
"""Validate first-party Agent Skills in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError as exc:  # pragma: no cover
    raise SystemExit(
        "validate-skills.py requires PyYAML. Install it with 'pip install pyyaml'."
    ) from exc


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_FIELDS = ("name", "description")

README_FILES = ("README.md", "README.zh-CN.md")
TABLE_ROW_PATTERN = re.compile(r"^\| `([a-z0-9][a-z0-9-]*)`")
SKILL_BADGE_PATTERN = re.compile(r"badge/skills-(\d+)-")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, [f"{path}: missing YAML frontmatter"]

    end = text.find("\n---", 4)
    if end == -1:
        return {}, [f"{path}: frontmatter is not closed"]

    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as error:
        return {}, [f"{path}: invalid YAML frontmatter: {error}"]

    if data is None:
        return {}, []
    if not isinstance(data, dict):
        return {}, [f"{path}: frontmatter must be a mapping of 'key: value' pairs"]

    fields: dict[str, str] = {}
    errors: list[str] = []
    for key, value in data.items():
        if isinstance(value, (dict, list)):
            errors.append(f"{path}: field '{key}' must be a scalar value")
            continue
        fields[str(key)] = "" if value is None else str(value).strip()

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


def validate_readme_sync(root: Path, skill_names: list[str]) -> list[str]:
    """Ensure each README's skills table matches the skills/ directory."""
    errors: list[str] = []
    skill_set = set(skill_names)
    skill_count = len(skill_names)

    for readme_name in README_FILES:
        readme_path = root / readme_name
        if not readme_path.exists():
            continue

        text = readme_path.read_text(encoding="utf-8")
        listed: list[str] = []
        for line in text.splitlines():
            match = TABLE_ROW_PATTERN.match(line)
            if match:
                listed.append(match.group(1))
        listed_set = set(listed)

        for missing in sorted(skill_set - listed_set):
            errors.append(f"{readme_path}: skill '{missing}' is missing from the skills table")
        for extra in sorted(listed_set - skill_set):
            errors.append(f"{readme_path}: skills table lists '{extra}', which has no skills/ directory")

        duplicates = sorted({name for name in listed if listed.count(name) > 1})
        if duplicates:
            errors.append(f"{readme_path}: skills table has duplicate rows: {', '.join(duplicates)}")

        badge = SKILL_BADGE_PATTERN.search(text)
        if badge and int(badge.group(1)) != skill_count:
            errors.append(
                f"{readme_path}: skills badge says {badge.group(1)} but there are {skill_count} skill(s)"
            )

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

    errors.extend(validate_readme_sync(root, [skill_dir.name for skill_dir in skill_dirs]))
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
