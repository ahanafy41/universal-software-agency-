#!/usr/bin/env python3
"""
diff_verifier.py - Automated Blast-Radius & Code Preservation Diff Auditor
"""

import os
import sys
import difflib

def verify_diff(original_file, modified_file, max_churn_percent=35.0):
    if not os.path.isfile(original_file) or not os.path.isfile(modified_file):
        print("Error: Both original and modified files must exist.")
        sys.exit(1)

    with open(original_file, "r", encoding="utf-8", errors="ignore") as f:
        orig_lines = f.readlines()
    with open(modified_file, "r", encoding="utf-8", errors="ignore") as f:
        mod_lines = f.readlines()

    diff = list(difflib.unified_diff(orig_lines, mod_lines, fromfile=original_file, tofile=modified_file))
    added = sum(1 for line in diff if line.startswith("+") and not line.startswith("+++"))
    deleted = sum(1 for line in diff if line.startswith("-") and not line.startswith("---"))
    total_orig = max(len(orig_lines), 1)
    churn = ((added + deleted) / total_orig) * 100.0

    print(f"=== Diff Verifier Blast-Radius Audit ===")
    print(f"Lines added: {added} | Lines removed: {deleted} | Churn: {churn:.2f}% (Max allowed: {max_churn_percent}%)")

    if churn > max_churn_percent:
        print(f"[FAIL] Churn exceeds blast radius threshold of {max_churn_percent}%. Modification rejected.")
        sys.exit(1)
    else:
        print("[PASS] Diff churn is strictly within blast radius safety bounds.")
        sys.exit(0)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 diff_verifier.py <original_file> <modified_file> [max_churn_percent]")
        sys.exit(1)
    max_churn = float(sys.argv[3]) if len(sys.argv) > 3 else 35.0
    verify_diff(sys.argv[1], sys.argv[2], max_churn)

if __name__ == "__main__":
    main()