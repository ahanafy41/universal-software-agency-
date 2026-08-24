# Real-Time Debugging & Diagnostic Scratchpad (`debug_tasks.md`)

```markdown
# 🛠️ Diagnostic & Bug Fix Task List

- **Issue ID**: [e.g. BUG-001]
- **Severity**: [Critical | High | Medium | Low]
- **Environment**: OS: [e.g. Windows 11 / Ubuntu 24.04], Runtime: [e.g. .NET 8 / Python 3.12 / Node 20]
- **Reproduction Command**: [e.g. pytest tests/test_auth.py OR dotnet run]
- **Target File**: `[path/to/faulty_file]`
- **Target Line**: `[line number]`
- **Symbol / AST Node**: `[Class.MethodName or function_name]`
- **Status**: [Investigating | Patching | Verifying | Resolved]

---

## 🔍 Pre-Fix Discovery & Triage
- [ ] Step 1: Ingest directory hierarchy, callers, and dependencies (Subagent B).
- [ ] Step 2: Formulate 3-Branch Diagnostic Hypotheses (Subagent E):
  - **Branch A (API Contract / Signature)**: [Evaluation]
  - **Branch B (Lifecycle / Concurrency / State)**: [Evaluation]
  - **Branch C (Data Boundary / Nullability / Syntax)**: [Evaluation]
- [ ] Step 3: Exact Location Pinpointed & Locked in `debug_manifest.json`.

---

## 🛡️ Pre-Mutation Backup & Surgical Patching
- [ ] Step 4: Execute `python3 scripts/backup_manager.py backup <file>` to snapshot file in `.backups/`.
- [ ] Step 5: Apply localized surgical patch strictly to faulty AST node (Subagent F).
- [ ] Step 6: Verify blast radius with `python3 scripts/diff_verifier.py <backup> <modified>`.

---

## 🧪 Verification & Delivery Gate
- [ ] Step 7: Run `python3 scripts/validate_code.py --strict <modified_file>` (AST & syntax clean).
- [ ] Step 8: Run reproduction command and automated tests (Subagent D).
- [ ] Step 9: Deliver What's Next roadmap with verification commands and regression watchlist.
```
