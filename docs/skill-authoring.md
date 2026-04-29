# Skill Authoring Guide

This guide defines the style for skills in this repository.

## Required Structure

Each first-party skill must live under `skills/<skill-name>/SKILL.md`.

```text
skills/
└── skill-name/
    ├── SKILL.md
    └── references-or-scripts-if-needed
```

Skill names must use lowercase letters, numbers, and hyphens only.

## Frontmatter

Every `SKILL.md` must start with YAML frontmatter:

```markdown
---
name: skill-name
description: Use when an agent needs to do a specific task in a specific context
---
```

Rules:

- `name` must match the folder name.
- `description` should start with `Use when`.
- `description` should describe trigger conditions, not the whole workflow.
- Keep frontmatter short enough for agents to scan quickly.

## Body Sections

Use these sections unless the skill is intentionally tiny:

```markdown
# Skill Name

## Overview
## When To Use
## Workflow
## Verification
## Common Mistakes
```

Prefer direct instructions over essays. A skill is operational guidance, not a blog post.

## Supporting Files

Keep `SKILL.md` focused. Add supporting files only when they materially improve reuse:

- `references/*.md` for long API docs or background material.
- `scripts/*` for reusable tools.
- `examples/*` for runnable examples.

Do not add supporting files for narrative notes or one-off session history.

## Public Safety

Before publishing:

- Remove secrets, tokens, private URLs, and customer data.
- Avoid copying licensed content from other repositories.
- Link to external references instead of duplicating large sections.
- Make examples generic enough for public readers.

## Quality Bar

A skill is ready when a new agent can answer:

- When should I load this?
- What exact workflow should I follow?
- What output or behavior proves I used it correctly?
- What mistakes should I avoid?
