#!/usr/bin/env python3
"""
diff_verifier.py - AST & Line Diff Bounds Verifier (Blast Radius Limiter)
Part of Universal Software & AI Engineering Agency
"""

import sys
import os
import difflib

def verify_diff(original_file, modified_file, max_allowed_churn=100):
    if not os.path.exists(original_file) or not os.path.exists(modified_file):
        print("Error: One or both files do not exist.")
        return False

    with open(original_file, "r", encoding="utf-8", errors="ignore") as f1:
        lines1 = f1.readlines()
    with open(modified_file, "r", encoding="utf-8", errors="ignore") as f2:
        lines2 = f2.readlines()

    diff = list(difflib.unified_diff(lines1, lines2, fromfile=original_file, tofile=modified_file))
    churn = len([l for l in diff if l.startswith("+") or l.startswith("-")]) - 2

    print(f"Diff verification: Total modified lines (churn) = {churn}")
    if churn > max_allowed_churn:
        print(f"Warning: Blast radius exceeded maximum allowed churn ({max_allowed_churn}).")
        return False

    print("Diff verification passed: Blast radius within bounds.")
    return True

def main():
    if len(sys.argv) < 3:
        print("Usage: diff_verifier.py <original_file> <modified_file> [max_churn]")
        sys.exit(1)

    orig = sys.argv[1]
    mod = sys.argv[2]
    max_c = int(sys.argv[3]) if len(sys.argv) > 3 else 100

    success = verify_diff(orig, mod, max_c)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
