#!/usr/bin/env python3
# allow-large-file
"""
Code Symbol Mapper & Surgical Token Saver (v1.0)
Lightweight, zero-dependency symbol indexer and surgical navigation tool.
Supports Python (AST), Lua, JavaScript/TypeScript, Shell, and more.
"""

import sys
import os
import re
import ast
import argparse
from typing import List, Dict, Any, Optional

def estimate_tokens(text: str) -> int:
    """Rough estimation of tokens (~4 chars per token)."""
    return max(1, len(text) // 4)

def parse_python_file(content: str, filename: str) -> List[Dict[str, Any]]:
    """Parse Python code using built-in AST."""
    symbols = []
    lines = content.splitlines()
    try:
        tree = ast.parse(content, filename=filename)
    except SyntaxError:
        return parse_generic_file(content, filename, "py")

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            start = node.lineno
            end = getattr(node, "end_lineno", start)
            symbols.append({
                "type": "class",
                "name": node.name,
                "start": start,
                "end": end,
                "params": [b.id if isinstance(b, ast.Name) else "..." for b in node.bases]
            })
            for subnode in node.body:
                if isinstance(subnode, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    sub_start = subnode.lineno
                    sub_end = getattr(subnode, "end_lineno", sub_start)
                    params = [arg.arg for arg in subnode.args.args]
                    is_async = isinstance(subnode, ast.AsyncFunctionDef)
                    symbols.append({
                        "type": "method",
                        "name": f"{node.name}.{subnode.name}",
                        "start": sub_start,
                        "end": sub_end,
                        "params": params,
                        "is_async": is_async
                    })
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            start = node.lineno
            end = getattr(node, "end_lineno", start)
            params = [arg.arg for arg in node.args.args]
            is_async = isinstance(node, ast.AsyncFunctionDef)
            symbols.append({
                "type": "function",
                "name": node.name,
                "start": start,
                "end": end,
                "params": params,
                "is_async": is_async
            })
    return symbols

def parse_lua_file(content: str, filename: str) -> List[Dict[str, Any]]:
    """Parse Lua scripts for functions and tables."""
    symbols = []
    lines = content.splitlines()
    pattern = re.compile(r"^\s*(?:local\s+)?function\s+([a-zA-Z0-9_.:]+)\s*\(([^)]*)\)")

    for idx, line in enumerate(lines):
        match = pattern.match(line)
        if match:
            func_name = match.group(1)
            params = [p.strip() for p in match.group(2).split(",") if p.strip()]
            start_line = idx + 1
            
            # Simple heuristic for Lua function end: scan forward for matching 'end'
            end_line = start_line
            depth = 1
            for forward_idx in range(idx + 1, len(lines)):
                l = lines[forward_idx].strip()
                # Tokens that open blocks in Lua
                if re.match(r"\b(function|then|do|repeat)\b", l) and not l.startswith("--"):
                    depth += 1
                if re.match(r"\b(end|until)\b", l) and not l.startswith("--"):
                    depth -= 1
                    if depth <= 0:
                        end_line = forward_idx + 1
                        break
            if end_line == start_line and idx + 1 < len(lines):
                end_line = min(len(lines), start_line + 20)

            symbols.append({
                "type": "function",
                "name": func_name,
                "start": start_line,
                "end": end_line,
                "params": params
            })
    return symbols

def parse_generic_file(content: str, filename: str, ext: str) -> List[Dict[str, Any]]:
    """Generic regex parsing for JS, TS, Shell, etc."""
    symbols = []
    lines = content.splitlines()
    # Matches common JS/TS functions, classes, or shell functions
    func_pattern = re.compile(r"^\s*(?:export\s+)?(?:async\s+)?function\s+([a-zA-Z0-9_$]+)\s*\(([^)]*)\)")
    arrow_pattern = re.compile(r"^\s*(?:export\s+)?(?:const|let|var)\s+([a-zA-Z0-9_$]+)\s*=\s*(?:async\s*)?\(([^)]*)\)\s*=>")
    class_pattern = re.compile(r"^\s*(?:export\s+)?class\s+([a-zA-Z0-9_$]+)")
    sh_pattern = re.compile(r"^\s*(?:function\s+)?([a-zA-Z0-9_-]+)\s*\(\)\s*\{")

    for idx, line in enumerate(lines):
        start_line = idx + 1
        m_cls = class_pattern.match(line)
        if m_cls:
            symbols.append({"type": "class", "name": m_cls.group(1), "start": start_line, "end": start_line, "params": []})
            continue
        m_fn = func_pattern.match(line)
        if m_fn:
            params = [p.strip() for p in m_fn.group(2).split(",") if p.strip()]
            symbols.append({"type": "function", "name": m_fn.group(1), "start": start_line, "end": start_line, "params": params})
            continue
        m_ar = arrow_pattern.match(line)
        if m_ar:
            params = [p.strip() for p in m_ar.group(2).split(",") if p.strip()]
            symbols.append({"type": "function", "name": m_ar.group(1), "start": start_line, "end": start_line, "params": params})
            continue
        m_sh = sh_pattern.match(line)
        if m_sh:
            symbols.append({"type": "function", "name": m_sh.group(1), "start": start_line, "end": start_line, "params": []})
            continue

    return symbols

def analyze_file(filepath: str) -> Optional[Dict[str, Any]]:
    """Analyze a single file and generate its symbol map."""
    if not os.path.isfile(filepath):
        return None

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except Exception as e:
        return {"error": str(e), "filepath": filepath}

    ext = os.path.splitext(filepath)[1].lower().lstrip(".")
    if ext == "py":
        symbols = parse_python_file(content, filepath)
    elif ext in ("lua", "luac"):
        symbols = parse_lua_file(content, filepath)
    else:
        symbols = parse_generic_file(content, filepath, ext)

    lines = content.splitlines()
    total_lines = len(lines)
    raw_tokens = estimate_tokens(content)

    return {
        "filepath": filepath,
        "filename": os.path.basename(filepath),
        "total_lines": total_lines,
        "raw_tokens": raw_tokens,
        "symbols": symbols
    }

def format_map_output(res: Dict[str, Any], find_query: Optional[str] = None) -> str:
    """Format symbol map for clean, human and AI consumption."""
    output = []
    fname = res["filename"]
    tot_lines = res["total_lines"]
    raw_tok = res["raw_tokens"]
    symbols = res["symbols"]

    if find_query:
        query = find_query.lower()
        matched = [s for s in symbols if query in s["name"].lower()]
        output.append(f"🔍 Search for '{find_query}' in {fname} ({tot_lines} lines):")
        if not matched:
            output.append("   ❌ No matching symbol found.")
        else:
            for s in matched:
                st, en = s["start"], s["end"]
                name = s["name"]
                stype = s["type"]
                p_str = ", ".join(s.get("params", []))
                output.append(f"   🎯 [{stype}] {name}({p_str}) -> Lines {st}:{en}")
                output.append(f"      👉 Read command: read_file(Path='{res['filepath']}', StartLine={st}, EndLine={en})")
        return "\n".join(output)

    # Full Map Output
    output.append(f"📄 {fname} | Total Lines: {tot_lines:,} | Raw Content: ~{raw_tok:,} tokens")
    if not symbols:
        output.append("   (No top-level functions or classes detected)")
        return "\n".join(output)

    map_lines = []
    for s in symbols:
        st, en = s["start"], s["end"]
        stype = s["type"][0].upper()
        name = s["name"]
        params = ", ".join(s.get("params", []))
        if s.get("is_async"):
            map_lines.append(f"  L{st:04d}-{en:04d} [{stype}] async {name}({params})")
        else:
            map_lines.append(f"  L{st:04d}-{en:04d} [{stype}] {name}({params})")

    map_text = "\n".join(map_lines)
    map_tok = estimate_tokens(map_text)
    savings = max(0.0, 100.0 * (1.0 - (map_tok / max(1, raw_tok))))

    output.append(f"📊 Symbols: {len(symbols)} definitions | Map Size: ~{map_tok:,} tokens | Savings: {savings:.1f}%")
    output.append("--- Symbol Map ---")
    output.append(map_text)
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Code Symbol Mapper & Surgical Token Saver")
    parser.add_argument("target", help="Path to file or directory to map")
    parser.add_argument("--find", "-f", help="Find specific function/class and print exact line range")
    parser.add_argument("--max-depth", type=int, default=2, help="Directory scan max depth (default: 2)")
    args = parser.parse_args()

    target = os.path.abspath(args.target)
    if os.path.isfile(target):
        res = analyze_file(target)
        if not res:
            print(f"Error reading file: {target}")
            sys.exit(1)
        print(format_map_output(res, args.find))
    elif os.path.isdir(target):
        print(f"📁 Scanning Directory: {target}")
        total_raw_tokens = 0
        total_map_tokens = 0
        total_files = 0
        total_symbols = 0

        for root, dirs, files in os.walk(target):
            # Prune hidden & virtualenv dirs
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("venv", "node_modules", "__pycache__")]
            rel_depth = root[len(target):].count(os.sep)
            if rel_depth > args.max_depth:
                continue

            for f in sorted(files):
                if f.endswith((".py", ".lua", ".js", ".ts", ".sh")):
                    fpath = os.path.join(root, f)
                    res = analyze_file(fpath)
                    if res and res.get("symbols"):
                        total_files += 1
                        total_raw_tokens += res["raw_tokens"]
                        sym_count = len(res["symbols"])
                        total_symbols += sym_count
                        map_out = format_map_output(res, args.find)
                        map_tok = estimate_tokens(map_out)
                        total_map_tokens += map_tok
                        print("\n" + map_out)

        if total_files > 0:
            savings = max(0.0, 100.0 * (1.0 - (total_map_tokens / max(1, total_raw_tokens))))
            print("\n" + "=" * 50)
            print(f"🏆 REPOSITORY SUMMARY:")
            print(f"   Files Mapped: {total_files}")
            print(f"   Total Symbols: {total_symbols}")
            print(f"   Original Repo Tokens: ~{total_raw_tokens:,} tokens")
            print(f"   Compact Map Tokens:   ~{total_map_tokens:,} tokens")
            print(f"   ⚡ Net Token Savings: {savings:.1f}%")
            print("=" * 50)
    else:
        print(f"Target not found: {target}")
        sys.exit(1)

if __name__ == "__main__":
    main()
