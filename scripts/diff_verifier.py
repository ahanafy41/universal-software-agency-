#!/usr/bin/env python3
"""
Diff Verifier & Blast Radius Compliance Guard
Part of the Universal Software & AI Engineering Agency Toolset
"""

import os
import sys
import difflib
import argparse

def calculate_diff_metrics(file_a, file_b):
    if not os.path.exists(file_a) or not os.path.exists(file_b):
        print(f"Error: One or both files do not exist: '{file_a}', '{file_b}'", file=sys.stderr)
        return None

    with open(file_a, "r", encoding="utf-8", errors="replace") as fa:
        lines_a = fa.readlines()
    with open(file_b, "r", encoding="utf-8", errors="replace") as fb:
        lines_b = fb.readlines()

    diff = list(difflib.unified_diff(lines_a, lines_b, fromfile=file_a, tofile=file_b))

    additions = sum(1 for line in diff if line.startswith("+") and not line.startswith("+++"))
    deletions = sum(1 for line in diff if line.startswith("-") and not line.startswith("---"))
    total_churn = additions + deletions

    return {
        "additions": additions,
        "deletions": deletions,
        "total_churn": total_churn,
        "total_lines_original": len(lines_a),
        "total_lines_modified": len(lines_b),
        "diff_text": "".join(diff)
    }

def verify_blast_radius(file_a, file_b, max_churn=50, max_churn_pct=25.0):
    metrics = calculate_diff_metrics(file_a, file_b)
    if not metrics:
        return False

    orig_lines = max(1, metrics["total_lines_original"])
    churn_pct = (metrics["total_churn"] / orig_lines) * 100.0

    print(f"--- Blast Radius Analysis ---")
    print(f"Original Lines: {metrics['total_lines_original']}")
    print(f"Modified Lines: {metrics['total_lines_modified']}")
    print(f"Additions: +{metrics['additions']}")
    print(f"Deletions: -{metrics['deletions']}")
    print(f"Total Churn: {metrics['total_churn']} lines ({churn_pct:.1f}%)")

    violations = []
    if metrics["total_churn"] > max_churn and churn_pct > max_churn_pct:
        violations.append(f"Total churn ({metrics['total_churn']} lines, {churn_pct:.1f}%) exceeds thresholds (max: {max_churn} lines, {max_churn_pct}%)")

    if violations:
        print("\n❌ BLAST RADIUS VIOLATION DETECTED:", file=sys.stderr)
        for v in violations:
            print(f"  - {v}", file=sys.stderr)
        return False

    print("\n✅ Blast Radius Check Passed: Changes are well-contained.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Diff Verifier & Blast Radius Guard")
    parser.add_argument("original_file", help="Path to original / backup file")
    parser.add_argument("modified_file", help="Path to modified file")
    parser.add_argument("--max-churn", type=int, default=50, help="Maximum allowed line churn (default: 50)")
    parser.add_argument("--max-churn-pct", type=float, default=25.0, help="Maximum allowed churn percentage (default: 25.0)")
    parser.add_argument("--show-diff", action="store_true", help="Print unified diff output")

    args = parser.parse_args()

    passed = verify_blast_radius(args.original_file, args.modified_file, args.max_churn, args.max_churn_pct)

    if args.show_diff:
        metrics = calculate_diff_metrics(args.original_file, args.modified_file)
        if metrics and metrics["diff_text"]:
            print("\n--- Unified Diff ---")
            print(metrics["diff_text"])

    if not passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
