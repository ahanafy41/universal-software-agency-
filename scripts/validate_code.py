#!/usr/bin/env python3
"""
validate_code.py - Multi-Language AST, Schema, Bracket & Senior Craftsmanship Validator
Part of Universal Software & AI Engineering Agency
"""

import sys
import os
import ast
import json
import re
import argparse

def validate_python_ast(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        ast.parse(source, filename=file_path)
        return True, "Valid Python AST."
    except SyntaxError as e:
        return False, f"Python SyntaxError in {file_path}:{e.lineno}:{e.offset} - {e.msg}"
    except Exception as e:
        return False, f"Failed to parse Python file {file_path}: {e}"

def validate_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
        return True, "Valid JSON."
    except json.JSONDecodeError as e:
        return False, f"JSONDecodeError in {file_path}:{e.lineno}:{e.colno} - {e.msg}"
    except Exception as e:
        return False, f"Failed to parse JSON file {file_path}: {e}"

def check_placeholders(file_path):
    issues = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for idx, line in enumerate(f, 1):
            if re.search(r"\b(TODO|FIXME|XXX|HACK)\b", line):
                issues.append(f"Line {idx}: Placeholder found: {line.strip()}")
    return issues

def main():
    parser = argparse.ArgumentParser(description="Universal Code & Craftsmanship Validator")
    parser.add_argument("files", nargs="+", help="Files to validate")
    parser.add_argument("--strict", action="store_true", help="Fail on placeholders")
    parser.add_argument("--json", action="store_true", help="Output JSON results")
    args = parser.parse_args()

    results = {"valid": True, "files": {}}

    for file_path in args.files:
        if not os.path.exists(file_path):
            results["valid"] = False
            results["files"][file_path] = {"valid": False, "error": "File does not exist."}
            continue

        ext = os.path.splitext(file_path)[1].lower()
        file_valid = True
        msg = "OK"

        if ext == ".py":
            file_valid, msg = validate_python_ast(file_path)
        elif ext == ".json":
            file_valid, msg = validate_json_file(file_path)

        placeholders = check_placeholders(file_path)
        if args.strict and placeholders:
            file_valid = False
            msg = f"{msg} | Placeholders detected: {len(placeholders)}"

        if not file_valid:
            results["valid"] = False

        results["files"][file_path] = {
            "valid": file_valid,
            "message": msg,
            "placeholders": placeholders
        }

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for f, res in results["files"].items():
            status = "✅ PASS" if res["valid"] else "❌ FAIL"
            print(f"[{status}] {f}: {res['message']}")

    sys.exit(0 if results["valid"] else 1)

if __name__ == "__main__":
    main()
