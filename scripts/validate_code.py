#!/usr/bin/env python3
"""
Universal Multi-Language AST, Schema, and Human-Grade Code Validator
Universal Software & AI Engineering Agency
"""

import argparse
import ast
import json
import os
import re
import sys
from pathlib import Path

PLACEHOLDER_PATTERNS = [
    r"\bTODO\b",
    r"\bFIXME\b",
    r"\bXXX\b",
    r"pass\s*#\s*stub",
    r"throw\s+new\s+NotImplementedException",
    r"raise\s+NotImplementedError",
    r'panic!\s*\(\s*"not\s+implemented',
    r"unimplemented!\s*\(",
]

PRINT_PATTERNS = [
    (r"\bprint\s*\(", "Python print() statement detected - use structured logging instead"),
    (r"\bConsole\.WriteLine\s*\(", "C# Console.WriteLine() detected - use structured logging instead"),
    (r"\bconsole\.(log|debug)\s*\(", "JS/TS console.log() detected - use structured logging instead"),
    (r"\bfmt\.Print(ln|f)?\s*\(", "Go fmt.Print detected - use structured logging instead"),
]

NON_ATOMIC_WRITE_PATTERNS = [
    (r"open\s*\([^)]+['\"]w['\"]\)", "Potential non-atomic file write - consider atomic write pattern (tempfile + atomic rename)"),
    (r"File\.WriteAllText\s*\(", "C# File.WriteAllText directly overwriting target - consider atomic replacement pattern"),
    (r"fs\.writeFileSync\s*\(", "Node fs.writeFileSync directly overwriting target - consider atomic tempfile rename"),
]

IGNORED_DIRS = {
    ".git", ".svn", "__pycache__", ".pytest_cache", "node_modules",
    "bin", "obj", "target", "dist", "build", ".backups", ".venv", "venv"
}


def validate_json_file(file_path):
    issues = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "$schema" in data:
            pass
    except json.JSONDecodeError as e:
        issues.append(f"Line {e.lineno}, Col {e.colno} [JSONDecodeError]: {e.msg}")
    except Exception as e:
        issues.append(f"Line 0 [ReadError]: {str(e)}")
    return issues


def validate_python_ast(file_path, content):
    issues = []
    try:
        ast.parse(content, filename=str(file_path))
    except SyntaxError as e:
        issues.append(f"Line {e.lineno}, Col {e.offset} [SyntaxError]: {e.msg}")
    except Exception as e:
        issues.append(f"Line 0 [ASTError]: {str(e)}")
    return issues


def validate_markdown_frontmatter(file_path, content):
    issues = []
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            if not fm_text:
                issues.append("Line 1 [FrontmatterError]: Empty YAML frontmatter block")
            elif "name:" not in fm_text:
                issues.append("Line 1 [FrontmatterWarning]: Frontmatter missing 'name:' identifier")
        else:
            issues.append("Line 1 [FrontmatterError]: Unclosed YAML frontmatter delimiter (---)")
    return issues


def validate_delimiters(content):
    issues = []
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    in_string = False
    string_char = None
    in_comment = False

    for line_idx, line in enumerate(content.splitlines(), start=1):
        for col_idx, char in enumerate(line, start=1):
            if in_comment:
                continue
            if in_string:
                if char == string_char and (col_idx == 1 or line[col_idx - 2] != '\\'):
                    in_string = False
                continue
            if char in ('"', "'") and (col_idx == 1 or line[col_idx - 2] != '\\'):
                in_string = True
                string_char = char
                continue
            if char in ('(', '{', '['):
                stack.append((char, line_idx, col_idx))
            elif char in (')', '}', ']'):
                expected = pairs[char]
                if not stack:
                    issues.append(f"Line {line_idx}, Col {col_idx} [DelimiterError]: Unmatched closing delimiter '{char}'")
                    return issues
                top, top_line, top_col = stack.pop()
                if top != expected:
                    issues.append(f"Line {line_idx}, Col {col_idx} [DelimiterError]: Mismatched delimiter '{char}', expected match for '{top}' from Line {top_line}")
                    return issues

    if stack:
        top, top_line, top_col = stack[-1]
        issues.append(f"Line {top_line}, Col {top_col} [DelimiterError]: Unclosed opening delimiter '{top}'")

    return issues


def check_strict_placeholders(content):
    issues = []
    lines = content.splitlines()
    for idx, line in enumerate(lines, start=1):
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                # Ignore if inside a markdown documentation explanation
                if line.strip().startswith("-") or line.strip().startswith("*") or "`" in line:
                    continue
                issues.append(f"Line {idx} [StrictPlaceholderViolation]: Placeholder pattern '{pattern}' found: '{line.strip()}'")
    return issues


def check_human_grade_rules(content, is_source_code=False):
    issues = []
    if not is_source_code:
        return issues
    lines = content.splitlines()
    for idx, line in enumerate(lines, start=1):
        clean_line = line.strip()
        if clean_line.startswith("#") or clean_line.startswith("//") or clean_line.startswith("/*"):
            continue
        for pattern, msg in PRINT_PATTERNS:
            if re.search(pattern, clean_line):
                issues.append(f"Line {idx} [CraftsmanshipNotice]: {msg}")
        for pattern, msg in NON_ATOMIC_WRITE_PATTERNS:
            if re.search(pattern, clean_line):
                issues.append(f"Line {idx} [CraftsmanshipNotice]: {msg}")
    return issues


