import importlib.util
import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


def load_validator():
    script_path = Path(__file__).resolve().parents[1] / "scripts" / "validate-skills.py"
    spec = importlib.util.spec_from_file_location("validate_skills", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load validation script")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidateSkillsTest(unittest.TestCase):
    def test_accepts_valid_skill(self):
        validator = load_validator()

        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_dir = root / "skills" / "good-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: good-skill
                    description: Use when testing valid skill metadata
                    ---

                    # Good Skill
                    """
                ),
                encoding="utf-8",
            )

            self.assertEqual(validator.validate_repo(root), [])

    def test_accepts_folded_scalar_description(self):
        validator = load_validator()

        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_dir = root / "skills" / "folded-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: folded-skill
                    description: >
                      Use when a skill needs a long description that spans
                      multiple lines for readability
                    ---

                    # Folded Skill
                    """
                ),
                encoding="utf-8",
            )

            self.assertEqual(validator.validate_repo(root), [])

    def test_rejects_invalid_yaml_frontmatter(self):
        validator = load_validator()

        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_dir = root / "skills" / "broken-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: broken-skill
                    description: "Use when unbalanced quotes break parsing
                    ---

                    # Broken Skill
                    """
                ),
                encoding="utf-8",
            )

            errors = validator.validate_repo(root)

        self.assertTrue(any("invalid YAML frontmatter" in error for error in errors))

    def test_rejects_name_mismatch_and_bad_description(self):
        validator = load_validator()

        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_dir = root / "skills" / "bad-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    name: other-name
                    description: Explains a workflow
                    ---

                    # Bad Skill
                    """
                ),
                encoding="utf-8",
            )

            errors = validator.validate_repo(root)

        self.assertTrue(any("name must match folder" in error for error in errors))
        self.assertTrue(any("description must start with 'Use when'" in error for error in errors))


    def _make_skill(self, root, name):
        skill_dir = root / "skills" / name
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            textwrap.dedent(
                f"""\
                ---
                name: {name}
                description: Use when testing {name}
                ---

                # {name}
                """
            ),
            encoding="utf-8",
        )

    def test_flags_readme_out_of_sync(self):
        validator = load_validator()

        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._make_skill(root, "alpha-skill")
            self._make_skill(root, "beta-skill")
            (root / "README.md").write_text(
                textwrap.dedent(
                    """\
                    # Repo

                    | Skill | Purpose |
                    | --- | --- |
                    | `alpha-skill` | Does alpha things. |
                    | `gamma-skill` | Stale row. |
                    """
                ),
                encoding="utf-8",
            )

            errors = validator.validate_repo(root)

        self.assertTrue(any("beta-skill' is missing" in error for error in errors))
        self.assertTrue(
            any("gamma-skill" in error and "no skills/ directory" in error for error in errors)
        )

    def test_flags_stale_skill_badge_count(self):
        validator = load_validator()

        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._make_skill(root, "alpha-skill")
            (root / "README.md").write_text(
                textwrap.dedent(
                    """\
                    # Repo

                    ![Skills](https://img.shields.io/badge/skills-9-7c3aed)

                    | Skill | Purpose |
                    | --- | --- |
                    | `alpha-skill` | Does alpha things. |
                    """
                ),
                encoding="utf-8",
            )

            errors = validator.validate_repo(root)

        self.assertTrue(any("skills badge says 9 but there are 1" in error for error in errors))

    def test_accepts_readme_in_sync(self):
        validator = load_validator()

        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._make_skill(root, "alpha-skill")
            self._make_skill(root, "beta-skill")
            (root / "README.md").write_text(
                textwrap.dedent(
                    """\
                    # Repo

                    ![Skills](https://img.shields.io/badge/skills-2-7c3aed)

                    | Skill | Purpose |
                    | --- | --- |
                    | `alpha-skill` | Does alpha things. |
                    | `beta-skill` | Does beta things. |
                    """
                ),
                encoding="utf-8",
            )

            self.assertEqual(validator.validate_repo(root), [])


if __name__ == "__main__":
    unittest.main()
