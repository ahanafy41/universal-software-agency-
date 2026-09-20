#!/usr/bin/env python3
"""
Pre-Mutation Backup Manager & Snapshot Rollback Engine (Zero-Dependency)
Creates timestamped backups in .backups/YYYYMMDD_HHMMSS/ before any file mutation.
Compatible with Google Anti-Gravity 2.0 sandbox.
"""
import os
import sys
import shutil
import json
import argparse
from datetime import datetime

BACKUP_ROOT = ".backups"

def create_snapshot(target_file_path):
    if not os.path.exists(target_file_path):
        return {"success": False, "error": f"Target file does not exist: {target_file_path}"}

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_dir = os.path.join(BACKUP_ROOT, timestamp)
    os.makedirs(snapshot_dir, exist_ok=True)

    filename = os.path.basename(target_file_path)
    snapshot_path = os.path.join(snapshot_dir, filename)
    shutil.copy2(target_file_path, snapshot_path)
    return {
        "success": True,
        "action": "backup",
        "original_file": target_file_path,
        "snapshot_path": snapshot_path,
        "timestamp": timestamp
    }

def restore_latest_snapshot(target_file_path):
    if not os.path.exists(BACKUP_ROOT):
        return {"success": False, "error": f"No backup directory found at '{BACKUP_ROOT}'"}

    filename = os.path.basename(target_file_path)
    snapshots = sorted([d for d in os.listdir(BACKUP_ROOT) if os.path.isdir(os.path.join(BACKUP_ROOT, d))], reverse=True)
    
    for snap in snapshots:
        candidate_path = os.path.join(BACKUP_ROOT, snap, filename)
        if os.path.exists(candidate_path):
            shutil.copy2(candidate_path, target_file_path)
            return {
                "success": True,
                "action": "restore",
                "restored_file": target_file_path,
                "source_snapshot": candidate_path,
                "snapshot_id": snap
            }

    return {"success": False, "error": f"No matching snapshot found for '{filename}' in '{BACKUP_ROOT}'"}

def list_snapshots(target_file_path=None):
    if not os.path.exists(BACKUP_ROOT):
        return {"success": True, "snapshots": []}
    
    snapshots = sorted([d for d in os.listdir(BACKUP_ROOT) if os.path.isdir(os.path.join(BACKUP_ROOT, d))], reverse=True)
    results = []
    filter_filename = os.path.basename(target_file_path) if target_file_path else None

    for s in snapshots:
        s_dir = os.path.join(BACKUP_ROOT, s)
        try:
            files = os.listdir(s_dir)
        except OSError:
            continue
        if filter_filename:
            if filter_filename in files:
                results.append({"timestamp": s, "files": [filter_filename], "path": os.path.join(s_dir, filter_filename)})
        else:
            results.append({"timestamp": s, "files": files, "directory": s_dir})
            
    return {"success": True, "snapshots": results}

def main():
    parser = argparse.ArgumentParser(description="Pre-Mutation Snapshot & Backup Manager (Zero-Dependency)")
    parser.add_argument("action", choices=["backup", "restore", "list"], help="Action to perform")
    parser.add_argument("file_path", nargs="?", default=None, help="Target file path")
    parser.add_argument("--json", action="store_true", help="Output formatted JSON")
    parser.add_argument("--compact", action="store_true", help="Output compact single-line JSON")
    parser.add_argument("-q", "--quiet", action="store_true", help="Silent mode (exit code only)")
    args = parser.parse_args()

    if args.action == "list":
        res = list_snapshots(args.file_path)
        if args.quiet:
            sys.exit(0)
        if args.compact:
            print(json.dumps(res, separators=(',', ':')))
        elif args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"Available Snapshots in '{BACKUP_ROOT}':")
            for s in res["snapshots"]:
                print(f"  - {s['timestamp']}: {', '.join(s['files'])}")
        sys.exit(0)

    if not args.file_path:
        err = {"success": False, "error": "file_path is required for backup and restore actions."}
        if not args.quiet:
            if args.compact:
                print(json.dumps(err, separators=(',', ':')))
            elif args.json:
                print(json.dumps(err, indent=2))
            else:
                print(f"[ERROR] {err['error']}")
        sys.exit(1)

    if args.action == "backup":
        res = create_snapshot(args.file_path)
    elif args.action == "restore":
        res = restore_latest_snapshot(args.file_path)
    else:
        res = {"success": False, "error": f"Unknown action '{args.action}'"}

    if not args.quiet:
        if args.compact:
            print(json.dumps(res, separators=(',', ':')))
        elif args.json:
            print(json.dumps(res, indent=2))
        else:
            if res["success"]:
                if args.action == "backup":
                    print(f"[BACKUP_SUCCESS] Created snapshot: {res['snapshot_path']}")
                else:
                    print(f"[RESTORED] Reverted {res['restored_file']} from snapshot '{res['snapshot_id']}'")
            else:
                print(f"[ERROR] {res['error']}")

    sys.exit(0 if res.get("success") else 1)

if __name__ == '__main__':
    main()
