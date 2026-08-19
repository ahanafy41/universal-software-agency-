# 🚀 Universal Software & AI Engineering Agency
### Autonomous Multi-Agent Software Architecture for Gemini Spark & AI Agent Frameworks

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Architecture: Multi-Agent](https://img.shields.io/badge/Architecture-Multi--Agent-blue.svg)](SKILL.md)
[![Standard: PRD & Spec-Driven](https://img.shields.io/badge/Standard-PRD%20%26%20JSON%20Manifest-green.svg)](references/prd-template.md)
[![Offline-First: Supported](https://img.shields.io/badge/Offline--First-100%25-brightgreen.svg)](references/architecture-blueprints.md)

An enterprise-grade, framework-agnostic virtual software engineering agency that plans, scopes, architects, implements, tests, and packages production-grade software across **any language or framework** (C# .NET, Python, TypeScript/JavaScript, Rust, Go, Shell, etc.).

Designed for seamless deployment across **Google Gemini Spark**, **OpenAI Codex**, **Cursor**, **Windsurf**, and custom **Model Context Protocol (MCP)** agent systems.

---

## 🏛️ Multi-Agent Architecture

The agency operates strictly as a hierarchical **Orchestrator-Workers Multi-Agent Graph**:

```text
                                  ┌────────────────────────────────┐
                                  │   Orchestrator Lead Agent      │
                                  │ (Turn-by-Turn Scoping & PRD)   │
                                  └───────────────┬────────────────┘
                                                  │
                ┌─────────────────────────────────┼─────────────────────────────────┐
                ▼                                 ▼                                 ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐ ┌───────────────────────────────┐
│ Track A: Desktop & Offline    │ │ Track B: Universal Web / API  │ │ Track C: Automation & Tools   │
│ (C# .NET / Python GUI / App)  │ │ (Single-File / Local / Cloud) │ │ (CLI / Batch / Shell scripts) │
└───────────────────────────────┘ └───────────────────────────────┘ └───────────────────────────────┘
                                                  │
                                                  ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Phase 0: Turn-by-Turn Scoping, PRD Generation (`PRD.md`) & JSON Manifest (`project_spec.json`)     │
│ • ONE question per turn across Product/Business & Technical pillars OR Ingest existing codebase    │
│ • Ingests user-supplied references (`docs/`, `references/`, Markdown guides, JSON schemas)        │
│ • Compiles human-readable `PRD.md` (Product Requirements Document) & machine-readable spec.json    │
└─────────────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                                  ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Phase 1: Live Research, Custom Knowledge Ingestion & Architecture (Parallel Subagents)            │
│ • Product Manager & Business Strategist: Problem-solution fit, MVP feature prioritization (MoSCoW)│
│ • Knowledge Base & API Reference Specialist: Parses user docs, JSON schemas, custom SDKs & specs  │
│ • Live API & SDK Documentation Specialist: Queries web for latest SDKs, AI agent APIs & docs      │
│ • System & Offline Data Architect: 3-tier architecture, SQLite/LiteDB schemas, offline-first flow │
│ • Security, Permissions & Edge-Case Specialist: Exception boundaries, OS permissions & safeguards │
└─────────────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                                  ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Phase 2: Pre-Mutation Backup, Surgical Assembly & Step-by-Step Review (Assembly Subagents)        │
│ • Automated Pre-Mutation Backup Engine: Snapshots target file to `.backups/<timestamp>/`          │
│ • Core Polyglot Developer: Schema-driven code generation, Design-by-Contract (`Requires`/`Ensures`)│
│ • Step-by-Step Peer Reviewer: Reviews code diff against contract & reference specs BEFORE disk    │
│ • UI/UX & Accessibility Architect: High contrast, non-blocking UI threads, keyboard navigation   │
│ • Tooling & Release Packager: Clean project layout, `.csproj`/`pyproject.toml`, platform-appropriate 1-click build/launch scripts│
└─────────────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                                  ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Phase 3: QA, Automated Static Analysis & Delivery (Verification Subagents)                        │
│ • QA & AST Verification Specialist: Runs `validate_code.py`, syntax parse & 3-branch reflexion   │
│ • Reference Conformance Validator: Cross-checks code against user-provided schemas & API symbols  │
│ • Monolithic Single-Project Delivery: Writes clean, self-contained project files (No chat dump)   │
│ • Manifest Synchronizer: Updates `project_spec.json` with new modules, timestamps & checksums     │
│ • Citizen UX & Documentation Specialist: Friendly 3-step run guide, error log troubleshooting   │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## ✨ Key Capabilities

1. **Interactive Turn-by-Turn Scoping (حظر التخمين)**:
   - Asks **exactly ONE question per turn** across 6 core discovery pillars (Target user, custom knowledge, track, offline storage, UX, resilience).
   - Generates formal **`PRD.md`** (for humans) and **`project_spec.json`** (for machines) before writing code.

2. **Custom Knowledge & Reference Ingestion (استيعاب المراجع والتوثيق)**:
   - Ingests Markdown API manuals (`docs/`), JSON Schemas (`references/`), OpenAPI contracts, and code stubs.
   - **Zero-Hallucination Grounding**: Locks all code synthesis strictly to user-provided reference definitions.

3. **Brownfield Codebase Ingestion (استيعاب المشاريع القائمة)**:
   - Scans and reverse-engineers existing codebases into structured `PRD.md` and `project_spec.json` manifests.

4. **Zero-Data-Loss Pre-Mutation Backups (`.backups/`)**:
   - Automatically snapshots files before any mutation into `.backups/YYYYMMDD_HHMMSS/`.
   - Guaranteed one-click rollbacks if builds or tests fail.

5. **Design-by-Contract (DbC) & Small Model Superpowers**:
   - Enforces `Requires` (preconditions) and `Ensures` (postconditions) on all routines.
   - 3-branch reflexion debugging (Contract breach, State misalignment, I/O boundary).

6. **1-Click Launchers & Defensive Logging**:
   - Generates platform-appropriate 1-click build and launch scripts (`build.sh`, `build.bat`, `Makefile`, `npm run build`).
   - Global exception handling logging to `app_errors.log`.

---

## 📁 Repository Structure

```text
universal-software-agency/
├── SKILL.md                              # Core AI Agent Skill Definition
├── README.md                             # Repository Overview & Architecture Guide
├── AGENT_GUIDE.md                        # Direct Instructions for AI Agents & LLM Clients
├── LICENSE                               # MIT Open Source License
├── .gitignore                            # Standard Git ignore rules
├── references/
│   ├── custom-knowledge-ingestion-guide.md # Guide for ingesting custom docs & schemas
│   ├── prd-template.md                   # Product Requirements Document Template
│   ├── project-manifest-schema.json      # JSON Schema for project_spec.json
│   ├── product-scoping-guide.md          # PM scoping & MoSCoW prioritization
│   └── architecture-blueprints.md        # File structures for C#, Python, & Web
├── scripts/
│   └── validate_code.py                  # Multi-language AST validator (Py, C#, JS, JSON)
└── examples/
    └── sample-project-walkthrough.md     # Step-by-step example with custom JSON schema
```

---

## 🛠️ Installation & Setup

### 1. For Google Gemini Spark & Agent Workspaces
1. Download or clone this repository.
2. In your Gemini agent environment, use the **Skill Creator / Skill Manager**:
   - Set skill name to `universal-software-agency`.
   - Import the repository directory containing `SKILL.md`, `references/`, and `scripts/`.
3. The agency triggers automatically whenever you ask to build, refactor, or scope software applications.

### 2. For External Multi-Agent Frameworks & MCP
1. Clone this repository into your local workspace:
   ```bash
   git clone https://github.com/<your-username>/universal-software-agency.git
   ```
2. Reference `SKILL.md` in your agent system prompt or environment config:
   ```markdown
   Include instructions from: universal-software-agency/SKILL.md
   ```

### 3. For Cursor / Windsurf / VS Code Roo Code / Cline
1. Place the repository in your project's `.agent/skills/` or `.cursorrules` / `.windsurfrules` path.
2. Add a pointer to `SKILL.md` to ground the model in the Orchestrator-Workers architecture.

---

## 📖 Quick Usage Example

1. **Start a Project**:
   > *"I want to build a lightweight desktop tool in C# that processes invoice PDFs and stores summaries in an offline SQLite database."*
2. **Interactive Scoping**:
   The agent initiates turn-by-turn scoping (one question per message) to clarify user persona, offline requirements, and custom schemas.
3. **Supply Custom Docs (Optional)**:
   > *"Here is the JSON schema of our invoice format in `references/invoice_schema.json`."*
4. **PRD & Code Generation**:
   The agent generates `PRD.md`, `project_spec.json`, strongly-typed models, business logic, UI, and platform-appropriate build/launch scripts.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
