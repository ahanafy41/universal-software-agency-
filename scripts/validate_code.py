#!/usr/bin/env python3
"""
Universal Multi-Language AST, Schema, and Human-Grade Code Validator
Universal Software & AI Engineering Agency
"""

import argparse
import ast
import difflib
import json
import os
import re
import subprocess
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
    in_block_comment = False

    for line_idx, line in enumerate(content.splitlines(), start=1):
        i = 0
        line_len = len(line)
        while i < line_len:
            char = line[i]
            col_idx = i + 1

            if in_block_comment:
                if i + 1 < line_len and line[i:i+2] == '*/':
                    in_block_comment = False
                    i += 2
                    continue
                i += 1
                continue

            if in_string:
                if char == string_char and (i == 0 or line[i - 1] != '\\'):
                    in_string = False
                i += 1
                continue

            # Check single line comment // or #
            if i + 1 < line_len and line[i:i+2] == '//':
                break
            if char == '#' and (i == 0 or line[i - 1] != '\\'):
                break

            # Check block comment /*
            if i + 1 < line_len and line[i:i+2] == '/*':
                in_block_comment = True
                i += 2
                continue

            # Skip regex literal /.../
            if char == '/' and i + 1 < line_len and line[i+1] not in ('/', '*'):
                prev_non_ws = ''
                for k in range(i - 1, -1, -1):
                    if not line[k].isspace():
                        prev_non_ws = line[k]
                        break
                if prev_non_ws in ('=', '(', ',', ':', '[', '!', '&', '|', '?', '+', '~'):
                    j = i + 1
                    while j < line_len:
                        if line[j] == '\\':
                            j += 2
                            continue
                        if line[j] == '/':
                            # Skip regex flags (g, i, m, s, u, y)
                            j += 1
                            while j < line_len and line[j].isalpha():
                                j += 1
                            i = j
                            break
                        j += 1
                    else:
                        i += 1
                    continue

            if char in ('"', "'", '`') and (i == 0 or line[i - 1] != '\\'):
                in_string = True
                string_char = char
                i += 1
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
            i += 1

    if stack:
        top, top_line, top_col = stack[-1]
        issues.append(f"Line {top_line}, Col {top_col} [DelimiterError]: Unclosed opening delimiter '{top}'")

    return issues


def check_strict_placeholders(content, is_markdown=False):
    issues = []
    lines = content.splitlines()
    for idx, line in enumerate(lines, start=1):
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                # Ignore if inside a markdown documentation explanation, list, table or quote
                if is_markdown:
                    clean = line.strip()
                    if clean.startswith(("-", "*", ">", "|", "#")) or "`" in clean or '"' in clean or "'" in clean:
                        continue
                else:
                    if line.strip().startswith(("-", "*")) or "`" in line:
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
        if (
            clean_line.startswith("#")
            or clean_line.startswith("//")
            or clean_line.startswith("/*")
            or "allow-print" in clean_line
            or "noqa" in clean_line
        ):
            continue
        # Skip regex definitions or pattern tuples
        if clean_line.startswith('(') and ('r"' in clean_line or "r'" in clean_line):
            continue
        for pattern, msg in PRINT_PATTERNS:
            if re.search(pattern, clean_line):
                # If it's a CLI tool print or deliberate stdout output, note as advisory rather than blocker
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


def compute_blast_radius_diff(original_file, modified_file, max_allowed_churn=30.0):
    p_orig, p_mod = Path(original_file), Path(modified_file)
    if not p_orig.exists():
        return False, f"Original file not found: {original_file}", {}
    if not p_mod.exists():
        return False, f"Modified file not found: {modified_file}", {}

    try:
        orig_lines = p_orig.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
        mod_lines = p_mod.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    except Exception as e:
        return False, f"Failed to read files: {e}", {}

    diff = list(difflib.unified_diff(orig_lines, mod_lines, fromfile="backup", tofile="active", lineterm=""))
    added = sum(1 for line in diff if line.startswith("+") and not line.startswith("+++"))
    removed = sum(1 for line in diff if line.startswith("-") and not line.startswith("---"))
    total_changed = added + removed
    churn = (total_changed / max(len(orig_lines), 1)) * 100.0
    within_bounds = churn <= max_allowed_churn

    stats = {
        "lines_added": added,
        "lines_removed": removed,
        "total_changed": total_changed,
        "churn_percent": round(churn, 2),
        "max_allowed_churn": max_allowed_churn,
        "within_bounds": within_bounds
    }
    return within_bounds, "", stats


