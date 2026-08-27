#!/usr/bin/env python3
"""
AST & Code Quality Validator with JSON Manifest Coverage Verification
Part of the Universal Software & AI Engineering Agency Toolset
"""

import os
import sys
import ast
import json
import argparse
import re

def validate_python_ast(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    try:
        ast.parse(content, filename=file_path)
        return True, "AST syntax check passed."
    except SyntaxError as e:
        return False, f"SyntaxError at line {e.lineno}, col {e.offset}: {e.msg}"

def check_placeholders(file_path):
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    
    placeholder_pattern = re.compile(r'\b(TODO|FIXME|PLACEHOLDER|TBD|IMPLEMENT_HERE)\b', re.IGNORECASE)
    findings = []
    for idx, line in enumerate(lines, start=1):
        match = placeholder_pattern.search(line)
        if match:
            findings.append((idx, match.group(0), line.strip()))
    return findings

def validate_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
        return True, "Valid JSON."
    except Exception as e:
        return False, f"Invalid JSON: {e}"

def verify_manifest_coverage(manifest_path, target_code_path):
    if not os.path.exists(manifest_path) or not os.path.exists(target_code_path):
        return False, "Manifest or target code file missing."
    
    with open(manifest_path, "r", encoding="utf-8") as f:
        try:
            manifest = json.load(f)
        except Exception as e:
            return False, f"Could not parse manifest JSON: {e}"
            
    with open(target_code_path, "r", encoding="utf-8", errors="replace") as f:
        code_text = f.read()

    symbols = manifest.get("symbols", [])
    missing = []
    for sym in symbols:
        sym_name = sym.get("name")
        if sym_name and sym_name not in code_text:
            missing.append(sym_name)

    if missing:
        return False, f"Missing {len(missing)} symbols from manifest: {', '.join(missing[:5])}..."
    return True, f"All {len(symbols)} manifest symbols verified."

def main():
    parser = argparse.ArgumentParser(description="Universal Code & AST Validator")
    parser.add_argument("target", help="Target file or directory to validate")
    parser.add_argument("--strict", action="store_true", help="Disallow placeholders and enforce strict AST parsing")
    parser.add_argument("--manifest", help="Path to references_manifest.json to verify symbol coverage")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    results = {
        "target": args.target,
        "valid": True,
        "errors": [],
        "warnings": []
    }

    target = args.target
    if os.path.isfile(target):
        files_to_check = [target]
    else:
        files_to_check = []
        for root, _, files in os.walk(target):
            for file in files:
                files_to_check.append(os.path.join(root, file))

    for file_path in files_to_check:
        if file_path.endswith(".py"):
            ok, msg = validate_python_ast(file_path)
            if not ok:
                results["valid"] = False
                results["errors"].append(f"{file_path}: {msg}")
        elif file_path.endswith(".json"):
            ok, msg = validate_json_file(file_path)
            if not ok:
                results["valid"] = False
                results["errors"].append(f"{file_path}: {msg}")

        if args.strict:
            placeholders = check_placeholders(file_path)
            for lineno, kw, linetext in placeholders:
                results["valid"] = False
                results["errors"].append(f"{file_path}:{lineno}: Forbidden placeholder '{kw}' found -> '{linetext}'")

    if args.manifest and os.path.isfile(target):
        ok, msg = verify_manifest_coverage(args.manifest, target)
        if not ok:
            results["valid"] = False
            results["errors"].append(f"Manifest Coverage: {msg}")
        else:
            results["warnings"].append(f"Manifest Coverage: {msg}")

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        if results["valid"]:
            print(f"✅ Validation PASSED for {args.target}")
            for w in results["warnings"]:
                print(f"  ℹ️ {w}")
        else:
            print(f"❌ Validation FAILED for {args.target}:", file=sys.stderr)
            for err in results["errors"]:
                print(f"  - {err}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
