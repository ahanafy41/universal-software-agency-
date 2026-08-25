# Human-Grade Craftsmanship, Reference Ingestion & DevOps Standards (دليل الحرفية البرمجية واستيعاب المراجع والـ DevOps)

Defines senior human engineering standards, reference ingestion rules, code preservation guardrails, and DevOps CI/CD blueprints.

---

## 1. The 6 Pillars of Senior Human Software Engineering

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   🏛️ The 6 Pillars of Senior Human Software Engineering                          │
├───────────────────────────────┬───────────────────────────────┬──────────────────────────────────┤
│ 1. Atomic I/O & Defense       │ 2. Actionable Errors & Doctor │ 3. Graceful Shutdown & Ergonomics│
├───────────────────────────────┼───────────────────────────────┼──────────────────────────────────┤
│ 4. Structured Logging         │ 5. Failure-Mode Testing       │ 6. Universal Accessibility (A11y)│
└───────────────────────────────┴───────────────────────────────┴──────────────────────────────────┘
```

1. **Pillar 1: Defensive Programming & Atomic I/O**
   - Always write data to a temporary file (`.tmp`) and replace the original via an atomic rename operation (`os.replace` in Python, `File.Move` with overwrite in C#).
   - Implement exponential backoff with jitter for network operations.
2. **Pillar 2: Actionable Error Messages & `--doctor` Self-Check**
   - Error messages must answer 3 questions: **What failed? Why did it fail? How does the user fix it?**
   - Provide a built-in `--doctor` / `--check-env` CLI command to verify prerequisites, permissions, and dependencies before running.
3. **Pillar 3: Graceful Shutdown (`SIGINT`) & Clean CLI Ergonomics**
   - Catch termination signals (`SIGINT`, `SIGTERM`, `Ctrl+C`) to flush buffers, close database pools, and delete temporary files cleanly.
   - Support standard flags: `--help`, `--version`, `--verbose`, `--json`.
4. **Pillar 4: Structured Logging over Raw Prints**
   - Eliminate raw unformatted `print()` / `Console.WriteLine()` statements in production code. Use leveled loggers (`DEBUG`, `INFO`, `WARN`, `ERROR`).
5. **Pillar 5: Failure-Mode & Edge-Case Testing**
   - Never test only the happy path. Test network cuts, disk full conditions, malformed payloads, and race conditions.
6. **Pillar 6: Built-in Universal Accessibility (Keyboard-First / Screen-Reader Friendly)**
   - 100% keyboard operability (`Tab`, `Shift+Tab`, `Enter`, `Esc`), explicit ARIA landmarks, high contrast visual cues, and accessible console output without flashing ANSI escape codes.

---

## 2. Zero-Skipping Mandatory Reference Ingestion Protocol

When user-supplied documentation or proprietary SDK guides exist in `docs/` or `references/`:
1. **Zero-Skipping Invariant**: The agent is strictly prohibited from summarizing, skimming, or skipping sections.
2. **Symbol Table Extraction in JSON**: Subagent A must parse reference files and emit `references_manifest.json` conforming to `references/agency-schemas.json`.
3. **Coverage Verification**: Subagent A generates `references_coverage_matrix.md` certifying 100% mapping of exported classes, methods, parameters, and constraints before writing code.
4. **Deterministic Validation**: `scripts/validate_code.py --manifest references_manifest.json` checks that all extracted symbols are implemented.

---

## 3. Strict Code Preservation & Blast Radius Limiter

1. **Pre-Mutation Snapshot**: Run `python3 scripts/backup_manager.py backup <target_file>` before any edit.
2. **Blast Radius Limiter**: Changes must be isolated exclusively to the target fault line or AST node. The agent is strictly forbidden from modifying surrounding working code.
3. **Diff Verification**: Run `python3 scripts/diff_verifier.py <backup_file> <modified_file>` to ensure code churn stays within bounds.

---

## 4. Proactive Live 2026 Google Search Mandate

Every worker subagent is equipped and mandated to query Google Search for:
- Official 2026 SDK documentation and modern framework idioms.
- Exact error signatures and GitHub Issues triage.
- Deprecation warnings and breaking changes in recent library versions.

---

## 5. DevOps & CI/CD Packaging Blueprints

### Multi-Stage Production Dockerfile Pattern:
```dockerfile
# Multi-stage lightweight build
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.12-slim AS runner
WORKDIR /app
RUN useradd -u 1000 appuser && chown -R appuser:appuser /app
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appuser src/ ./src/
USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
CMD ["python3", "src/main.py"]
```

### 1-Click Launchers (`run.sh` / `run.bat`):
- Automatically check runtime prerequisites.
- Install dependencies into virtual environments if missing.
- Launch the application smoothly.