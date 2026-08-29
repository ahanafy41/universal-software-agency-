# Human-Grade Craftsmanship, Code Preservation, Reference Ingestion & DevOps Playbook

This consolidated reference defines the operational, architectural, and quality standards enforced across all worker subagents to ensure production-grade software engineering, rigorous reference ingestion, strict code preservation, and robust packaging across all languages.

---

## 1. The 6 Pillars of Senior Human-Grade Software Engineering

Every line of code, CLI interface, API, or GUI authored by the agency must reflect senior engineering craftsmanship:

### 🌟 Pillar 1: Atomic File I/O & Defensive Resilience
- Never overwrite destination files directly in place.
- **Pattern**: Write to a temporary file (`.tmp`), flush buffers to disk (`flush()` + `fsync`), and perform an atomic rename/replace.
- Protect against sudden power loss, process termination, or concurrent access collisions.

### 🌟 Pillar 2: 3-Part Actionable Error Messages
Every handled exception and user-facing error message must strictly provide 3 components:
1. **What Failed**: Clear explanation of the operation that was interrupted.
2. **Why It Failed**: The exact underlying technical cause or unmet precondition.
3. **How to Fix**: Concrete, actionable recovery steps (e.g., exact command to run, file permission to check, or configuration key to fix).

### 🌟 Pillar 3: Built-In Environment Self-Check (`--doctor`)
- All CLI utilities, server daemons, and standalone applications must provide a `--doctor` (or `doctor`) subcommand.
- Validates runtime prerequisites: directory permissions, database connection strings, external binary dependencies, and configuration presence.
- Returns a structured status report (`[PASS]`, `[WARN]`, `[FAIL]`) with explicit remedies for any failed checks.

### 🌟 Pillar 4: Graceful Process Shutdown & Signal Trapping
- Always register signal handlers (`SIGINT`, `SIGTERM`) across all runtimes (Python `signal`, Node.js `process.on`, Go `os.Interrupt`, C# `AppDomain.CurrentDomain.ProcessExit`).
- Flush and close open file handles, commit or rollback in-flight database transactions, and terminate child worker threads cleanly.

### 🌟 Pillar 5: Structured Logging & Clean Telemetry
- Never use unformatted print statements (`print()`, `console.log()`) for operational logging.
- Use structured loggers supporting standard severity levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
- Support CLI flags: `--verbose` (enables DEBUG output), `--quiet` (suppresses non-error output), and `--json` (outputs machine-parsable JSON lines).

### 🌟 Pillar 6: Universal Accessibility (A11y) & Keyboard-First Design
- **Keyboard-First**: 100% of functionality accessible without a mouse (`Tab`, `Shift+Tab`, `Enter`, `Space`, Arrows).
- **Screen-Reader Compatibility**: Explicit ARIA roles, semantic landmarks, live regions for dynamic alerts, and high-contrast color ratios.
- **Accessible CLI Output**: Clean formatting, avoid flashing ANSI characters that crash Braille displays or screen readers.

---

## 2. Zero-Skipping Reference Ingestion Protocol

When custom API documentation, schemas, or specs exist in `docs/` or `references/`, Subagent A must execute the Zero-Skipping protocol:

1. **Full Symbol Extraction**: Extract every function signature, argument type, return type, exception, and schema definition.
2. **Structured JSON Manifestation**: Generate `references_manifest.json` conforming to `references/agency-schemas.json`.
3. **Automated Coverage Check**: Execute `python3 scripts/validate_code.py --manifest references_manifest.json <file>` to verify 100% compliance.

---

## 3. Strict Blast Radius Control & Pre-Mutation Safeguards

When fixing bugs or refactoring existing code, Subagent F enforces strict isolation:

```text
┌────────────────────────────────────────────────────────┐
│ 1. Pre-Mutation Snapshot: python3 backup_manager.py     │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. Pinpoint Surgical AST Node in debug_tasks.md        │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. Apply Targeted Patch Exclusively to Diagnosed Node   │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. Verify Diff Bounds: python3 diff_verifier.py         │
└────────────────────────────────────────────────────────┘
```

---

## 4. DevOps, Multi-Stage Packaging & CI/CD Standards

Subagent H packages deliverables for production distribution:

- **Multi-Stage Dockerfiles**: Separate build-time dependencies from lightweight production runtimes with non-root security users.
- **GitHub Actions Workflows**: Automated linting, test execution, coverage gates, and multi-platform artifact packaging.
- **1-Click Execution Launchers**: Cross-platform execution scripts (`run.sh` / `run.bat`) that check dependencies and start the app cleanly.
