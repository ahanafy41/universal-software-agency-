#!/usr/bin/env python3
"""
Blast Radius & Code Preservation Verifier (Zero-Dependency)
Compares modified files against backup snapshots to enforce zero-corruption invariants.
Compatible with Google Anti-Gravity 2.0 sandbox.
"""

import sys
import difflib
import argparse
import json
from pathlib import Path


def calculate_churn(original_lines, modified_lines):
    matcher = difflib.SequenceMatcher(None, original_lines, modified_lines)
    total_lines = max(len(original_lines), len(modified_lines), 1)
    changes = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag in ('replace', 'delete', 'insert'):
            changes += max(i2 - i1, j2 - j1)
    return (changes / total_lines) * 100.0


def verify_diff(orig_path: str, mod_path: str, max_churn: float = 30.0, json_output: bool = False, compact: bool = False) -> int:
    orig = Path(orig_path)
    mod = Path(mod_path)

    if not orig.is_file() or not mod.is_file():
        err = {"status": "error", "message": "Both original and modified files must exist."}
        if json_output:
            print(json.dumps(err))
        else:
            print(f"[-] Error: {err['message']}", file=sys.stderr)
        return 1

    with open(orig, "r", encoding="utf-8", errors="ignore") as f:
        orig_lines = f.readlines()
    with open(mod, "r", encoding="utf-8", errors="ignore") as f:
        mod_lines = f.readlines()

    churn = calculate_churn(orig_lines, mod_lines)
    passed = churn <= max_churn

    report = {
        "status": "PASS" if passed else "FAIL",
        "original_file": str(orig),
        "modified_file": str(mod),
        "original_lines": len(orig_lines),
        "modified_lines": len(mod_lines),
        "churn_percentage": round(churn, 2),
        "max_churn_threshold": max_churn,
        "is_within_bounds": passed,
    }

    if json_output:
        print(json.dumps(report, indent=None if compact else 2))
    else:
        status_tag = "[PASS]" if passed else "[FAIL]"
        print(f"{status_tag} Diff Churn: {report['churn_percentage']}% (Max allowed: {max_churn}%)")
        if not passed:
            print(f"[-] Blast Radius Warning: Code churn exceeded safety limit!", file=sys.stderr)

    return 0 if passed else 2


def main():
    parser = argparse.ArgumentParser(description="Blast Radius & Code Diff Verifier (Zero-Dependency)")
    parser.add_argument("original_path", help="Original snapshot file path")
    parser.add_argument("modified_path", help="Modified active file path")
    parser.add_argument("--max-churn", type=float, default=30.0, help="Maximum allowed churn percentage (default: 30.0)")
    parser.add_argument("--json", action="store_true", help="Output formatted JSON")
    parser.add_argument("--compact", action="store_true", help="Output compact single-line JSON")
    parser.add_argument("-q", "--quiet", action="store_true", help="Silent mode (exit code only)")

    args = parser.parse_args()
    sys.exit(verify_diff(args.original_path, args.modified_path, max_churn=args.max_churn, json_output=args.json, compact=args.compact))


if __name__ == "__main__":
    main()
