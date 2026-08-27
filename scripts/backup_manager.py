#!/usr/bin/env python3
"""
Pre-Mutation Backup Manager (Human-Grade Safety Utility)
Part of the Universal Software & AI Engineering Agency Toolset
"""

import os
import sys
import shutil
import argparse
import datetime
import json

BACKUP_DIR = ".backups"

def ensure_backup_dir():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

def create_backup(target_path):
    if not os.path.exists(target_path):
        print(f"Error: Target path '{target_path}' does not exist.", file=sys.stderr)
        return False

    ensure_backup_dir()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_subdir = os.path.join(BACKUP_DIR, timestamp)
    os.makedirs(backup_subdir, exist_ok=True)

    rel_path = os.path.basename(target_path)
    dest_path = os.path.join(backup_subdir, rel_path)

    if os.path.isdir(target_path):
        shutil.copytree(target_path, dest_path)
    else:
        shutil.copy2(target_path, dest_path)

    meta = {
        "timestamp": timestamp,
        "original_path": os.path.abspath(target_path),
        "backup_path": os.path.abspath(dest_path),
        "is_dir": os.path.isdir(target_path)
    }

    with open(os.path.join(backup_subdir, "backup_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    print(f"✅ Backup created: {dest_path}")
    print(f"Snapshot ID: {timestamp}")
    return True

def list_backups():
    if not os.path.exists(BACKUP_DIR):
        print("No backups found.")
        return

    snapshots = sorted(os.listdir(BACKUP_DIR), reverse=True)
    if not snapshots:
        print("No backups found.")
        return

    print(f"Found {len(snapshots)} backup snapshots:")
    for s in snapshots:
        meta_file = os.path.join(BACKUP_DIR, s, "backup_meta.json")
        if os.path.exists(meta_file):
            with open(meta_file, "r", encoding="utf-8") as f:
                meta = json.load(f)
            print(f"  - ID: {s} | Target: {meta.get('original_path')} | Created: {meta.get('timestamp')}")
        else:
            print(f"  - ID: {s}")

def restore_backup(snapshot_id):
    backup_subdir = os.path.join(BACKUP_DIR, snapshot_id)
    meta_file = os.path.join(backup_subdir, "backup_meta.json")

    if not os.path.exists(meta_file):
        print(f"Error: Snapshot '{snapshot_id}' does not exist or metadata is missing.", file=sys.stderr)
        return False

    with open(meta_file, "r", encoding="utf-8") as f:
        meta = json.load(f)

    orig_path = meta["original_path"]
    backup_path = meta["backup_path"]

    if meta["is_dir"]:
        if os.path.exists(orig_path):
            shutil.rmtree(orig_path)
        shutil.copytree(backup_path, orig_path)
    else:
        shutil.copy2(backup_path, orig_path)

    print(f"✅ Restored snapshot '{snapshot_id}' to '{orig_path}'")
    return True

def main():
    parser = argparse.ArgumentParser(description="Pre-Mutation Backup Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    backup_parser = subparsers.add_parser("backup", help="Create a backup snapshot of a file or directory")
    backup_parser.add_argument("path", help="Path to file or directory to backup")

    list_parser = subparsers.add_parser("list", help="List all available backup snapshots")

    restore_parser = subparsers.add_parser("restore", help="Restore a backup snapshot")
    restore_parser.add_argument("snapshot_id", help="Snapshot ID / timestamp to restore")

    args = parser.parse_args()

    if args.command == "backup":
        if not create_backup(args.path):
            sys.exit(1)
    elif args.command == "list":
        list_backups()
    elif args.command == "restore":
        if not restore_backup(args.snapshot_id):
            sys.exit(1)

if __name__ == "__main__":
    main()
