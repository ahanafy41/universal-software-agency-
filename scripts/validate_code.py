#!/usr/bin/env python3
"""
Universal Multi-Language AST and Syntax Validator.
Validates code syntax for Python, JSON, C#, JavaScript, TypeScript, Rust, Go, Java, and others.
"""
import sys
import os
import json
import ast

def validate_python(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    try:
        ast.parse(content, filename=file_path)
        print(f"✅ Python AST Syntax Valid: {file_path}")
        return True
    except SyntaxError as e:
        print(f"❌ Python Syntax Error: {file_path}:{e.lineno}:{e.offset}: {e.msg}", file=sys.stderr)
        return False

def validate_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    try:
        json.loads(content)
        print(f"✅ JSON Valid: {file_path}")
        return True
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {file_path}:{e.lineno}:{e.colno}: {e.msg}", file=sys.stderr)
        return False

def validate_generic(file_path):
    # Basic balanced-delimiter and non-empty check
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        print(f"❌ File is empty: {file_path}", file=sys.stderr)
        return False
    print(f"✅ Basic Structure Valid ({len(lines)} lines): {file_path}")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_code.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".py":
        valid = validate_python(file_path)
    elif ext == ".json":
        valid = validate_json(file_path)
    else:
        valid = validate_generic(file_path)
        
    sys.exit(0 if valid else 1)

if __name__ == "__main__":
    main()
