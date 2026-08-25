# End-to-End Walkthrough: Building a Production Tool with the Universal Agency

This walkthrough demonstrates the end-to-end multi-agent execution pipeline on a sample project.

---

## Phase 0: Scoping & Project Contract

1. **User Request**: "Build an accessible CLI and GUI markdown notes tool with encrypted local SQLite storage in Python."
2. **Scoping Execution**:
   - Agency activates **Fast-Track Mode** because the tech stack, UI requirements, and persistence layer are fully specified.
   - Compiles `PRD.md` (Human contract) and `project_spec.json` (Machine contract).
   - Generates `project_mindmap.md` showing UI, Core, and Storage layer separation.
   - Creates `tasks.md` checklist with assigned worker subagent tags.

---

## Phase 1: Knowledge Ingestion & Live 2026 Web Search

1. Subagent A inspects `references/agency-schemas.json` and user-provided API notes.
2. Subagent G searches Google for modern 2026 SQLite encryption patterns (`sqlcipher3` / `cryptography`).
3. Subagent B confirms baseline environment and library compatibility.

---

## Phase 2: Implementation with Human-Grade Craftsmanship

1. **Subagent C (Storage Engine)**: Implements `storage/db.py` with **Atomic I/O**, connection pooling, and exponential backoff retries.
2. **Subagent C (Core Domain)**: Implements `core/notes_service.py` using pure domain models, Design-by-Contract (`Requires`/`Ensures`), and custom actionable exceptions.
3. **Subagent C (UI & CLI)**: Implements `cli/main.py` with `--doctor` self-check, `--json` output, and **Graceful Shutdown (`SIGINT`)** handling.

---

## Phase 3: Automated QA & Deterministic Validation

1. **Subagent D (Testing Engineer)**: Authors `tests/test_notes.py` covering:
   - Happy paths (create, read, search, delete).
   - Failure-mode tests (corrupted DB file, invalid encryption key, disk full).
2. **Subagent F (Verification)**: Runs `python3 scripts/validate_code.py --strict .` to ensure:
   - Zero syntax/AST errors.
   - Zero `TODO` or `FIXME` placeholders.
   - 100% adherence to human-grade standards.
3. **Delivery**: Outputs `COMPLETION_REPORT.md` with 1-click execution commands and the Verification Seal.