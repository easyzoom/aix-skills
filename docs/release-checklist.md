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

- Check links in `README.md` and `awesome/README.md`.
- Confirm `CONTRIBUTING.md` matches the current repository structure.
- Confirm issue and pull request templates are useful for external contributors.
- Review `git diff` for accidental generated files or local-only notes.

## Publishing

- Ensure the license is intentional.
- Confirm `.github/workflows/validate.yml` passes on the default branch.
- Push to GitHub.
- Add repository topics such as `agent-skills`, `claude-skills`, `ai-workflows`, and `skills`.
- Open a first issue listing planned future skills.
