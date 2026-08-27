# 🎯 Senior Craftsmanship, Reference Ingestion & DevOps Playbook

This playbook establishes the technical standards, file formats, and execution rules for **Human-Grade Code Craftsmanship**, **Zero-Skipping Reference Ingestion**, and **Production Deployment**.

---

## 1. The 6 Pillars of Senior Human Craftsmanship

All code produced by any subagent must rigorously adhere to these 6 principles:

### 1.1. Defensive Engineering & Atomic File I/O
- **Atomic File Writes**: Never overwrite a target file directly. Write to a temporary file (`.tmp`) in the same directory, flush/sync to disk, and perform an atomic rename.
- **Network Resilience**: Wrap all external HTTP and RPC calls in exponential backoff retries with explicit timeout limits.

### 1.2. Actionable Error Messages
Errors must never be silent or generic. Every thrown or logged exception must clearly answer:
1. **What failed**: (e.g., `Failed to bind to port 8080`).
2. **Why it failed**: (e.g., `Address already in use by another process PID 1234`).
3. **Actionable recovery**: (e.g., `Specify a different port via --port or terminate the conflicting process`).

### 1.3. Built-In `--doctor` Self-Check
Every CLI utility or service must implement a `--doctor` diagnostic command that verifies:
- Runtime environment and dependencies.
- Required system permissions and disk space.
- Configuration file schema validity.

### 1.4. Graceful Shutdown & Signal Traps
- Intercept termination signals (`SIGINT`, `SIGTERM`, `Ctrl+C`).
- Safely close database connection pools, flush pending logs, and release acquired file locks.

### 1.5. Structured Logging & Clean Terminal Ergonomics
- Replace raw console print statements with structured logging libraries.
- Support standard log levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`.
- Provide `--verbose` and `--json` command-line flags.

### 1.6. Universal Accessibility (A11y) & Keyboard-First Design
- Full keyboard operability (`Tab`, `Shift+Tab`, `Enter`, `Space`, Arrows).
- Screen-reader friendly terminal outputs without flashing escape codes.
- Explicit ARIA landmarks and WCAG AAA color contrast compliance in GUI/Web applications.

---

## 2. Mandatory Zero-Skipping Reference Ingestion Protocol

When documentation, SDK references, or API contracts are provided:

1. **Subagent A Ingestion**: Subagent A parses reference files in `docs/` or `references/` line-by-line.
2. **Extraction into `references_manifest.json`**: Extract all symbols, function signatures, data types, and parameters into a structured manifest adhering to `references/agency-schemas.json`.
3. **Deterministic Coverage Verification**: Run `python3 scripts/validate_code.py --manifest references_manifest.json <implementation_file>` to ensure 100% adherence.

---

## 3. DevOps, CI/CD & Production Packaging

- **Multi-Stage Dockerfile**: Keep final container images lean by separating the build environment from the runtime container.
- **GitHub Actions CI**: Automated linting, static analysis, unit test suites, and release artifact packaging.
