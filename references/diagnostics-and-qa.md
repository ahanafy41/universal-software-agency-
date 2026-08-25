# Diagnostics, Root-Cause Debugging & QA Standards (دليل التشخيص وضمان الجودة)

Defines the mandatory gates and methodologies for troubleshooting bugs, diagnosing root causes, authoring automated test suites, and certifying deliverables.

---

## 1. Mandatory Pre-Fix Diagnostic & Triage Gate

### 🚫 STRICT PROHIBITION OF PREMATURE PATCHING
When a bug or regression is reported in an existing codebase, the AI agent is **STRICTLY FORBIDDEN from immediately modifying code**. It must follow this 3-step gate:

### Step 1: Deep Codebase & Context Ingestion (Subagent B)
- Inspect entry points, module hierarchy, and caller graphs without guessing.
- Map affected modules and active data flows in `project_mindmap.md`.

### Step 2: Turn-by-Turn Diagnostic Triage
- If reproduction details, logs, or environment context are missing, ask **strictly ONE focused diagnostic question per turn**:
  1. What was the exact command or action performed immediately before failure?
  2. What is the OS, runtime version, and installed dependency versions?
  3. What was the expected behavior versus the actual behavior?
  4. What exact error message, stack trace, or log output was emitted?

### Step 3: Diagnostic Hypothesis & Pinpointing
- Evaluate the universal 3-Branch Root-Cause Matrix backed by live error searches on GitHub/Google.
- Record the **Exact Location Pinpoint** (File path, line range, AST node, symbol) in `debug_tasks.md` and `debug_manifest.json` **BEFORE editing any code**.

---

## 2. The Universal 3-Branch Root-Cause Matrix

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             🔬 Universal 3-Branch Root-Cause Matrix                              │
└────────────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                                 │
      ┌───────────────────────────┬──────────────┴──────────────┬───────────────────────────┐
      ▼                           ▼                             ▼                           ▼
┌───────────┐               ┌───────────┐                 ┌───────────┐               ┌───────────┐
│ Branch A  │               │ Branch B  │                 │ Branch C  │               │ Live 2026 │
│API Contract│              │Concurrency│                 │Data Bounds│               │Search &   │
│ & Types   │               │& Lifecycle│                 │ & Encodings│              │Forensics  │
└───────────┘               └───────────┘                 └───────────┘               └───────────┘
```

1. **Branch A: API Contract & Type Boundaries**
   - Mismatched method signatures, missing arguments, changed return types.
   - Breaking API changes in 2026 package updates or serialization schema drift.
2. **Branch B: Concurrency, Lifecycle & State Transitions**
   - Race conditions, unhandled async promise rejections, deadlocks, missing `await`.
   - Premature resource disposal, unclosed streams, memory leaks.
3. **Branch C: Data Boundaries, Inputs & Syntax**
   - `Null`/`None`/`undefined` dereferences, off-by-one index overflows.
   - Character encoding mismatches (e.g. UTF-8 vs. Windows-1256), malformed JSON/YAML payloads.

---

## 3. Automated Testing Standards (Arrange-Act-Assert)

All test suites authored by the agency must adhere to the AAA pattern and test both happy and unhappy paths:

```python
# Python AAA Test Example
def test_atomic_write_preserves_original_on_failure(tmp_path):
    # 1. Arrange: Prepare mock filesystem and target file
    target_file = tmp_path / "data.json"
    target_file.write_text("{\"status\": \"original\"}")
    
    # 2. Act & Assert: Simulate crash during write
    with pytest.raises(IOError):
        atomic_save_with_simulated_crash(target_file, "{\"status\": \"corrupted\"}")
        
    # Verify original file remains intact (Failure-Mode Testing)
    assert target_file.read_text() == "{\"status\": \"original\"}"
```

### Multi-Language Test Matrix:
- **Python**: `pytest` + `pytest-asyncio` + `unittest.mock`
- **C# / .NET**: `xUnit` + `Moq` + `FluentAssertions`
- **TypeScript / JavaScript**: `Vitest` or `Jest` + `@testing-library`
- **Rust**: `cargo test` with unit `#[test]` and integration tests in `tests/`
- **Go**: `go test ./...` with `testing.T` and table-driven test cases

---

## 4. Delivery Artifact & Verification Seal (`COMPLETION_REPORT.md`)

```markdown
# 🏁 Final Completion & Verification Report

## 1. Executive Deliverable Summary
- **Target Feature / Fix**: [Summary of what was built or repaired]
- **Files Modified / Created**: [List of affected paths]
- **Verification Status**: ✅ 100% Passed AST, Unit, and Integration Tests

## 2. Quality Verification Seal
\`\`\`text
================================================================================
           🎖️ 100% COMPLIANCE & QUALITY VERIFICATION SEAL 🎖️
  • Human-Grade Craftsmanship (Atomic I/O, Graceful Shutdown, Actionable Errors)
  • Zero Collateral Drift: Churn strictly within blast radius bounds
  • Universal Accessibility (A11y): Fully keyboard-operable & screen-reader friendly
  • Deterministic Tests: All unit, failure-mode, and AST checks passed
================================================================================
\`\`\`

## 3. 1-Click Verification & Launch Commands
\`\`\`bash
# Run automated tests
python3 -m pytest tests/

# Validate syntax & AST integrity
python3 scripts/validate_code.py --strict .

# Launch application
./run.sh
\`\`\`
```