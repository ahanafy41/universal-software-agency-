# Universal AI Software Engineering Agency: Agent Integration Guide

This guide explains how autonomous AI agents, orchestrators, and prompt pipelines integrate with and leverage the Universal AI Software Engineering Agency skill.

---

## 1. High-Level Agent Integration Flow

```text
┌───────────────────────────┐
│     User Task Request     │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│   Dual Scoping Protocol   │
│ (Interactive / Fast-Track)│
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ Reference Knowledge Ingest│
│ (references_manifest.json)│
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ Architectural Blueprinting│
│    (project_mindmap.md)   │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│  Pre-Mutation Snapshots   │
│   (backup_manager.py)     │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ Polyglot Code Synthesis   │
│   (Human-Grade Craft)     │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ AST & Schema Verification │
│    (validate_code.py)     │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ Delivery & Seal of Quality│
│   (COMPLETION_REPORT.md)  │
└───────────────────────────┘
```

---

## 2. Key Orchestration Invariants for AI Agents

1. **Subagent Delegation is Mandatory**: The root orchestrator agent must never bloat its own primary context window with deep file dumps or multi-page documentation parsing. Always spawn specialized worker subagents (`invoke_subagent`).
2. **Proactive Live 2026 Google Search**: When encountering any third-party framework, package, or API signature, the agent is strictly required to query Google Search for official 2026 documentation.
3. **Strict Reference Grounding**: When custom user documentation is provided under `docs/` or `references/`, the agent must parse it into `references_manifest.json` before implementing code.
4. **Non-Destructive Mutation**: When diagnosing or modifying existing code, the agent must run `backup_manager.py backup <file>` and pinpoint the exact AST node before modifying any code.
5. **Deterministic Verification**: Every deliverable must be validated using `validate_code.py --strict` before presenting the final verification seal.