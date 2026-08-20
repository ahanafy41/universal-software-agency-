# Debug & Resolution Scratchpad (`debug_tasks.md`)

## 1. Problem Statement & Exact Location Pinpoint
- **Issue ID**: BUG-YYYYMMDD-001
- **Issue Description**: [Summary of the bug or runtime fault]
- **Exact File Path**: `[path/to/target_file.ext]`
- **Exact Line Number**: Line [X]
- **Target Symbol / AST Node**: `[ClassName::MethodName / function_name]`
- **Failing Code Snippet**:
  ```text
  [Exact lines where error originates]
  ```
- **Error Stack Trace / Log**:
  ```text
  [Raw error log or stack trace]
  ```

---

## 2. Interactive Discovery Q&A Log
- **Q1**: [Targeted question asked to user] -> **A1**: [User response]
- **Q2**: [Follow-up question if needed] -> **A2**: [User response]

---

## 3. 3-Branch Root-Cause Diagnostic Matrix
- [ ] **Branch A (API / Contract / Reflection Mismatch)**: [Evaluation notes]
- [ ] **Branch B (Lifecycle / Concurrency / State Fault)**: [Evaluation notes]
- [ ] **Branch C (Data / Boundary / Syntax Corruption)**: [Evaluation notes]
- **Confirmed Root Cause**: [Definitive explanation of the fault]

---

## 4. Surgical Resolution Checklist
- [ ] **Step 1: Pre-Mutation Snapshot**: Archived in `.backups/YYYYMMDD_HHMMSS/`
- [ ] **Step 2: AST Surgical Patch**: Applied only to line [X]
- [ ] **Step 3: Diff Integrity Audit**: Verified 0% unintended drift against snapshot
- [ ] **Step 4: AST & Syntax Validation**: `validate_code.py` passed with 0 errors
- [ ] **Step 5: Manifest Sync**: Updated `debug_manifest.json` to "verified"
- [ ] **Step 6: Delivery & What's Next**: Presented verification steps & roadmap

---

## 5. Execution & Audit Log
| Timestamp | Step ID | Status | Summary of Action / Fix |
|---|---|---|---|
| YYYY-MM-DD HH:MM | Step 1 | Completed | Snapshot archived to .backups/ |
| YYYY-MM-DD HH:MM | Step 2 | Completed | Surgical patch applied to exact target line |
| YYYY-MM-DD HH:MM | Step 4 | Completed | validate_code.py passed clean |
