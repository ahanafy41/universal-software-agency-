# Universal AI Software Agency - Agent Execution Guide

This document defines runtime behavior and execution invariants for AI agents running within this repository.

## Non-Negotiable Operational Rules

1. **Hierarchy**: The main agent acts as the Lead Orchestrator. Never perform heavy analytical tasks in the main loop; always delegate to specialized subagents.
2. **Blast Radius Limiter**: Changes must be surgical and strictly localized to the target AST node or function.
3. **Turn-by-Turn Scoping**: Ask strictly ONE question per message when scoping new requirements or investigating ambiguous bugs.
4. **Backup Invariant**: Always snapshot files to `.backups/<timestamp>/` before mutating them.
5. **Real-Time Tracking**: Maintain and update `tasks.md` (or `debug_tasks.md` and `debug_manifest.json`) after each step.
6. **AST Validation**: Always validate modified files with `python3 scripts/validate_code.py <file>` before declaring completion.