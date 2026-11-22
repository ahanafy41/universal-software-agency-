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
try:
    import code_mapper
except ImportError:
    code_mapper = None


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

    def test_symbol_mapper_available(self):
        self.assertIsNotNone(code_mapper, "code_mapper.py must exist in scripts/ directory")

    def test_symbol_mapping_python_ast(self):
        py_code = "class Calculator:\n    def add(self, a, b):\n        return a + b\n\ndef multiply(x, y):\n    return x * y\n"
        symbols = code_mapper.parse_python_file(py_code, "calc.py")
        names = [s["name"] for s in symbols]
        self.assertIn("Calculator", names)
        self.assertIn("Calculator.add", names)
        self.assertIn("multiply", names)
        # Check line ranges
        mult_sym = next(s for s in symbols if s["name"] == "multiply")
        self.assertEqual(mult_sym["start"], 5)
        self.assertEqual(mult_sym["end"], 6)

    def test_symbol_mapping_lua(self):
        lua_code = "local function calculate(score)\n    return score * 2\nend\n\nfunction onTouch(x, y)\n    print(x)\nend\n"
        symbols = code_mapper.parse_lua_file(lua_code, "test.lua")
        names = [s["name"] for s in symbols]
        self.assertIn("calculate", names)
        self.assertIn("onTouch", names)
        calc_sym = next(s for s in symbols if s["name"] == "calculate")
        self.assertEqual(calc_sym["start"], 1)
        self.assertEqual(calc_sym["end"], 3)

    def test_validate_code_map_integration(self):
        """Verify that validate_code integrates symbol mapping cleanly."""
        self.assertTrue(hasattr(validate_code, "generate_symbol_map"), "validate_code must expose generate_symbol_map")
        tmp_py = Path(__file__).parent / "_sample_calc.py"
        tmp_py.write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")
        try:
            res = validate_code.generate_symbol_map(str(tmp_py))
            self.assertIn("add", res)
            self.assertIn("Savings", res)
        finally:
            if tmp_py.exists():
                tmp_py.unlink()


if __name__ == "__main__":
    unittest.main()
