# Project Lifecycle & Architectural Planning Guide (دليل دورة حياة المشروع وتأسيس المعمارية)

This consolidated guide defines the end-to-end lifecycle for scoping, planning, structuring, and tracking software projects.

---

## 1. Dual Scoping Protocol: Interactive Mode & Fast-Track Mode

### 🎯 Mode A: Interactive Scoping (النمط التفاعلي - الافتراضي)
When the user's requirements are open-ended, ambiguous, or incomplete:
- Ask **strictly ONE focused question per message/turn** across the discovery pillars:
  1. **Business Value & Core Objective**: What exact problem is being solved and who is the user?
  2. **Technical Constraints & Stack**: Language version, UI framework, CLI vs. GUI, external libraries.
  3. **Knowledge & Reference Documents**: Any custom schemas, SDK headers, or API specs in `docs/`?
  4. **Persistence & Data Storage**: SQLite, JSON files, Postgres, in-memory, or stateless?
  5. **Universal Accessibility (A11y)**: Screen reader support, keyboard shortcuts, high contrast?
  6. **Error Handling & Resilience**: Offline fallbacks, network retry strategies, logging depth?

### ⚡ Mode B: Fast-Track Scoping (نمط المسار السريع)
When the user provides a complete PRD, detailed specifications, or explicit architecture upfront:
- **Bypass exploratory questions immediately**. Transition directly to compiling `PRD.md`, `project_spec.json`, `project_mindmap.md`, and `tasks.md`.

---

## 2. Executive PRD Template (`PRD.md`)

```markdown
# Product Requirements Document (PRD): [Project Name]

## 1. Executive Summary & Core Value
- **Problem Statement**: [What problem does this solve?]
- **Target Audience**: [Developers, power users, general audience, screen reader users]
- **Target MVP Scope**: [Concise list of core deliverables for v1]

## 2. Technical Stack & Invariants
- **Primary Language & Runtime**: [e.g., Python 3.12, C# .NET 9, Node.js 22 LTS, Rust 1.80]
- **UI & UX Paradigm**: [CLI, WPF/WinForms, Web React/Vite, Terminal TUI]
- **Persistence & State**: [SQLite with Atomic I/O, JSON Dataclass, Postgres]
- **Universal Accessibility (A11y)**: [100% Keyboard-first, ARIA landmarks, accessible console text]

## 3. Functional Modules & Public APIs
- **Module 1 (UI/CLI)**: [CLI parser, `--doctor` command, `--json` output, keyboard shortcuts]
- **Module 2 (Core Domain)**: [Domain models, Business logic, Design-by-Contract]
- **Module 3 (Data/Storage)**: [Atomic transactions, snapshot management, connection pools]

## 4. Verification & Quality Gates
- **Automated Tests**: Unit & Failure-mode integration tests with AAA pattern
- **AST & Schema Validation**: 100% compliance with `validate_code.py --strict`
```

---

## 3. Project Mental Topology (`project_mindmap.md`)

```markdown
# Project Mental Topology & Module Map

## 1. Visual Component Hierarchy
\`\`\`mermaid
graph TD
    A[Entry Point: main.py / Program.cs] --> B[UI / Presentation Layer]
    B --> C[Core Business Domain & Contracts]
    C --> D[Data Persistence & Atomic I/O]
    C --> E[External Services & APIs]
\`\`\`

## 2. Module Roster & Contracts
| Module / Path | Responsibilities | Key Dependencies | Invariants |
| :--- | :--- | :--- | :--- |
| `src/ui/` | Accessible UI / CLI | `core/` | Keyboard-first, `--doctor` command |
| `src/core/` | Domain logic & DbC | None (Pure) | Zero UI dependencies, strict types |
| `src/storage/`| Persistence layer | SQLite / Filesystem | Atomic I/O (write `.tmp` + rename) |
```

---

## 4. Real-Time Task Tracking (`tasks.md`)

```markdown
# Project Execution Tracker

## Phase 1: Scoping & Reference Ingestion
- [x] Compile `PRD.md` and `project_spec.json` [Owner: Lead Orchestrator]
- [x] Ingest `docs/` into `references_manifest.json` [Owner: Subagent A]
- [x] Map architecture in `project_mindmap.md` [Owner: Subagent B]

## Phase 2: Polyglot Implementation
- [ ] Implement Persistence layer with Atomic I/O [Owner: Subagent C]
- [ ] Implement Core Domain with Design-by-Contract [Owner: Subagent C]
- [ ] Implement Accessible UI/CLI with `--doctor` & `SIGINT` [Owner: Subagent C]

## Phase 3: QA & Verification
- [ ] Write Unit & Failure-Mode Tests [Owner: Subagent D]
- [ ] Execute `validate_code.py --strict` [Owner: Subagent F]
- [ ] Output `COMPLETION_REPORT.md` with Verification Seal [Owner: Subagent F]
```

---

## 5. 3-Tier Polyglot Architecture Standards

```text
MyProject/
├── PRD.md                         # Human requirements contract
├── project_spec.json              # Machine-readable project spec
├── project_mindmap.md             # Visual component hierarchy
├── tasks.md                       # Real-time task tracker
├── src/
│   ├── ui/                        # Presentation & CLI / GUI layer
│   ├── core/                      # Pure domain models & algorithms
│   └── storage/                   # Database & atomic filesystem I/O
├── tests/                         # Unit & failure-mode integration tests
├── scripts/                       # Local build and verification helpers
└── run.sh / run.bat               # 1-click execution launcher
```