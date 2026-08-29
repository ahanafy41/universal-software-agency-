# Project Lifecycle, Scoping & Architecture Playbook

This playbook governs the end-to-end inception, scoping, structural design, live documentation verification, human approval gate, and real-time execution tracking across all software engineering tracks.

---

## 1. Comprehensive Two-Way Scoping & Live Search Protocol

The Lead Orchestrator engages in a deep, interactive discovery dialogue to explore all technical layers:

### 🧭 Comprehensive Scoping Invariants:
1. **Deep Exploration**: Thoroughly investigate business value, library ecosystem, persistence, accessibility (A11y), error handling, and edge cases.
2. **Two-Way Dialogue**: Conclude discovery rounds by actively asking the user if they have additional questions, clarifications, or specific library preferences.
3. **Mandatory Live 2026 Web Search Gate**: Before drafting specifications, query Google Search / live SDK documentation for official 2026 API signatures, modern models, and breaking changes.

---

## 2. Mandatory Human-in-the-Loop Approval Gate (Stop & Wait Invariant)

**STRICT PROHIBITION OF PREMATURE CODING**: The orchestrator is **STRICTLY FORBIDDEN** from invoking implementation subagents or writing code in the same turn that specifications are compiled.

### The Gatekeeper Protocol:
1. Compile `PRD.md`, `project_spec.json`, and `tasks.md`.
2. Present a comprehensive plan summary card to the user.
3. **STOP and wait for the user's explicit decision**:
   - **Approve (`موافق` / `Approved`)**: Proceed to implementation phase.
   - **Reject (`رفض` / `Rejected`)**: Abort or rethink core direction.
   - **Request Changes (`تعديل`)**: Update specs and task plan without writing code until approval is secured.

---

## 3. Product Requirements Document (`PRD.md`) Template

```markdown
# Product Requirements Document (PRD): [Project Title]

**Version:** 1.0 (MVP) | **Date:** YYYY-MM-DD | **Track:** [Track A / B / C]

## 1. Executive Summary & Problem Statement
- **Problem Overview:** [Core user pain point].
- **Proposed Solution:** [Concise tool description].
- **Target Persona:** [End users, power users, accessibility users].

## 2. Live Research & Verified 2026 Reference Specs
- **Live Search Findings:** [Verified SDK signatures, models, and official documentation].
- **Extracted Contracts:** [Key DTOs, schemas, and validation constraints in `references_manifest.json`].

## 3. Functional Requirements (MVP Scope)
- **FR-1 (Must-Have):** [Primary feature workflow].
- **FR-2 (Must-Have):** [Secondary feature workflow].
- **FR-3 (Data & Storage):** [Atomic persistence / SQLite schema].
- **FR-4 (Diagnostics):** [Actionable errors & `--doctor` pre-flight check].

## 4. Non-Functional Requirements
- **Accessibility:** 100% keyboard-navigable, explicit ARIA labels, clean terminal output.
- **Portability:** 1-click launcher (`run.sh`/`run.bat`) or self-contained binary.
- **Resilience:** Graceful shutdown (`SIGINT`), atomic disk writes, structured logging.
```

---

## 4. Machine-Readable Manifest & Tasks (`project_spec.json` & `tasks.md`)

Alongside `PRD.md`, generate `project_spec.json` and track execution milestones in `tasks.md` tagged with subagent owners.

---

## 5. 3-Tier Polyglot Architecture Blueprints

Every application strictly separates **Presentation**, **Domain Logic**, and **Persistence** across Python, C# .NET, TypeScript, Rust, and Go.
