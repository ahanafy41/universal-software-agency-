# Project Lifecycle, Scoping & Architecture Playbook (`project-lifecycle.md`)

This playbook governs the end-to-end inception, scoping, structural design, and real-time execution tracking for all software built by the Universal Software & AI Engineering Agency across all languages.

---

## 1. Dual Scoping Protocol

The Lead Orchestrator selects the scoping protocol based on requirement clarity:

### 🎯 Mode 1: Interactive Scoping Protocol (Default / Ambiguous)
When specifications are open-ended, ask **strictly ONE focused question per turn** across the discovery pillars:
1. **Business Value & Core Users**: What is the core problem and who are the primary users?
2. **Reference Documents & Existing Assets**: Are there custom APIs, schemas, or reference code?
3. **Target Technology Stack**: Which programming language, framework, and database?
4. **Persistence & Data Tier**: Local SQLite, remote PostgreSQL, Redis, or flat-file store?
5. **Accessibility & Ergonomics**: Keyboard shortcuts, screen-reader support, CLI vs. GUI?
6. **Error Recovery & Logging**: Structured JSON logs, retry policies, doctor diagnostics?

### ⚡ Mode 2: Fast-Track Scoping Protocol (Explicit / PRD Provided)
When complete specifications are provided upfront, bypass exploratory questions immediately. Compile `PRD.md`, `project_spec.json`, and `tasks.md` in one turn and initiate subagent dispatch.

---

## 2. 3-Tier Polyglot Architecture & Domain Isolation

All production software must adhere to clean 3-tier domain separation:

```text
┌────────────────────────────────────────────────────────┐
│ Tier 1: User Interface / CLI / API Endpoints (UI)      │
│ • Keyboard navigation, command routing, ARIA landmarks │
└──────────────────────────┬─────────────────────────────┘
                           │ Typed Contracts / DTOs
                           ▼
┌────────────────────────────────────────────────────────┐
│ Tier 2: Core Domain Logic & Business Rules (Logic)     │
│ • Design-by-Contract, pure algorithms, validations     │
└──────────────────────────┬─────────────────────────────┘
                           │ Abstract Repository Interfaces
                           ▼
┌────────────────────────────────────────────────────────┐
│ Tier 3: Data Engine & Infrastructure (Data)            │
│ • Atomic disk I/O, SQLite/Postgres connectors, network  │
└────────────────────────────────────────────────────────┘
```

---

## 3. Real-Time Task & Progress Tracking (`tasks.md`)

Every project tracks progress through `tasks.md` using the standard status markers:
- `- [ ]`: Pending task.
- `- [/]`: In-progress task.
- `- [x]`: Completed and verified task.

---

## 4. Formal Project Manifest Schema (`project_spec.json`)

All project specifications are persisted as machine-readable JSON matching the schema in `references/agency-schemas.json`:
- `project_id`: Unique slug.
- `project_name`: Human-readable name.
- `architecture_tier`: Selected architectural pattern.
- `target_stack`: Language, frameworks, testing tools.
- `modules`: List of discrete components with defined responsibilities.
