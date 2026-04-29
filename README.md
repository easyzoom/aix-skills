# AIX Skills

English | [简体中文](README.zh-CN.md)

![AIX Skills Overview](docs/assets/aix-skills-overview.svg)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-5-7c3aed)
![Validation](https://img.shields.io/badge/validation-docker%20ready-16a34a)
![Agent Skills](https://img.shields.io/badge/agent--skills-public-0f766e)

AIX Skills is a public collection of Agent Skills, templates, and references for building repeatable AI workflows.

This repository uses a hybrid structure: first-party skills that can be used directly, templates and authoring guidance for creating new skills, and a curated directory of external resources.

## What Is An Agent Skill?

Agent Skills are task-specific instructions, scripts, and references that an AI agent can load only when they are relevant. A good skill teaches an agent when to use a workflow, how to execute it, and what mistakes to avoid.

![Anatomy of an Agent Skill](docs/assets/skill-anatomy.svg)

A good skill should have:

- Clear trigger conditions: when the agent should load it.
- A repeatable workflow: steps the agent can follow reliably.
- Lightweight context: core guidance in `SKILL.md`, heavy references in supporting files.
- Verifiable results: checks that prove the skill was used correctly.

## Repository Layout

```text
.
├── skills/                 # First-party skills maintained in this repo
├── template/               # Copyable templates for new skills
├── awesome/                # Curated external skill resources
├── docs/                   # Maintainer guides and publishing checklists
├── scripts/                # Repository validation tools
├── CONTRIBUTING.md         # Contribution guide
└── README.md
```

## Available Skills

| Skill | Purpose |
| --- | --- |
| `cortex-m-debug` | Helps agents debug Cortex-M firmware, faults, startup code, and SWD/JTAG sessions. |
| `embedded-linux-login-debug` | Helps agents choose a safe login method before debugging embedded Linux devices. |
| `readme-writing` | Helps agents create attractive, trustworthy, quickstart-friendly README files. |
| `skill-writing-guide` | Teaches agents how to write concise, discoverable, testable skills for this repository. |
| `webpage-to-markdown` | Converts a public webpage URL into clean Markdown content. |

Each skill lives in its own folder under `skills/` and uses `SKILL.md` as the entry point.

## Quickstart

Copy a skill folder into your agent's skill directory, or install it with the skill manager used by your environment if supported.

```bash
cp -R skills/webpage-to-markdown ~/.claude/skills/
```

To create a new skill, start from the template:

```bash
cp -R template/skill-template skills/my-new-skill
```

Then edit `skills/my-new-skill/SKILL.md` and run validation:

```bash
python3 scripts/validate-skills.py
```

## Design Principles

![Repeatable AI Workflow](docs/assets/repeatable-workflow.svg)

- **Small core, rich references**: keep `SKILL.md` fast to scan; move long API references or scripts into supporting files.
- **Trigger-first descriptions**: frontmatter descriptions should say when to use a skill, not summarize every step.
- **One excellent example**: prefer one realistic example over many generic snippets.
- **Public-ready by default**: avoid secrets, private links, company-only assumptions, or unlicensed copied content.
- **Verification matters**: include checks so contributors can prove their skill works.

## References

This repository is inspired by:

- [google/skills](https://github.com/google/skills) for product-focused skill packs.
- [anthropics/skills](https://github.com/anthropics/skills) for skill structure, templates, and examples.
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) for curated skill discovery.

## Contributing

Contributions are welcome. Read `CONTRIBUTING.md` before opening a pull request, and run:

```bash
python3 scripts/validate-skills.py
```

## License

MIT. See `LICENSE`.
