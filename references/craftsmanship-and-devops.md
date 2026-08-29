# Human-Grade Craftsmanship, Live Search & DevOps Playbook

This playbook establishes the technical engineering pillars, live web research protocols, blast-radius code preservation controls, and multi-stage packaging blueprints across all languages.

---

## 1. Mandatory Live Web & 2026 SDK Search Gate

To prevent hallucinated APIs, breaking changes, and outdated syntax:
1. **Compulsory Search Invariant**: Every subagent is mandated to query Google Search / official developer documentation for modern 2026 library signatures before writing code.
2. **Targeted Queries**: Search exact error messages, official SDK upgrade guides, and GitHub Issues for modern frameworks.
3. **Symbol Verification**: Verify all methods, types, and parameters against live 2026 documentation.

---

## 2. 10 Pillars of Human-Grade Senior Craftsmanship

1. **Mandatory Human-in-the-Loop Approval Gate**: Stop and wait for user approval on all specs, RFCs, and patch plans.
2. **Defensive Engineering & Atomic I/O**: Write to `.tmp` file, flush, and atomically replace to prevent corruption.
3. **Actionable Error Messages**: 3-part messages (What failed, Why it failed, Actionable fix).
4. **Self-Check Diagnostic (`--doctor`)**: CLI/server flag to validate dependencies, environment, and connectivity.
5. **Graceful Shutdown (`SIGINT`)**: Clean trap for `Ctrl+C` releasing locks and closing connections safely.
6. **Structured Logging**: Standard log levels (`DEBUG`, `INFO`, `WARN`, `ERROR`) supporting `--verbose` and `--json`.
7. **Universal Accessibility (A11y)**: 100% keyboard navigable, semantic ARIA landmarks, and clean terminal outputs.
8. **Failure-Mode Testing**: AAA pattern testing edge cases, network timeouts, and malformed inputs.
9. **Blast Radius Limiter**: Restrict code churn strictly to diagnosed fault nodes.
10. **Pre-Mutation Snapshot**: Always execute `backup_manager.py` before modifying existing files.

---

## 3. DevOps, CI/CD & Automated Packaging

- **Multi-Stage Dockerfiles**: Lean container builds isolating compile-time dependencies.
- **GitHub Actions CI/CD**: Automated linting, testing, and multi-platform release packaging.
- **1-Click Launchers**: Standalone `run.sh` / `run.bat` scripts for friction-free execution.
