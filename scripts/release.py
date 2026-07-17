#!/usr/bin/env python3
"""Cut a release for the aix-skills plugin marketplace.

Usage:
    python3 scripts/release.py X.Y.Z [--dry-run]

Steps:
    1. Verify the tag does not exist and (unless --dry-run) the tree is clean.
    2. Run validate-skills.py and the unit tests.
    3. Sync the ``skills-N`` badge in both READMEs to the real skill count.
    4. Set the plugin version in ``.claude-plugin/marketplace.json``.
    5. Prepend a CHANGELOG.md section built from commits since the last tag
       (skipped if a section for this version already exists).
    6. Commit the release changes and create an annotated tag ``vX.Y.Z``.

Then publish with::

    git push --follow-tags

Pushing the tag triggers the Release workflow, which creates the GitHub Release.
"""

from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
BADGE = re.compile(r"(badge/skills-)\d+(-)")
VERSION_FIELD = re.compile(r'("version"\s*:\s*")\d+\.\d+\.\d+(")')
README_FILES = ("README.md", "README.zh-CN.md")
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CHANGELOG = ROOT / "CHANGELOG.md"


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=True
    )
    return result.stdout.strip()


def git_ok(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True)


def run_checked(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def skill_count() -> int:
    return sum(1 for path in (ROOT / "skills").iterdir() if path.is_dir())


def last_tag() -> str:
    result = git_ok("describe", "--tags", "--abbrev=0")
    return result.stdout.strip() if result.returncode == 0 else ""


def changelog_section(version: str) -> str:
    previous = last_tag()
    rev_range = f"{previous}..HEAD" if previous else "HEAD"
    subjects = git("log", rev_range, "--no-merges", "--pretty=%s").splitlines()
    today = datetime.date.today().isoformat()
    lines = [f"## [{version}] - {today}", ""]
    lines += [f"- {s}" for s in subjects] if subjects else ["- No changes recorded."]
    lines.append("")
    return "\n".join(lines)


def prepend_changelog(section: str) -> None:
    text = CHANGELOG.read_text(encoding="utf-8") if CHANGELOG.exists() else "# Changelog\n"
    lines = text.splitlines(keepends=True)
    insert_at = next(
        (i for i, line in enumerate(lines) if line.startswith("## [")), len(lines)
    )
    block = section if section.endswith("\n") else section + "\n"
    lines.insert(insert_at, block + "\n")
    CHANGELOG.write_text("".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Cut an aix-skills release.")
    parser.add_argument("version", help="release version, e.g. 1.2.0")
    parser.add_argument("--dry-run", action="store_true", help="print changes only")
    args = parser.parse_args()

    version = args.version
    if not SEMVER.fullmatch(version):
        sys.exit(f"version must be X.Y.Z, got {version!r}")
    tag = f"v{version}"

    if git("tag", "--list", tag):
        sys.exit(f"tag {tag} already exists")
    if not args.dry_run and git("status", "--porcelain"):
        sys.exit("working tree is not clean; commit or stash first")

    # Fail fast before touching anything.
    run_checked([sys.executable, "scripts/validate-skills.py"])
    run_checked([sys.executable, "-m", "unittest", "tests/test_validate_skills.py"])

    count = skill_count()
    marketplace_text = MARKETPLACE.read_text(encoding="utf-8")
    new_marketplace, replaced = VERSION_FIELD.subn(rf"\g<1>{version}\g<2>", marketplace_text)
    if replaced != 1:
        sys.exit("expected exactly one version field in marketplace.json")

    section_exists = CHANGELOG.exists() and f"## [{version}]" in CHANGELOG.read_text(
        encoding="utf-8"
    )
    section = changelog_section(version)

    if args.dry_run:
        print(f"[dry-run] tag {tag}, skill count {count}")
        print(f"[dry-run] marketplace.json version -> {version}")
        for name in README_FILES:
            text = (ROOT / name).read_text(encoding="utf-8")
            changed = BADGE.sub(rf"\g<1>{count}\g<2>", text) != text
            print(f"[dry-run] {name} badge {'updated' if changed else 'already correct'}")
        if section_exists:
            print(f"[dry-run] CHANGELOG already has [{version}] section; would keep it")
        else:
            print("[dry-run] CHANGELOG section to prepend:\n" + section)
        return 0

    for name in README_FILES:
        path = ROOT / name
        path.write_text(BADGE.sub(rf"\g<1>{count}\g<2>", path.read_text(encoding="utf-8")), encoding="utf-8")
    MARKETPLACE.write_text(new_marketplace, encoding="utf-8")
    if not section_exists:
        prepend_changelog(section)

    if git("status", "--porcelain"):
        run_checked(["git", "add", "-A"])
        run_checked(["git", "commit", "-m", f"release: {tag}"])
    else:
        print("release content already in place; tagging current HEAD")
    run_checked(["git", "tag", "-a", tag, "-m", f"Release {tag}"])
    print(f"Created {tag}. Publish with: git push --follow-tags")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
