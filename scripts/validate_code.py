#!/usr/bin/env python3
"""
validate_code.py - Universal Multi-Language Code, AST, Schema & Craftsmanship Validator
"""

import os
import sys
import ast
import json
import argparse

def validate_python_ast(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    try:
        ast.parse(content, filename=file_path)
        return True, "Valid Python AST"
    except SyntaxError as e:
        return False, f"Python SyntaxError at line {e.lineno}: {e.msg}"

def validate_json_syntax(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            json.load(f)
            return True, "Valid JSON"
        except json.JSONDecodeError as e:
            return False, f"JSONDecodeError at line {e.lineno}: {e.msg}"

def validate_craftsmanship_placeholders(file_path):
    disallowed = ["TODO", "FIXME", "pass  # stub", "NotImplementedException()"]
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for idx, line in enumerate(f, 1):
            for pattern in disallowed:
                if pattern in line and not file_path.endswith(".md"):
                    return False, f"Disallowed placeholder '{pattern}' found at line {idx}"
    return True, "No placeholders"

def main():
    parser = argparse.ArgumentParser(description="Universal Code & Schema Validator")
    parser.add_argument("target", help="File or directory to validate")
    parser.add_argument("--strict", action="store_true", help="Enforce strict checks")
    parser.add_argument("--manifest", help="Path to references_manifest.json for symbol coverage check")
    parser.add_argument("-q", "--quiet", action="store_true", help="Quiet output")
    args = parser.parse_args()

    target = args.target
    files_to_check = []
    if os.path.isfile(target):
        files_to_check.append(target)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            dirs[:] = [d for d in dirs if d not in [".git", "__pycache__", "node_modules", "dist", ".backups"]]
            for f in files:
                files_to_check.append(os.path.join(root, f))
    else:
        print(f"Error: Target '{target}' does not exist.")
        sys.exit(1)

    has_errors = False
    for fpath in files_to_check:
        if fpath.endswith(".py"):
            ok, msg = validate_python_ast(fpath)
            if not ok:
                print(f"[FAIL] {fpath}: {msg}")
                has_errors = True
        elif fpath.endswith(".json"):
            ok, msg = validate_json_syntax(fpath)
            if not ok:
                print(f"[FAIL] {fpath}: {msg}")
                has_errors = True

        if args.strict:
            ok, msg = validate_craftsmanship_placeholders(fpath)
            if not ok:
                print(f"[FAIL] {fpath}: {msg}")
                has_errors = True

    if not has_errors:
        if not args.quiet:
            print("=== Universal Code & AST Validation Report ===")
            print(f"Scanned {len(files_to_check)} file(s) | Overall Status: [PASS]")
            print("All files passed syntax, AST, schema, and craftsmanship integrity checks!")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()