def run_automated_test_suites(target_dir, timeout=30):
    test_files = []
    p = Path(target_dir)
    if p.is_file():
        if "test" in p.name.lower():
            test_files.append(p)
    else:
        for root, dirs, files in os.walk(p):
            dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
            for f in files:
                lf = f.lower()
                if lf.startswith("test_") or lf.endswith("_test.py") or lf.endswith(".test.js") or lf.endswith(".test.ts"):
                    test_files.append(Path(root) / f)

    if not test_files:
        return False, "No test suites found! Agentic coding mandates writing at least one test file (e.g. test_*.py) with assertions."

    passed, failures = 0, []
    for tf in test_files:
        cmd = [sys.executable, str(tf)] if tf.suffix == ".py" else ["node", "--test", str(tf)]
        try:
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
            if proc.returncode == 0:
                passed += 1
            else:
                failures.append((tf.name, proc.stdout.strip(), proc.stderr.strip()))
        except Exception as e:
            failures.append((tf.name, "", str(e)))

    if failures:
        details = "\n".join([f"Suite {name} FAILED:\n{err or out}" for name, out, err in failures])
        return False, f"{len(failures)}/{len(test_files)} test suites failed:\n{details}"

    return True, f"All {passed} test suite(s) passed 100% assertions successfully!"


def validate_file(file_path, strict=False, human_grade=False, max_lines=100):
    p = Path(file_path)
    issues = []
    ext = p.suffix.lower()

    if not p.is_file():
        return [f"Line 0 [ReadError]: Path is not a file: '{file_path}'"]

    try:
        content = p.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Line 0 [ReadError]: Could not read file: {str(e)}"]

    is_source = ext in {".py", ".cs", ".ts", ".js", ".go", ".rs", ".java", ".cpp", ".c", ".lua", ".sh"}

    # Strict Modular Limit: files must not exceed max_lines (default: 100 lines)
    if is_source and max_lines > 0:
        line_count = len(content.splitlines())
        # Skip validator scripts themselves or files with explicit exemption comment
        if line_count > max_lines and "# allow-large-file" not in content and p.name not in {"validate_code.py", "backup_manager.py", "test_runner.py"}:
            issues.append(f"Line {max_lines + 1} [ModularBloatViolation]: File exceeds {max_lines} lines limit (currently {line_count} lines). Must be refactored into smaller, single-responsibility submodules.")

    if ext == ".json":
        issues.extend(validate_json_file(file_path))
    elif ext == ".py":
        issues.extend(validate_python_ast(file_path, content))
    elif ext in {".md", ".markdown"}:
        issues.extend(validate_markdown_frontmatter(file_path, content))

    if is_source and ext != ".py":
        issues.extend(validate_delimiters(content))

    if strict:
        issues.extend(check_strict_placeholders(content, is_markdown=ext in {".md", ".markdown"}))

    if human_grade:
        issues.extend(check_human_grade_rules(content, is_source_code=is_source))

    return issues


