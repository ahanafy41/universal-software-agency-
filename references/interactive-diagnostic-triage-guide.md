# Interactive Diagnostic Triage & Bug Discovery Protocol (دليل الاستكشاف التفاعلي للأعطال)

Protocol for engaging the user with focused, turn-by-turn interactive questions whenever an error is ambiguous, lacks reproduction context, or requires environment-specific clarity.

---

## 1. The Strict One-Question-Per-Turn Triage Rule (قاعدة السؤال الواحد لكل رسالة)

When a bug report is incomplete or ambiguous:
1. **No Question Overload**: NEVER overwhelm the user with a barrage of questions. Ask **exactly ONE targeted question per message**.
2. **Prioritized Discovery Sequence**:
   - **Turn 1 (Trigger & Steps)**: "What specific action or button click immediately preceded this error?"
   - **Turn 2 (Environment & Target)**: "Which OS version, framework version, or device model are you running?"
   - **Turn 3 (Expected vs Actual)**: "What was the expected output or behavior versus what actually happened?"
   - **Turn 4 (Log / Context)**: "Do you have any error logs or console messages around that timestamp?"
3. **Artifact Syncing**: Each answered question is immediately appended to `debug_tasks.md` and `debug_manifest.json`.

---

## 2. Dual-Artifact Tracking Engine: `debug_tasks.md` + `debug_manifest.json`

Every debugging mission generates and maintains two synchronized artifacts in the project root or workspace:

1. **Human Executive Scratchpad (`debug_tasks.md`)**:
   - Clear markdown checklist with checkboxes `- [ ]`, `- [/]`, `- [x]`.
   - Explicit section identifying the **Exact Location (File, Line, Symbol, Snippet)**.
   - Real-time execution log updated after every mutation.

2. **Machine Deterministic Manifest (`debug_manifest.json`)**:
   - Conforms strictly to `references/debug-manifest-schema.json`.
   - Records structured error metadata, 3-branch diagnostic results, backup path, line-level diffs, and verification flags.
