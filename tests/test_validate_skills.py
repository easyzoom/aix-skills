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


if __name__ == "__main__":
    unittest.main()
