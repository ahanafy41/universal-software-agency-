#!/usr/bin/env python3
"""
Blast Radius & Code Preservation Verifier
Compares the modified file against a backup snapshot to enforce the zero-corruption invariant.
"""
import os
import sys
import difflib
import json
import argparse

def compute_diff(original_file, modified_file, max_allowed_churn_percent=30.0):
    if not os.path.exists(original_file):
        return {"success": False, "error": f"Original file not found: {original_file}"}
    if not os.path.exists(modified_file):
        return {"success": False, "error": f"Modified file not found: {modified_file}"}

    with open(original_file, 'r', encoding='utf-8', errors='replace') as f:
        orig_lines = f.readlines()
    with open(modified_file, 'r', encoding='utf-8', errors='replace') as f:
        mod_lines = f.readlines()

    diff = list(difflib.unified_diff(
        orig_lines, mod_lines,
        fromfile='snapshot_original',
        tofile='current_modified',
        lineterm=''
    ))

    added_count = 0
    removed_count = 0
    for line in diff:
        if line.startswith('+') and not line.startswith('+++'):
            added_count += 1
        elif line.startswith('-') and not line.startswith('---'):
            removed_count += 1

    total_changed = added_count + removed_count
    total_original = max(len(orig_lines), 1)
    churn_percent = (total_changed / total_original) * 100.0
    within_bounds = churn_percent <= max_allowed_churn_percent

    return {
        "success": True,
        "original_file": original_file,
        "modified_file": modified_file,
        "original_line_count": len(orig_lines),
        "modified_line_count": len(mod_lines),
        "lines_added": added_count,
        "lines_removed": removed_count,
        "total_changed_lines": total_changed,
        "churn_percent": round(churn_percent, 2),
        "max_allowed_churn_percent": max_allowed_churn_percent,
        "within_blast_radius": within_bounds,
        "diff_snippet": diff[:40]
    }

def main():
    parser = argparse.ArgumentParser(description="Blast Radius & Code Diff Verifier")
    parser.add_argument("original_path", help="Original snapshot file path")
    parser.add_argument("modified_path", help="Modified active file path")
    parser.add_argument("--max-churn", type=float, default=30.0, help="Maximum allowed change churn percentage (default: 30.0)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args()

    res = compute_diff(args.original_path, args.modified_path, args.max_churn)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        if not res.get("success"):
            print(f"[FAIL] Error: {res.get('error')}")
            sys.exit(1)

        if res["within_blast_radius"]:
            print(f"[PASS] Diff audit passed: {res['churn_percent']}% churn ({res['total_changed_lines']} changed lines <= {args.max_churn}% threshold).")
        else:
            print(f"[ALERT] Blast radius exceeded: {res['churn_percent']}% churn exceeds maximum threshold of {args.max_churn}%.")
            print("Diff sample:")
            for line in res["diff_snippet"][:20]:
                print(f"  {line}")

    sys.exit(0 if res.get("within_blast_radius") else 1)

if __name__ == '__main__':
    main()
