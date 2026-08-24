#!/usr/bin/env python3
"""
Universal Multi-Language AST, Syntax & Structure Validator
Validates Python (ast.parse), JSON (json.loads), YAML (yaml.safe_load),
Shell (bash -n), Node.js (node --check), and performs line-aware bracket balancing.
"""
import sys
import os
import ast
import json
import argparse
import subprocess
import shutil

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

FORBIDDEN_PLACEHOLDERS = [
    'TODO', 'FIXME', 'PLACEHOLDER', 'YOUR_CODE_HERE',
    'pass  # implement', 'throw new NotImplementedException()',
    'todo!()', 'unimplemented!()'
]

def check_strict_placeholders(content):
    findings = []
    lines = content.splitlines()
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith(('#', '//', '--', '/*', '*')):
            continue
        for ph in FORBIDDEN_PLACEHOLDERS:
            if ph in line:
                findings.append({
                    "line": idx,
                    "column": line.find(ph) + 1,
                    "message": f"Forbidden placeholder/stub detected: '{ph}'",
                    "type": "StrictQualityWarning"
                })
    return findings

def validate_python_ast(content, filename):
    errors = []
    try:
        ast.parse(content, filename=filename)
    except SyntaxError as e:
        errors.append({
            "line": e.lineno or 1,
            "column": e.offset or 1,
            "message": f"Python SyntaxError: {e.msg}",
            "type": "SyntaxError"
        })
    except Exception as e:
        errors.append({
            "line": 1,
            "column": 1,
            "message": f"Python AST Parse Error: {str(e)}",
            "type": "ParseException"
        })
    return errors

def validate_json_strict(content):
    errors = []
    try:
        json.loads(content)
    except json.JSONDecodeError as e:
        errors.append({
            "line": e.lineno,
            "column": e.colno,
            "message": f"JSON Decode Error: {e.msg}",
            "type": "JSONDecodeError"
        })
    return errors

def validate_yaml_strict(content):
    if not HAS_YAML:
        return []
    errors = []
    try:
        yaml.safe_load(content)
    except yaml.YAMLError as e:
        mark = getattr(e, 'problem_mark', None)
        line = mark.line + 1 if mark else 1
        col = mark.column + 1 if mark else 1
        errors.append({
            "line": line,
            "column": col,
            "message": f"YAML Syntax Error: {str(e)}",
            "type": "YAMLError"
        })
    return errors

def validate_external_compiler(cmd, file_path):
    errors = []
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if proc.returncode != 0:
            err_msg = proc.stderr.strip() or proc.stdout.strip()
            errors.append({
                "line": 1,
                "column": 1,
                "message": f"Compiler check failed: {err_msg}",
                "type": "CompilerError"
            })
    except Exception as e:
        errors.append({
            "line": 1,
            "column": 1,
            "message": f"Execution error running compiler check: {str(e)}",
            "type": "ExecutionError"
        })
    return errors

