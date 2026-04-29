# Repository Structure

This repository is organized for three audiences: users, contributors, and maintainers.

## Top-Level Directories

| Path | Responsibility |
| --- | --- |
| `skills/` | First-party skills maintained by this repository. |
| `template/` | Copyable starting points for new skills. |
| `awesome/` | Curated external skills and references. |
| `docs/` | Authoring, review, and publishing guidance. |
| `scripts/` | Validation and maintenance tools. |
| `.github/` | Issue and pull request templates. |

## Skill Directory Contract

Every first-party skill follows this shape:

```text
skills/<skill-name>/SKILL.md
```

Optional supporting files should stay inside that skill's folder so the skill remains portable.

## Naming Rules

- Directory names use lowercase kebab-case.
- `SKILL.md` is always uppercase.
- Frontmatter `name` matches the directory name.
- Avoid vendor names unless the skill is explicitly vendor-specific.

## Growth Model

The repository should grow in this order:

1. Add or improve a first-party skill.
2. Add validation or documentation that helps future contributors.
3. Add curated resources to `awesome/`.
4. Add automation only after a repeated manual task emerges.

This keeps the repository useful without becoming a framework too early.
