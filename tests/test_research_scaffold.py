from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_research", ROOT / "tools" / "validate_research.py"
)
assert SPEC is not None and SPEC.loader is not None
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ResearchScaffoldTest(unittest.TestCase):
    def test_scaffold_contract(self) -> None:
        errors: list[str] = []
        VALIDATOR.validate_interface(errors)
        VALIDATOR.validate_no_pipeline_input(errors)
        VALIDATOR.validate_no_python_input(errors)
        VALIDATOR.validate_policy(errors)
        source_ids = VALIDATOR.validate_catalog(errors)
        VALIDATOR.validate_evidence(source_ids, errors)
        VALIDATOR.validate_icon_evidence(source_ids, errors)
        VALIDATOR.validate_markdown_links(errors)
        self.assertEqual([], errors, "\n".join(errors))


if __name__ == "__main__":
    unittest.main()
