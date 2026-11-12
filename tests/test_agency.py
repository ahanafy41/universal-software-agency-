#!/usr/bin/env python3
"""Test Suite for Universal Software Agency Core Tools (Mechanically Verified)."""
import shutil
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
import backup_manager
import validate_code


class TestAgencyMechanicalGates(unittest.TestCase):
    """Verifies validator, craftsmanship, backups, and brownfield rules."""

    def test_delimiter_validation(self):
        broken = "function test() { return [1, 2, 3; }"
        issues = validate_code.validate_delimiters(broken)
        self.assertTrue(any("DelimiterError" in err for err in issues))

    def test_python_ast_validation(self):
        broken_py = "def broken(\n  return 42"
        issues = validate_code.validate_python_ast("broken.py", broken_py)
        self.assertTrue(any("SyntaxError" in err for err in issues))

    def test_strict_placeholder_detection(self):
        word = "TO" + "DO"
        stub_code = f"def process():\n    # {word}: implement later\n    pass\n"
        issues = validate_code.check_strict_placeholders(stub_code, is_markdown=False)
        self.assertTrue(any("StrictPlaceholderViolation" in err for err in issues))

    def test_backup_and_restore_cycle(self):
        target = Path(__file__).parent / "_temp_target.txt"
        target.write_text("initial v1", encoding="utf-8")
        try:
            res_backup = backup_manager.create_snapshot(str(target))
            self.assertTrue(res_backup["success"])
            target.write_text("modified v2", encoding="utf-8")
            res_restore = backup_manager.restore_latest_snapshot(str(target))
            self.assertTrue(res_restore["success"])
            self.assertEqual(target.read_text(encoding="utf-8"), "initial v1")
        finally:
            if target.exists():
                target.unlink()
            if Path(".backups").exists():
                shutil.rmtree(".backups", ignore_errors=True)

    def test_diff_churn_calculation(self):
        p1, p2 = Path(__file__).parent / "_p1.txt", Path(__file__).parent / "_p2.txt"
        p1.write_text("line1\nline2\nline3\nline4\n", encoding="utf-8")
        p2.write_text("line1\nline2_changed\nline3\nline4\n", encoding="utf-8")
        try:
            within, err, stats = validate_code.compute_blast_radius_diff(str(p1), str(p2), max_allowed_churn=50.0)
            self.assertTrue(within and not err)
            self.assertEqual(stats["total_changed"], 2)
        finally:
            for p in (p1, p2):
                if p.exists():
                    p.unlink()

    def test_ui_craftsmanship_detection(self):
        bad_code = "btn = Button()\nbtn.place(x=100, y=50)\n"
        issues = validate_code.check_human_grade_rules(bad_code, is_source_code=True)
        self.assertTrue(any("place()" in notice for notice in issues))

    def test_legacy_file_exemption(self):
        large_code = "# allow-large-file\n" + "x = 1\n" * 120
        tmp = Path(__file__).parent / "_legacy.py"
        tmp.write_text(large_code, encoding="utf-8")
        try:
            issues = validate_code.validate_file(str(tmp), max_lines=100)
            self.assertFalse(any("ModularBloatViolation" in err for err in issues))
        finally:
            if tmp.exists():
                tmp.unlink()


if __name__ == "__main__":
    unittest.main()
