# Real-Time Debugging Checklist (`debug_tasks.md`)

## 1. Issue Triage & Ground Truth
- [ ] Confirm exact trigger action from user
- [ ] Verify OS & runtime environment
- [ ] Pinpoint exact file path, line number, and AST symbol

## 2. Pre-Mutation Snapshot
- [ ] Create timestamped backup in `.backups/`
- [ ] Lock non-failing files as read-only

## 3. Surgical Patch & Verification
- [ ] Apply minimal patch to target AST node
- [ ] Run `python3 scripts/validate_code.py`
- [ ] Perform diff audit against backup snapshot
- [ ] Output What's Next Roadmap