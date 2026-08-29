# Quick Agent Guide: Universal Software Agency (v2.3.0 Anti-Gravity 2.0 Edition)

## 🚀 Execution Invariants for AI Agents

1. **Mandatory Live 2026 Web Search Gate**:
   - Query Google Search / live SDK documentation for official 2026 API signatures, models, and libraries before drafting specifications.

2. **Mandatory Human-in-the-Loop Approval Gate (Stop & Wait)**:
   - Present `PRD.md`, `project_spec.json`, and `tasks.md` (or `TICKET.md`) to the user.
   - **HALT** execution immediately and await explicit user approval (`Approved` / `موافق`) before spawning implementation subagents.

3. **Two-Way Comprehensive Scoping**:
   - Explore all layers (business logic, library ecosystem, persistence, A11y, error handling, edge cases).
   - Inquire open-endedly and ask if the user has any questions or specific libraries in mind.

4. **Support Ticket & Bug Triage Workflow**:
   - Open `TICKET.md` for any defect or runtime error.
   - Investigate environment and logs, classify via 3-Branch Root-Cause Matrix, formulate patch plan, and seek user approval before touching code.

5. **Strict Code Preservation & Zero Main-Loop Bloat**:
   - Take pre-mutation backup via `scripts/backup_manager.py`.
   - Restrict code churn using `scripts/diff_verifier.py`.
   - Delegate heavy parsing and implementation to subagents.
