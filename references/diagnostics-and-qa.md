# Diagnostics, Root-Cause Debugging & Automated QA Guide (دليل التشخيص الجذري وضمان الجودة والاختبارات الآلية)

This reference consolidates the agency's diagnostic triage protocols, 3-branch root-cause analysis matrix, automated testing standards (AAA pattern), failure-mode coverage, and delivery verification artifacts across all supported programming languages.

---

## 1. Mandatory Pre-Fix Diagnostic & Triage Gate

Modifying code before completing diagnostic triage is strictly forbidden:

1. **Step 1: Codebase Ingestion & Caller Tracing**: Subagent B scans the repository, identifies entry points, and produces `project_mindmap.md`.
2. **Step 2: Interactive Scoping & Triage**: If error logs, repro steps, or environment details are missing, ask strictly ONE focused question per turn.
3. **Step 3: 3-Branch Root-Cause Isolation**: Evaluate the 3 diagnostic branches to isolate the fault AST node.
4. **Step 4: Manifest Recording**: Record the exact file, line number, AST node, and hypothesized fix in `debug_tasks.md` and `debug_manifest.json`.

---

## 2. The 3-Branch Root-Cause Diagnostic Matrix

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                           3-Branch Root-Cause Diagnostic Matrix                        │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐ ┌───────────────────────────────┐
│ Branch A: Contract & API      │ │ Branch B: Lifecycle & Async   │ │ Branch C: Data & Boundaries   │
├───────────────────────────────┤ ├───────────────────────────────┤ ├───────────────────────────────┤
│ • Signature / Schema Drift    │ │ • Race Conditions             │ │ • Null / Nil Pointer Reference│
│ • Serialization Shape Mismatch│ │ • Unhandled Async Rejections  │ │ • Text / Encoding Collisions  │
│ • Wrong Param Types / Arity   │ │ • Thread Deadlocks / Leaks    │ │ • Off-by-One / Array Bounds   │
│ • Deprecated API Calls        │ │ • Unclosed DB / File Handles  │ │ • Missing Env Vars / Secrets  │
└───────────────────────────────┘ └───────────────────────────────┘ └───────────────────────────────┘
```

---

## 3. Automated QA & Testing Engineering Standards

Subagent D constructs comprehensive automated test suites using the **Arrange-Act-Assert (AAA)** pattern:

### 🧪 Test Coverage Requirements:
1. **Happy Path (Nominal Flow)**: Verify valid inputs yield expected outputs.
2. **Boundary & Edge Cases**: Test empty strings, zero values, max values, null inputs, and unexpected types.
3. **Failure Modes & Fault Injections**:
   - Simulated network timeouts and DNS failures.
   - File system permission errors and disk-full scenarios.
   - Corrupted JSON / malformed payload handling.
   - Database connection drops and automatic reconnection retries.
4. **Zero Flakiness Invariant**: Tests must not rely on unseeded randomness or unmanaged sleep timers.

---

## 4. Completion Report & Final Verification Seal

Upon completing implementation, testing, and static analysis, generate `COMPLETION_REPORT.md` featuring the **Final Verification Seal (خاتم المراجعة والتحقق الشامل)**:

```markdown
# 🏆 Universal Engineering Completion Report & Verification Seal

## 📋 Execution Summary
- **Project / Task**: <Project Name or Bug ID>
- **Stack & Architecture**: <Language / Framework / 3-Tier Layering>
- **Test Results**: <X tests passed, 0 failures, 0 skipped>
- **Static Analysis & Schema Validation**: [PASS] (`validate_code.py --strict`)

## 🛡️ Senior Craftsmanship Verification Matrix
- [x] Atomic File I/O Enforced
- [x] Actionable Error Messages Implemented (What, Why, Fix)
- [x] Environment Self-Check Supported (`--doctor`)
- [x] Graceful Signal Shutdown Handled (`SIGINT`)
- [x] Structured Logging Configured
- [x] Universal Keyboard-First & Screen-Reader Accessibility Verified

---
### 🎖️ خاتم المراجعة والتحقق الشامل (Seal of Verified Engineering Quality)
*Certified 100% complete, verified against all architectural and testing specifications.*
```
