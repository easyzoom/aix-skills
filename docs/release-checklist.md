# Release Checklist

Use this checklist before making the repository public or publishing a new batch of skills.

## Content

- `README.md` explains the repository purpose and quickstart.
- Localized README links stay valid for shared sections.
- Every first-party skill has `skills/<name>/SKILL.md`.
- Every skill has `name` and `description` frontmatter.
- Descriptions start with `Use when` and describe triggers.
- Examples are public-safe and free of private data.

## Validation

Run:

```bash
python3 scripts/validate-skills.py
```

Or run the same checks in Docker:

```bash
docker run --rm -v "$PWD:/workspace" -w /workspace python:3.12-slim bash -lc "python3 scripts/validate-skills.py && python3 -m unittest tests/test_validate_skills.py"
```

Expected result:

```text
Validated N skill(s).
```

The number may change as the repository grows.

## Review

- Check links in `README.md` and `README.zh-CN.md`.
- Confirm `CONTRIBUTING.md` matches the current repository structure.
- Confirm issue and pull request templates are useful for external contributors.
- Review `git diff` for accidental generated files or local-only notes.

## Cut A Release

Releases use semantic version tags (`vX.Y.Z`). The plugin version in
`.claude-plugin/marketplace.json` matches the tag, so plugin users receive an
update only when a new version ships.

Preview what a release would change without touching git:

```bash
python3 scripts/release.py 1.1.0 --dry-run
```

Then cut it. The script validates, syncs the `skills-N` badge to the real count,
sets the plugin version, prepends a `CHANGELOG.md` section from the commits since
the last tag, commits, and creates the annotated tag:

```bash
python3 scripts/release.py 1.1.0
```

Edit the generated `CHANGELOG.md` section if the auto-drafted notes need
polishing (amend the release commit), then publish:

```bash
git push --follow-tags
```

Pushing the tag triggers `.github/workflows/release.yml`, which re-runs
validation and creates the GitHub Release using the matching `CHANGELOG.md`
section as the release notes.

## Publishing

- Ensure the license is intentional.
- Confirm `.github/workflows/validate.yml` passes on the default branch.
- Push to GitHub.
- Add repository topics such as `agent-skills`, `claude-skills`, `ai-workflows`, and `skills`.
- Open a first issue listing planned future skills.
