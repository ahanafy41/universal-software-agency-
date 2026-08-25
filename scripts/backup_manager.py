#!/usr/bin/env python3
"""
backup_manager.py - Automated Pre-Mutation Snapshot and Instant Rollback Tool
"""

import os
import sys
import shutil
import datetime

BACKUP_ROOT = ".backups"

def create_backup(target_file):
    if not os.path.isfile(target_file):
        print(f"Error: Target file '{target_file}' does not exist.")
        sys.exit(1)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(BACKUP_ROOT, timestamp)
    os.makedirs(backup_dir, exist_ok=True)

    dest_file = os.path.join(backup_dir, os.path.basename(target_file))
    shutil.copy2(target_file, dest_file)
    print(f"Backup successfully created at: {dest_file}")
    return dest_file

def restore_backup(backup_file, target_file):
    if not os.path.isfile(backup_file):
        print(f"Error: Backup file '{backup_file}' does not exist.")
        sys.exit(1)
    shutil.copy2(backup_file, target_file)
    print(f"File successfully restored from '{backup_file}' to '{target_file}'")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 backup_manager.py [backup <file>] | [restore <backup_file> <target_file>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "backup":
        create_backup(sys.argv[2])
    elif command == "restore":
        if len(sys.argv) < 4:
            print("Usage: python3 backup_manager.py restore <backup_file> <target_file>")
            sys.exit(1)
        restore_backup(sys.argv[2], sys.argv[3])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()