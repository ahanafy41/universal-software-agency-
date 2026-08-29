#!/usr/bin/env python3
"""
backup_manager.py - Pre-Mutation Snapshot & Instant Rollback Utility
Part of Universal Software & AI Engineering Agency
"""

import sys
import os
import shutil
import datetime

BACKUP_DIR = ".backups"

def create_backup(target_file):
    if not os.path.exists(target_file):
        print(f"Error: Target file '{target_file}' does not exist.")
        return False

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_dir = os.path.join(BACKUP_DIR, timestamp)
    os.makedirs(dest_dir, exist_ok=True)

    dest_file = os.path.join(dest_dir, os.path.basename(target_file))
    shutil.copy2(target_file, dest_file)
    print(f"Backup created successfully: {dest_file}")
    return True

def main():
    if len(sys.argv) < 3:
        print("Usage: backup_manager.py [backup|restore] <target_file>")
        sys.exit(1)

    action = sys.argv[1].lower()
    target = sys.argv[2]

    if action == "backup":
        success = create_backup(target)
        sys.exit(0 if success else 1)
    else:
        print(f"Unsupported action: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