def validate_line_aware_brackets(content):
    errors = []
    pairs = {'{': '}', '(': ')', '[': ']'}
    closing = {v: k for k, v in pairs.items()}
    stack = []

    in_single_quote = False
    in_double_quote = False
    in_backtick = False
    in_line_comment = False
    in_block_comment = False

    lines = content.splitlines()
    for line_idx, line in enumerate(lines, 1):
        in_line_comment = False
        i = 0
        n = len(line)
        while i < n:
            c = line[i]
            nxt = line[i+1] if i + 1 < n else ''

            if in_block_comment:
                if c == '*' and nxt == '/':
                    in_block_comment = False
                    i += 2
                    continue
                i += 1
                continue

            if in_line_comment:
                break

            if not (in_single_quote or in_double_quote or in_backtick):
                if c == '/' and nxt == '/':
                    in_line_comment = True
                    break
                if c == '/' and nxt == '*':
                    in_block_comment = True
                    i += 2
                    continue
                if c == '#' or (c == '-' and nxt == '-'):
                    in_line_comment = True
                    break

            if c == '\\' and (in_single_quote or in_double_quote or in_backtick):
                i += 2
                continue

            if c == "'" and not (in_double_quote or in_backtick):
                in_single_quote = not in_single_quote
                i += 1
                continue

            if c == '"' and not (in_single_quote or in_backtick):
                in_double_quote = not in_double_quote
                i += 1
                continue

            if c == '`' and not (in_single_quote or in_double_quote):
                in_backtick = not in_backtick
                i += 1
                continue

            if not (in_single_quote or in_double_quote or in_backtick):
                if c in pairs:
                    stack.append((c, line_idx, i + 1))
                elif c in closing:
                    if not stack:
                        errors.append({
                            "line": line_idx,
                            "column": i + 1,
                            "message": f"Unmatched closing bracket '{c}' without corresponding '{closing[c]}'",
                            "type": "BracketMismatchError"
                        })
                    else:
                        top_bracket, top_line, top_col = stack.pop()
                        if pairs[top_bracket] != c:
                            errors.append({
                                "line": line_idx,
                                "column": i + 1,
                                "message": f"Mismatched closing bracket '{c}', expected '{pairs[top_bracket]}' (opened at line {top_line}, col {top_col})",
                                "type": "BracketMismatchError"
                            })

            i += 1

    while stack:
        unclosed, open_line, open_col = stack.pop()
        errors.append({
            "line": open_line,
            "column": open_col,
            "message": f"Unclosed opening bracket '{unclosed}' at end of file",
            "type": "UnclosedBracketError"
        })

    return errors

def validate_file(file_path, strict_mode=False):
    if not os.path.exists(file_path):
        return {
            "success": False,
            "file": file_path,
            "language": "unknown",
            "errors": [{"line": 0, "column": 0, "message": f"File not found: {file_path}", "type": "FileNotFound"}],
            "warnings": [],
            "line_count": 0
        }

    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    ext = os.path.splitext(file_path)[1].lower()
    errors = []
    lang = "unknown"

    if ext == '.py':
        lang = "python"
        errors = validate_python_ast(content, file_path)
    elif ext == '.json':
        lang = "json"
        errors = validate_json_strict(content)
    elif ext in ['.yaml', '.yml']:
        lang = "yaml"
        errors = validate_yaml_strict(content)
    elif ext == '.sh' and shutil.which('bash'):
        lang = "shell"
        errors = validate_external_compiler(['bash', '-n', file_path], file_path)
    elif ext in ['.js', '.mjs'] and shutil.which('node'):
        lang = "javascript"
        errors = validate_external_compiler(['node', '--check', file_path], file_path)
    else:
        lang = ext.lstrip('.') or "plain"
        errors = validate_line_aware_brackets(content)

    warnings = check_strict_placeholders(content) if strict_mode else []
    success = (len(errors) == 0) and (len(warnings) == 0 if strict_mode else True)

    return {
        "success": success,
        "file": file_path,
        "language": lang,
        "errors": errors,
        "warnings": warnings,
        "line_count": len(content.splitlines())
    }

def main():
    parser = argparse.ArgumentParser(description="Universal Multi-Language AST & Code Validator")
    parser.add_argument("file_path", help="Path to file to validate")
    parser.add_argument("--json", action="store_true", help="Output result in structured JSON")
    parser.add_argument("--strict", action="store_true", help="Fail on placeholders, TODOs, or stubs")
    args = parser.parse_args()

    res = validate_file(args.file_path, strict_mode=args.strict)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        if res["success"]:
            print(f"[PASS] {res['language'].upper()}: {res['file']} ({res['line_count']} lines)")
        else:
            print(f"[FAIL] Validation failed for {res['file']} ({res['language'].upper()}):")
            for err in res["errors"]:
                print(f"  Line {err.get('line')}, Col {err.get('column')}: [{err.get('type')}] {err.get('message')}")
            for warn in res["warnings"]:
                print(f"  Line {warn.get('line')}, Col {warn.get('column')}: [{warn.get('type')}] {warn.get('message')}")

    sys.exit(0 if res["success"] else 1)

if __name__ == '__main__':
    main()