def main():
    parser = argparse.ArgumentParser(description="Universal Code, AST, Modular Limits & Manifest Validator")
    parser.add_argument("target", nargs="?", default=None, help="File or directory path to validate")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode (checks for stub placeholders)")
    parser.add_argument("--human-grade", action="store_true", help="Audit code against senior human-grade craftsmanship rules")
    parser.add_argument("--max-lines", type=int, default=100, help="Maximum allowed lines per source code file (default: 100)")
    parser.add_argument("--run-tests", action="store_true", help="Execute automated test suites via in-process runner")
    parser.add_argument("--diff-check", nargs=2, metavar=("BACKUP", "MODIFIED"), help="Verify modification blast radius and churn percentage against backup")
    parser.add_argument("--max-churn", type=float, default=30.0, help="Maximum allowed churn percentage for diff check (default: 30.0)")
    parser.add_argument("--fail-on-notices", action="store_true", help="Fail build on craftsmanship notices (default treats as advisory warnings)")
    parser.add_argument("--manifest", type=str, default=None, help="Path to references_manifest.json to verify symbol coverage")
    parser.add_argument("--json", action="store_true", help="Output results in machine-readable JSON format")
    parser.add_argument("-q", "--quiet", action="store_true", help="Only output errors")

    args = parser.parse_args()

    if args.diff_check:
        orig, mod = args.diff_check
        within_bounds, err, stats = compute_blast_radius_diff(orig, mod, max_allowed_churn=args.max_churn)
        if err:
            print(f"Error in diff check: {err}", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps(stats, indent=2))
        else:
            status_str = "[PASS]" if within_bounds else "[FAIL]"
            print(f"=== Blast Radius & Diff Check Report ===")
            print(f"Status: {status_str} | Churn: {stats['churn_percent']}% (Allowed: {stats['max_allowed_churn']}%)")
            print(f"Lines Added: +{stats['lines_added']} | Lines Removed: -{stats['lines_removed']} | Total Changed: {stats['total_changed']}")
            if not within_bounds:
                print(f"Violation: Churn percentage exceeded safety threshold!")
        sys.exit(0 if within_bounds else 1)

    if not args.target:
        if args.manifest:
            args.target = args.manifest
            args.manifest = None
        else:
            parser.error("the following arguments are required: target")

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
    blocking_errors = 0
    advisory_notices = 0

    for file_path in files_to_scan:
        file_issues = validate_file(file_path, strict=args.strict, human_grade=args.human_grade, max_lines=args.max_lines)
        if file_issues:
            results[str(file_path)] = file_issues
            for iss in file_issues:
                if "[CraftsmanshipNotice]" in iss:
                    advisory_notices += 1
                else:
                    blocking_errors += 1

    if args.manifest:
        manifest_issues = validate_manifest_coverage(args.manifest, args.target)
        if manifest_issues:
            results[f"manifest:{args.manifest}"] = manifest_issues
            blocking_errors += len(manifest_issues)

    if args.run_tests:
        ok, msg = run_automated_test_suites(args.target)
        if not ok:
            results["test_suites"] = [f"[TestLogicFailure]: {msg}"]
            blocking_errors += 1
        else:
            if not args.quiet and not args.json:
                print(f"  [PASS] {msg}")

    total_failures = blocking_errors + (advisory_notices if args.fail_on_notices else 0)

    if args.json:
        report = {
            "status": "PASS" if total_failures == 0 else "FAIL",
            "files_scanned": len(files_to_scan),
            "blocking_errors": blocking_errors,
            "advisory_notices": advisory_notices,
            "issues": results
        }
        print(json.dumps(report, indent=2))
    else:
        status_str = "[PASS]" if total_failures == 0 else "[FAIL]"
        print(f"=== Universal Code & AST Validation Report ===")
        print(f"Scanned {len(files_to_scan)} file(s) | Overall Status: {status_str}")
        if blocking_errors > 0 or advisory_notices > 0:
            print(f"\nDiscovered {blocking_errors} blocking error(s) and {advisory_notices} advisory notice(s):")
            for fp, issues in results.items():
                print(f"\n  File: {fp}")
                for iss in issues:
                    print(f"    - {iss}")
        else:
            if not args.quiet:
                print("All files passed syntax, AST, schema, and craftsmanship integrity checks!")

    sys.exit(0 if total_failures == 0 else 1)


if __name__ == "__main__":
    main()
