# 🗺️ Project Lifecycle & Architecture Playbook

This playbook governs project scoping, specification blueprints, architecture topologies, and task management.

---

## 1. Dual Scoping Protocols

The agency operates in two scoping modes based on project clarity:

### 1.1. Interactive Mode (Default / Open-Ended)
When requirements are open-ended or ambiguous:
- Ask **strictly ONE focused discovery question per turn**.
- Cycle through the 6 discovery pillars:
  1. Business Value & Core Objective
  2. Reference Documents & External APIs
  3. Technology Stack & Runtime
  4. Data Persistence & Storage
  5. Accessibility (A11y) & UX
  6. Error Handling & Edge Cases

### 1.2. Fast-Track Mode (PRD Provided)
When complete specifications are provided upfront:
- Bypass exploratory questions immediately.
- Compile `PRD.md`, `project_spec.json`, and `tasks.md` in the first turn.

---

## 2. 3-Tier Clean Architecture Pattern

Projects must maintain a clear separation of concerns across 3 distinct tiers:

```text
┌────────────────────────────────────────────────────────┐
│  Tier 1: UI / CLI / Accessibility (A11y / Presentation) │
└───────────────────────────┬────────────────────────────┘
                            │ (Typed Contracts)
┌───────────────────────────▼────────────────────────────┐
│  Tier 2: Core Domain Logic & Business Rules            │
└───────────────────────────┬────────────────────────────┘
                            │ (Abstract Interfaces)
┌───────────────────────────▼────────────────────────────┐
│  Tier 3: Data Engine / Storage / External APIs         │
└────────────────────────────────────────────────────────┘
```

---

## 3. Project Mental Topology (`project_mindmap.md`)

Before generating complex features, create `project_mindmap.md` containing:
- Mermaid topology diagram mapping caller graphs and data flow.
- Directory breakdown and entry-point index.
