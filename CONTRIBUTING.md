# Contributing

Thanks for helping improve AIX Skills.

This repository welcomes:

- New first-party skills under `skills/`.
- Improvements to existing skills.
- Curated resources for `awesome/`.
- Documentation and validation improvements.

## Add A New Skill

1. Copy the template:

   ```bash
   cp -R template/skill-template skills/my-new-skill
   ```

2. Rename the skill in frontmatter:

   ```yaml
   ---
   name: my-new-skill
   description: Use when an agent needs to ...
   ---
   ```

3. Write the skill body with:

   - Clear trigger conditions.
   - A repeatable workflow.
   - Verification steps.
   - Common mistakes.
   - One strong example if useful.

4. Run validation:

   ```bash
   python3 scripts/validate-skills.py
   ```

## Skill Review Criteria

Pull requests are reviewed for:

- Public safety: no secrets, private customer data, or internal-only links.
- Discoverability: `description` starts with `Use when` and includes concrete triggers.
- Portability: supporting files stay inside the skill folder.
- Practicality: instructions are repeatable and verifiable.
- Scope: one skill should cover one coherent workflow.

## Add An Awesome Resource

Edit `awesome/README.md` and include:

- Resource name and link.
- One sentence describing the value.
- The most relevant category.
- Any license or usage caveat if known.

## Commit Style

Use concise commit messages:

- `docs: add skill authoring guide`
- `feat: add release-note skill`
- `chore: update validation script`

## Before Opening A Pull Request

Run:

```bash
python3 scripts/validate-skills.py
```

Then review:

- `README.md` still reflects available skills.
- New links work.
- No local-only files or generated noise are included.
