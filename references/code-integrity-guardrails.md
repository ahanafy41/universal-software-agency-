# Strict Code-Preservation & Zero-Corruption Guardrails (بروتوكول حماية الكود وتطويق نطاق التعديل)

This protocol enforces the non-negotiable **Zero-Corruption Invariant** across all programming languages and project architectures.

---

## 1. 🛡️ The 4-Stage Safety Lifecycle

```
[Phase 1: Pre-Mutation Backup]
       │
       ▼  python3 scripts/backup_manager.py backup <file>
[Phase 2: Exact AST Pinpoint]
       │
       ▼  Record File, Line, Symbol in debug_tasks.md & debug_manifest.json
[Phase 3: Surgical Mutation]
       │
       ▼  Apply localized patch to EXACT faulty AST node ONLY
[Phase 4: Diff & Churn Audit]
       │
       ▼  python3 scripts/diff_verifier.py <backup> <modified> --max-churn 30.0
[PASS -> validate_code.py] OR [FAIL -> python3 backup_manager.py restore <file>]
```

---

## 2. Non-Negotiable Invariants

1. **Strict Blast Radius Limitation**:
   - Edits must be isolated strictly to the target function, method, or line causing the bug.
   - Surrounding working code, helper functions, and comments are locked as read-only.
2. **Prohibition of Unrequested Refactoring**:
   - Never rename variables, restructure directories, or replace working dependencies unless explicitly requested.
3. **Automated Rollback on Failure**:
   - If AST syntax checks fail or churn exceeds threshold, immediately execute `python3 scripts/backup_manager.py restore <target_file>`.
