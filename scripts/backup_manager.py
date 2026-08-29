#!/usr/bin/env python3
"""
Pre-Mutation Backup Manager & Snapshot Rollback Engine (Zero-Dependency)
Creates timestamped backups in .backups/YYYYMMDD_HHMMSS/ before any file mutation.
Compatible with Google Anti-Gravity 2.0 sandbox.
"""

import sys
import os
import shutil
import argparse
import json
from datetime import datetime
from pathlib import Path


BACKUP_ROOT = Path(".backups")


def create_backup(target_file: str, json_output: bool = False, compact: bool = False) -> int:
    path = Path(target_file).resolve()
    if not path.is_file():
        err = {"status": "error", "message": f"Target file does not exist: {target_file}"}
        if json_output:
            print(json.dumps(err))
        else:
            print(f"[-] Error: {err['message']}", file=sys.stderr)
        return 1

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = BACKUP_ROOT / timestamp
    backup_dir.mkdir(parents=True, exist_ok=True)

    dest_file = backup_dir / path.name
    shutil.copy2(path, dest_file)

    meta = {
        "timestamp": timestamp,
        "original_path": str(path),
        "backup_path": str(dest_file),
        "file_size": path.stat().st_size,
    }
    with open(backup_dir / "meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    if json_output:
        print(json.dumps(meta, indent=None if compact else 2))
    else:
        print(f"[+] Backup created: {dest_file}")
    return 0


def list_backups(json_output: bool = False, compact: bool = False) -> int:
    if not BACKUP_ROOT.exists():
        if json_output:
            print("[]")
        else:
            print("No backups found.")
        return 0

    backups = []
    for entry in sorted(BACKUP_ROOT.iterdir(), reverse=True):
        if entry.is_dir():
            meta_file = entry / "meta.json"
            if meta_file.exists():
                try:
                    with open(meta_file, "r", encoding="utf-8") as f:
                        backups.append(json.load(f))
                except Exception:
                    pass

    if json_output:
        print(json.dumps(backups, indent=None if compact else 2))
    else:
        for b in backups:
            print(f"[{b.get('timestamp')}] {b.get('original_path')} -> {b.get('backup_path')}")
    return 0


def restore_backup(target_file: str, json_output: bool = False, compact: bool = False) -> int:
    target_name = Path(target_file).name
    if not BACKUP_ROOT.exists():
        err = {"status": "error", "message": "No backups directory found."}
        if json_output:
            print(json.dumps(err))
        else:
            print(f"[-] Error: {err['message']}", file=sys.stderr)
        return 1

    latest_backup = None
    for entry in sorted(BACKUP_ROOT.iterdir(), reverse=True):
        candidate = entry / target_name
        if candidate.is_file():
            latest_backup = candidate
            break

    if not latest_backup:
        err = {"status": "error", "message": f"No backup found for {target_name}"}
        if json_output:
            print(json.dumps(err))
        else:
            print(f"[-] Error: {err['message']}", file=sys.stderr)
        return 1

    dest = Path(target_file).resolve()
    shutil.copy2(latest_backup, dest)

    res = {
        "status": "success",
        "restored_from": str(latest_backup),
        "target_file": str(dest),
    }
    if json_output:
        print(json.dumps(res, indent=None if compact else 2))
    else:
        print(f"[+] Successfully restored {dest} from {latest_backup}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Pre-Mutation Snapshot & Backup Manager (Zero-Dependency)")
    parser.add_argument("action", choices=["backup", "restore", "list"], help="Action to perform")
    parser.add_argument("file_path", nargs="?", default=None, help="Target file path")
    parser.add_argument("--json", action="store_true", help="Output formatted JSON")
    parser.add_argument("--compact", action="store_true", help="Output compact single-line JSON")
    parser.add_argument("-q", "--quiet", action="store_true", help="Silent mode (exit code only)")

    args = parser.parse_args()

    if args.action == "list":
        sys.exit(list_backups(json_output=args.json, compact=args.compact))
    elif args.action == "backup":
        if not args.file_path:
            print("[-] Error: file_path is required for backup", file=sys.stderr)
            sys.exit(1)
        sys.exit(create_backup(args.file_path, json_output=args.json, compact=args.compact))
    elif args.action == "restore":
        if not args.file_path:
            print("[-] Error: file_path is required for restore", file=sys.stderr)
            sys.exit(1)
        sys.exit(restore_backup(args.file_path, json_output=args.json, compact=args.compact))


if __name__ == "__main__":
    main()