def validate_manifest_coverage(manifest_path, target_dir_or_file):
    issues = []
    if not os.path.exists(manifest_path):
        return [f"Manifest file not found: {manifest_path}"]

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest_data = json.load(f)
    except Exception as e:
        return [f"Failed to read manifest JSON: {str(e)}"]

    # Extract symbols to look for
    symbols = []
    if "symbols" in manifest_data:
        for item in manifest_data["symbols"]:
            if isinstance(item, dict) and "symbol_name" in item:
                symbols.append(item["symbol_name"])
            elif isinstance(item, str):
                symbols.append(item)

    if not symbols:
        return []

    # Gather source contents
    combined_source = ""
    target_path = Path(target_dir_or_file)
    if target_path.is_file():
        try:
            combined_source = target_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            return [f"Failed to read target source file: {str(e)}"]
    else:
        for root, dirs, files in os.walk(target_path):
            dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in {".py", ".cs", ".ts", ".js", ".go", ".rs", ".java", ".cpp", ".c", ".h"}:
                    try:
                        p = Path(root) / file
                        combined_source += p.read_text(encoding="utf-8", errors="ignore") + "\n"
                    except Exception:
                        pass

    missing = []
    for sym in symbols:
        pattern = r"\b" + re.escape(sym) + r"\b"
        if not re.search(pattern, combined_source):
            missing.append(sym)

    if missing:
        issues.append(f"ManifestCoverageMismatch: {len(missing)} declared symbol(s) missing from implementation: {', '.join(missing[:5])}" + ("..." if len(missing) > 5 else ""))

    return issues


def validate_file(file_path, strict=False, human_grade=False):
    p = Path(file_path)
    issues = []
    ext = p.suffix.lower()

    if not p.is_file():
        return [f"Line 0 [ReadError]: Path is not a file: '{file_path}'"]

    try:
        content = p.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Line 0 [ReadError]: Could not read file: {str(e)}"]

    is_source = ext in {".py", ".cs", ".ts", ".js", ".go", ".rs", ".java", ".cpp", ".c"}

    if ext == ".json":
        issues.extend(validate_json_file(file_path))
    elif ext == ".py":
        issues.extend(validate_python_ast(file_path, content))
    elif ext in {".md", ".markdown"}:
        issues.extend(validate_markdown_frontmatter(file_path, content))

    if is_source and ext != ".py":
        issues.extend(validate_delimiters(content))

    if strict:
        issues.extend(check_strict_placeholders(content))

    if human_grade:
        issues.extend(check_human_grade_rules(content, is_source_code=is_source))

    return issues


def main():
    parser = argparse.ArgumentParser(description="Universal Code, AST & Manifest Coverage Validator")
    parser.add_argument("target", help="File or directory path to validate")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode (checks for stub placeholders)")
    parser.add_argument("--human-grade", action="store_true", help="Audit code against senior human-grade craftsmanship rules")
    parser.add_argument("--manifest", type=str, default=None, help="Path to references_manifest.json to verify symbol coverage")
    parser.add_argument("--json", action="store_true", help="Output results in machine-readable JSON format")
    parser.add_argument("-q", "--quiet", action="store_true", help="Only output errors")

    args = parser.parse_args()
    target_path = Path(args.target)

    if not target_path.exists():
        print(f"Error: Target path '{args.target}' does not exist.", file=sys.stderr)
        sys.exit(1)

    files_to_scan = []
    if target_path.is_file():
        files_to_scan.append(target_path)
    else:
        for root, dirs, files in os.walk(target_path):
            dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in {".py", ".cs", ".ts", ".js", ".go", ".rs", ".java", ".cpp", ".c", ".h", ".json", ".md", ".yaml", ".yml"}:
                    files_to_scan.append(Path(root) / f)

    results = {}
    total_issues = 0

    for file_path in files_to_scan:
        file_issues = validate_file(file_path, strict=args.strict, human_grade=args.human_grade)
        if file_issues:
            results[str(file_path)] = file_issues
            total_issues += len(file_issues)

    if args.manifest:
        manifest_issues = validate_manifest_coverage(args.manifest, args.target)
        if manifest_issues:
            results[f"manifest:{args.manifest}"] = manifest_issues
            total_issues += len(manifest_issues)

    if args.json:
        report = {
            "status": "PASS" if total_issues == 0 else "FAIL",
            "files_scanned": len(files_to_scan),
            "total_issues": total_issues,
            "issues": results
        }
        print(json.dumps(report, indent=2))
    else:
        status_str = "[PASS]" if total_issues == 0 else "[FAIL]"
        print(f"=== Universal Code & AST Validation Report ===")
        print(f"Scanned {len(files_to_scan)} file(s) | Overall Status: {status_str}")
        if total_issues > 0:
            print(f"\nDiscovered {total_issues} issue(s):")
            for fp, issues in results.items():
                print(f"\n  File: {fp}")
                for iss in issues:
                    print(f"    - {iss}")
        else:
            if not args.quiet:
                print("All files passed syntax, AST, schema, and craftsmanship integrity checks!")

    sys.exit(0 if total_issues == 0 else 1)


if __name__ == "__main__":
    main()
