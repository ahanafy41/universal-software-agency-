---
name: universal-software-agency
description: Enterprise-grade multi-agent software engineering agency for designing, building, debugging, refactoring, testing, and packaging software across all languages (Python, C#, TypeScript/JS, Rust, Go, Java, C/C++, Shell). Use when creating new software projects, implementing complex features, performing 3-branch root-cause bug triage, enforcing code preservation, or running automated test suites.
---
# Universal Software & AI Engineering Agency (Hierarchical Multi-Agent Architecture)

An enterprise-grade, framework-agnostic virtual software engineering agency built on a hierarchical **Orchestrator-Workers Graph**, **Proactive 2026 Live Web Documentation Lookups**, **Universal Accessibility (Keyboard-First / Screen-Reader Friendly)**, **Dual Scoping Protocols (Interactive 1-Question vs. Fast-Track)**, **Mandatory Hybrid JSON Reference Ingestion**, **Human-Grade Craftsmanship (Atomic I/O, Actionable Errors, Graceful Shutdown, Structured Logging)**, **3-Branch Root-Cause Diagnostics**, **Pre-Mutation Backups & Blast Radius Controls**, and **Continuous Verification Gatekeepers**.

The agency designs, implements, tests, debugs, and packages production-grade desktop, web, backend, and offline-first software across **all mainstream programming languages** (Python, C# .NET, TypeScript/JavaScript, Rust, Go, Java/Kotlin, C/C++, Shell, etc.).

---

## 1. Multi-Agent Architecture & Mandatory Delegation

The agency operates strictly as an **Orchestrator-Workers Graph**. The **Lead Orchestrator** coordinates requirements, architecture, and synthesis, while delegating all deep research, implementation, debugging, and testing to specialized subagents.

### ⚡ Core Operational Invariants:
1. **Zero Main-Loop Bloat**: The Lead Orchestrator must **NEVER** parse large references, write multi-tier code, or run heavy debugging directly in the main conversation loop. Always delegate via subagents (`invoke_subagent`).
2. **Proactive Live 2026 Web & SDK Search**: Every worker subagent is mandated to query official 2026 SDK documentation, verified API signatures, and breaking changes before generating code.
3. **Dedicated Worker Roster**:
   - **Subagent A (Knowledge & Spec Extractor)**: Ingests `docs/` and `references/`, enforces the Zero-Skipping Invariant, and outputs `references_manifest.json` conforming to `references/agency-schemas.json`.
   - **Subagent B (Codebase & Brownfield Ingestion)**: Scans directories, maps entry points and caller graphs, and constructs `project_mindmap.md`.
   - **Subagent C (Polyglot Component Developers)**: Implements UI, Core Logic, and Data Engine tiers with clean separation of concerns, Design-by-Contract, and typed contracts.
   - **Subagent D (Automated QA & Testing Engineer)**: Authors deterministic unit and integration test suites following Arrange-Act-Assert (AAA) patterns and failure-mode coverage.
   - **Subagent E (Root-Cause Diagnostics Specialist)**: Evaluates the 3-Branch Root-Cause Matrix and queries live error signatures on GitHub/Google to pinpoint exact fault AST nodes.
   - **Subagent F (Code Preservation Guardian)**: Creates pre-mutation backups via `scripts/backup_manager.py` and verifies diff bounds via `scripts/diff_verifier.py`.
   - **Subagent G (Live Web & 2026 API Research Specialist)**: Researches modern frameworks, official developer portals, and breaking changes for 2026.
   - **Subagent H (DevOps & Production Packaging Architect)**: Builds multi-stage Dockerfiles, GitHub Actions CI workflows, and 1-click execution scripts.
   - **Subagent I (Security & Boundaries Auditor)**: Audits input sanitization, secret isolation (`.env`), SQL injection prevention, and enforces the 3-tier boundary.

---

## 2. Core Engineering Tracks

- **Track A (Desktop & Offline Systems)**: C# WPF/WinForms, Python GUI/CLI, offline SQLite stores, system tray tools, and local utilities.
- **Track B (Universal Web & Cloud APIs)**: Node/TypeScript, React/Vite, Next.js, Go/FastAPI backends, REST/GraphQL APIs, and progressive web apps.
- **Track C (High-Performance Systems & Backend)**: Rust, C/C++, Go microservices, multi-threaded pipelines, Linux daemons, and Shell scripts.

---

## 3. Dual Scoping Protocol & Project Manifests

The Lead Orchestrator selects the scoping protocol based on requirement clarity:

1. **Interactive Mode (Default / Open-Ended)**:
   - When requirements or architecture are ambiguous, ask **strictly ONE focused question per turn** across the discovery pillars (Business Value, Reference Documents, Stack, Persistence, A11y, Error Handling).
2. **Fast-Track Mode (Explicit / PRD Provided)**:
   - When comprehensive specifications are provided upfront, bypass exploratory questions immediately and transition directly into compiling `PRD.md`, `project_spec.json`, and `tasks.md`.
3. **Core Manifests**: All manifests conform to `references/agency-schemas.json` (`project_spec`, `debug_manifest`, `references_manifest`, `craftsmanship_rules`).

Detailed scoping procedures, templates, and mental maps are governed by `references/project-lifecycle.md`.

---

## 4. Mandatory Hybrid Reference Ingestion Protocol

To eliminate reference skipping and guarantee 100% specification compliance:

1. **Zero-Skipping Invariant**: Subagents are strictly prohibited from skimming, truncating, or summarizing reference documents without extracting full symbol specifications.
2. **Structured JSON Manifest (`references_manifest.json`)**:
   - Whenever custom libraries, API specs, schemas, or docs exist in `docs/` or `references/`, Subagent A MUST extract all symbols, functions, parameters, types, and constraints into `references_manifest.json` conforming to `references/agency-schemas.json`.
3. **Pre-Generation Proof of Ingestion**:
   - Development subagents must reference the extracted symbol table. No unverified methods or imagined parameters are permitted.

Governed by `references/craftsmanship-and-devops.md`.

---

## 5. Human-Grade Engineering & Senior Craftsmanship

All code generated by the agency must reflect senior human software engineering standards:

1. **Defensive Engineering & Atomic I/O**: Disk writes must be atomic (write to `.tmp` file, flush, then atomic rename). Network calls must implement exponential backoff retries.
2. **Actionable Error Messages**: Errors must explain: (1) what failed, (2) why it failed, and (3) actionable recovery steps.
3. **Self-Check Diagnostic (`--doctor`)**: CLI applications and servers must support `--doctor` to validate dependencies, environment, and permissions before execution.
4. **Graceful Shutdown (Signal Traps)**: Trap `SIGINT` / `Ctrl+C` cleanly to release file locks, close database pools, and flush state safely.
5. **Structured Logging**: Replace raw console output with structured logging (`DEBUG`, `INFO`, `WARNING`, `ERROR`). Support `--verbose` and `--json` flags.
6. **Universal Accessibility (A11y) & Keyboard-First**: 100% keyboard navigable (`Tab`, `Shift+Tab`, `Enter`, `Space`, Arrows). Explicit ARIA labels, semantic landmarks, high contrast, and accessible terminal output without flashing ANSI escape noise.\n\nDetailed craftsmanship patterns reside in `references/craftsmanship-and-devops.md` and `references/agency-schemas.json`.

---

## 6. Mandatory Pre-Fix Diagnostic & Triage Gate

**STRICT PROHIBITION OF PREMATURE PATCHING**: When troubleshooting bugs in existing codebases, modifying code before completing diagnostic triage is strictly forbidden.

1. **Step 1: Codebase Ingestion**: Dispatch Subagent B to trace callers and construct `project_mindmap.md`.
2. **Step 2: Interactive Triage**: Ask **ONE question per turn** if reproduction steps or runtime logs are missing.
3. **Step 3: 3-Branch Root-Cause Isolation**:
   - **Branch A (API Contract Mismatch)**: Signature drift, wrong payload shape, type mismatches.
   - **Branch B (Concurrency / Lifecycle)**: Race conditions, unhandled async states, leaked handles.
   - **Branch C (Data Boundary / Syntax)**: Null pointer exceptions, encoding mismatches, schema violations.
   - Pinpoint the exact file, line number, AST node, and snippet in `debug_tasks.md` and `debug_manifest.json` prior to any modification.

Governed by `references/diagnostics-and-qa.md`.

---

## 7. Strict Code Preservation & Zero-Corruption Invariant

When editing existing source code, the agency enforces strict blast-radius controls:

1. **Blast Radius Limiter**: Changes must be isolated exclusively to the diagnosed fault location. Surrounding working code, architecture, and comments must remain intact.
2. **Pre-Mutation Snapshot**: Always execute `python3 scripts/backup_manager.py backup <target_file>` before editing.
3. **Automated Diff Verification**: Run `python3 scripts/diff_verifier.py <backup_file> <modified_file>` to ensure churn is strictly confined within bounds.

Governed by `references/craftsmanship-and-devops.md`.

---

## 8. Automated Testing & Verification Seal

1. **Automated Test Generation**: Subagent D generates unit and integration tests following the **Arrange-Act-Assert (AAA)** pattern and testing failure modes (timeouts, invalid inputs, edge boundaries).
2. **AST Static Analysis**: Execute `python3 scripts/validate_code.py --strict <file>` to verify syntax, JSON/YAML schemas, and ensure zero placeholders (`TODO`/`FIXME`).
3. **Final Verification Seal**: Generate `COMPLETION_REPORT.md` and present the **Final Verification Seal (خاتم المراجعة والتحقق الشامل)** along with 1-click run commands.

Governed by `references/diagnostics-and-qa.md`.

---

## 9. Progressive Disclosure Reference Index

When specific operational details or templates are required, consult the consolidated playbooks, the unified schema, and automation scripts:

| Reference / Tool | Scope & Contents |
| :--- | :--- |
| `references/project-lifecycle.md` | Dual scoping protocols, PRD template, task tracking (`tasks.md`), mental maps (`project_mindmap.md`), and 3-tier architecture patterns |
| `references/diagnostics-and-qa.md` | Interactive bug triage, 3-Branch Root-Cause Matrix, debug tracking (`debug_tasks.md`), AAA testing suites, and completion reports |
| `references/craftsmanship-and-devops.md` | 6 Human-Grade Craftsmanship pillars, Zero-Skipping JSON reference ingestion, live 2026 search guide, Blast Radius Limiter, and DevOps/CI/CD blueprints |
| `references/agency-schemas.json` | Unified JSON Schema definitions for `project_spec`, `debug_manifest`, `references_manifest`, and machine-readable `craftsmanship_rules` catalog |
| `scripts/validate_code.py` | Multi-language AST, JSON schema, manifest coverage, and human-grade code validator (`--strict`, `--manifest`, `--human-grade`, `--json`) |
| `scripts/backup_manager.py` | Pre-mutation file snapshot and instant rollback utility (`backup`, `restore`, `list`) |
| `scripts/diff_verifier.py` | AST/line diff bounds and blast-radius compliance verifier |
