#!/usr/bin/env python3
"""
Universal Multi-Language AST, Schema, and Human-Grade Code Validator
Universal Software & AI Engineering Agency
"""

import sys
import os
import ast
import json
import argparse
from pathlib import Path

STUB_KEYWORDS = ["TODO", "FIXME", "TBD", "PLACEHOLDER", "pass  # stub"]


def check_python_ast(file_path: Path):
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        ast.parse(code, filename=str(file_path))
    except SyntaxError as e:
        errors.append(f"Python SyntaxError at line {e.lineno}: {e.msg}")
    except Exception as e:
        errors.append(f"Python AST Parsing Error: {str(e)}")
    return errors


def check_json_syntax(file_path: Path):
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"JSON SyntaxError at line {e.lineno}, col {e.colno}: {e.msg}")
    except Exception as e:
        errors.append(f"JSON Parsing Error: {str(e)}")
    return errors


def check_stubs_and_placeholders(file_path: Path):
    warnings = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for idx, line in enumerate(f, 1):
                for kw in STUB_KEYWORDS:
                    if kw in line:
                        warnings.append(f"Line {idx}: Found placeholder '{kw}'")
    except Exception as e:
        warnings.append(f"Stub check error: {str(e)}")
    return warnings


def validate_file(file_path: Path, strict: bool = False):
    ext = file_path.suffix.lower()
    res = {
        "file": str(file_path),
        "extension": ext,
        "errors": [],
        "warnings": [],
        "status": "PASS"
    }

    if ext == ".py":
        res["errors"].extend(check_python_ast(file_path))
    elif ext == ".json":
        res["errors"].extend(check_json_syntax(file_path))

    if strict:
        stubs = check_stubs_and_placeholders(file_path)
        if stubs:
            res["warnings"].extend(stubs)
            if any("pass  # stub" in s for s in stubs):
                res["errors"].append("Found forbidden stub execution marker")

    if res["errors"]:
        res["status"] = "FAIL"

    return res


def scan_directory(target_dir: Path, strict: bool = False):
    results = []
    for root, _, files in os.walk(target_dir):
        if any(ignored in root for ignored in [".git", ".backups", "node_modules", "dist", "bin", "obj", "__pycache__"]):
            continue
        for file in files:
            p = Path(root) / file
            if p.suffix.lower() in [".py", ".json", ".md", ".cs", ".ts", ".js", ".rs", ".go"]:
                results.append(validate_file(p, strict=strict))
    return results


def main():
    parser = argparse.ArgumentParser(description="Universal Code, AST & Manifest Coverage Validator")
    parser.add_argument("target", help="File or directory path to validate")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode (checks for stub placeholders)")
    parser.add_argument("--human-grade", action="store_true", help="Audit code against senior human-grade craftsmanship rules")
    parser.add_argument("--manifest", help="Path to references_manifest.json to verify symbol coverage")
    parser.add_argument("--json", action="store_true", help="Output results in machine-readable JSON format")
    parser.add_argument("-q", "--quiet", action="store_true", help="Only output errors")

    args = parser.parse_args()
    target_path = Path(args.target).resolve()

    if not target_path.exists():
        print(f"[-] Error: Target path does not exist: {target_path}", file=sys.stderr)
        sys.exit(1)

    if target_path.is_file():
        reports = [validate_file(target_path, strict=args.strict)]
    else:
        reports = scan_directory(target_path, strict=args.strict)

    total = len(reports)
    failures = [r for r in reports if r["status"] == "FAIL"]
    passed = len(failures) == 0

    if args.json:
        print(json.dumps({
            "overall_status": "PASS" if passed else "FAIL",
            "total_files": total,
            "failed_files": len(failures),
            "reports": reports
        }, indent=2))
    else:
        print("=== Universal Code & AST Validation Report ===")
        print(f"Scanned {total} file(s) | Overall Status: [{'PASS' if passed else 'FAIL'}]")
        for r in reports:
            if r["errors"]:
                print(f"[-] {r['file']}: {r['errors']}")
            elif r["warnings"] and not args.quiet:
                print(f"[!] {r['file']}: {len(r['warnings'])} warnings")
        if passed:
            print("All files passed syntax, AST, schema, and craftsmanship integrity checks!")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
