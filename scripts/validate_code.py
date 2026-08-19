import sys
import os
import ast
import json
import re

def validate_python(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        print(f"[PASS] Python AST parse successful for {file_path}")
        return True
    except SyntaxError as e:
        print(f"[FAIL] Python SyntaxError in {file_path} at line {e.lineno}: {e.msg}")
        return False
    except Exception as e:
        print(f"[FAIL] Error parsing {file_path}: {e}")
        return False

def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"[PASS] JSON parse successful for {file_path}")
        return True
    except Exception as e:
        print(f"[FAIL] JSON error in {file_path}: {e}")
        return False

def validate_brackets(file_path):
    pairs = {'{': '}', '(': ')', '[': ']'}
    stack = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cleaned = re.sub(r'//.*', '', content)
        cleaned = re.sub(r'/\*.*?\*/', '', cleaned, flags=re.DOTALL)
        cleaned = re.sub(r'"(\\.|[^"\\])*"', '', cleaned)
        cleaned = re.sub(r"'(\\.|[^'\\])*'", '', cleaned)

        for line_num, char in enumerate(cleaned, 1):
            if char in pairs:
                stack.append((char, line_num))
            elif char in pairs.values():
                if not stack:
                    print(f"[FAIL] Unmatched closing bracket '{char}' in {file_path}")
                    return False
                top, _ = stack.pop()
                if pairs[top] != char:
                    print(f"[FAIL] Mismatched bracket '{top}' with '{char}' in {file_path}")
                    return False

        if stack:
            unmatched = stack[-1][0]
            print(f"[FAIL] Unclosed bracket '{unmatched}' in {file_path}")
            return False

        print(f"[PASS] Bracket balance verified for {file_path}")
        return True
    except Exception as e:
        print(f"[FAIL] Error checking brackets in {file_path}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_code.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"[FAIL] File not found: {file_path}")
        sys.exit(1)

    ext = os.path.splitext(file_path)[1].lower()
    success = True

    if ext == '.py':
        success = validate_python(file_path)
    elif ext == '.json':
        success = validate_json(file_path)
    elif ext in ['.cs', '.js', '.ts', '.cpp', '.c', '.java', '.lua', '.rs', '.go']:
        success = validate_brackets(file_path)
    else:
        print(f"[INFO] Generic file checked: {file_path}")

    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
