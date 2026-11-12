#!/usr/bin/env python3
"""
Test Suite for Universal Software Agency Core Tools
Verifies mechanical behavior, assertions, AST parsing, and backups.
"""

import sys
import unittest
from pathlib import Path

# Add scripts directory to sys.path
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import backup_manager
import validate_code


class TestAgencyMechanicalGates(unittest.TestCase):
    """Verifies that validator and backup gates enforce strict engineering rules."""

    def test_delimiter_validation(self):
        """Mismatched brackets must be detected immediately."""
        broken_code = "function test() { return [1, 2, 3; }"
        issues = validate_code.validate_delimiters(broken_code)
        self.assertTrue(any("DelimiterError" in err for err in issues))

    def test_python_ast_validation(self):
        """Invalid Python syntax must raise SyntaxError issue."""
        broken_py = "def broken(\n  return 42"
        issues = validate_code.validate_python_ast("broken.py", broken_py)
        self.assertTrue(any("SyntaxError" in err for err in issues))

    def test_strict_placeholder_detection(self):
        """Stub keywords must be flagged by the validator."""
        word = "TO" + "DO"
        stub_code = f"def process():\n    # {word}: implement later\n    pass\n"
        issues = validate_code.check_strict_placeholders(stub_code, is_markdown=False)
        self.assertTrue(any("StrictPlaceholderViolation" in err for err in issues))

    def test_backup_and_restore_cycle(self):
        """Backup manager must create snapshot and restore correctly."""
        test_file = Path(__file__).parent / "_temp_target.txt"
        test_file.write_text("initial content v1", encoding="utf-8")
        try:
            res_backup = backup_manager.create_snapshot(str(test_file))
            self.assertTrue(res_backup["success"])
            snapshot_path = Path(res_backup["snapshot_path"])
            self.assertTrue(snapshot_path.exists())

            # Modify target file
            test_file.write_text("modified content v2", encoding="utf-8")
            self.assertEqual(test_file.read_text(encoding="utf-8"), "modified content v2")

            # Restore snapshot
            res_restore = backup_manager.restore_latest_snapshot(str(test_file))
            self.assertTrue(res_restore["success"])
            self.assertEqual(test_file.read_text(encoding="utf-8"), "initial content v1")
        finally:
            if test_file.exists():
                test_file.unlink()
            if Path(".backups").exists():
                import shutil
                shutil.rmtree(".backups", ignore_errors=True)

    def test_diff_churn_calculation(self):
        """Diff verifier must calculate churn accurately."""
        p1 = Path(__file__).parent / "_orig.txt"
        p2 = Path(__file__).parent / "_mod.txt"
        p1.write_text("line1\nline2\nline3\nline4\n", encoding="utf-8")
        p2.write_text("line1\nline2_changed\nline3\nline4\n", encoding="utf-8")
        try:
            within, err, stats = validate_code.compute_blast_radius_diff(str(p1), str(p2), max_allowed_churn=50.0)
            self.assertTrue(within)
            self.assertFalse(err)
            self.assertEqual(stats["total_changed"], 2)
        finally:
            if p1.exists():
                p1.unlink()
            if p2.exists():
                p2.unlink()

    def test_ui_craftsmanship_detection(self):
        """Hardcoded desktop coordinates must trigger craftsmanship notice."""
        bad_code = "btn = Button()\nbtn.place(x=100, y=50)\n"
        issues = validate_code.check_human_grade_rules(bad_code, is_source_code=True)
        self.assertTrue(any("place()" in notice for notice in issues))


if __name__ == "__main__":
    unittest.main()
