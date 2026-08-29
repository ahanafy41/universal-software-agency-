# Diagnostics, Root-Cause Debugging & Support Ticket Guide

This reference consolidates the agency's diagnostic triage protocols, support ticket lifecycle (`TICKET.md`), 3-branch root-cause analysis matrix, live error lookups, patch plan approval gate, automated testing standards (AAA pattern), and delivery verification artifacts across all supported programming languages.

---

## 1. Support Ticket Protocol & Pre-Fix Diagnostic Gate

**STRICT PROHIBITION OF PREMATURE PATCHING**: When troubleshooting bugs in an existing codebase, the AI Agent is **STRICTLY FORBIDDEN from immediately modifying code**. It must complete the support ticket workflow:

### Step 1: Open Formal Support Ticket (`TICKET.md`)
Create `TICKET.md` capturing:
1. Symptom summary and severity level (`Critical`, `High`, `Medium`, `Low`).
2. Exact steps to reproduce and observed vs expected behavior.
3. Runtime environment details (OS, language version, dependencies).
4. Raw stack traces, error messages, and logs.

### Step 2: Interactive Diagnostic Investigation & Live Lookups
- Dispatch **Subagent B** to map call graphs and pinpoint execution paths.
- Query Google Search / GitHub Issues for exact error signatures and 2026 breaking changes.
- Conduct two-way clarifying dialogue with the user if logs or environment parameters are missing.

### Step 3: 3-Branch Root-Cause Isolation
Classify failure into:
- **Branch A (API Contract & Type Boundaries)**: Signature drift, wrong payload shape, type mismatches.
- **Branch B (Concurrency, Lifecycle & State)**: Race conditions, unhandled async states, leaked handles.
- **Branch C (Data Boundary, Syntax & Input)**: Null pointer exceptions, encoding mismatches, schema violations.

### Step 4: Mandatory Patch Plan Approval Gate (Stop & Wait Invariant)
- Formulate the minimal surgical patch, affected files, line numbers, and blast radius.
- Present the patch plan to the user in `TICKET.md` and **HALT execution**.
- **Await explicit user approval (`Approved` / `موافق`) before modifying any code.**

---

## 2. Universal 3-Branch Root-Cause Matrix

```
                          ┌──────────────────────────────────┐
                          │   Root-Cause Diagnostic Matrix   │
                          └─────────────────┬────────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
┌───────────────────────────┐   ┌───────────────────────────┐   ┌───────────────────────────┐
│ Branch A: API Contract    │   │ Branch B: Concurrency     │   │ Branch C: Data Boundary   │
│ • Signature drift         │   │ • Race conditions         │   │ • Null/None references    │
│ • Payload schema mismatch │   │ • Unhandled async states  │   │ • Encoding & parsing error│
│ • Type & return mismatches│   │ • Resource handle leaks   │   │ • Boundary / off-by-one   │
└───────────────────────────┘   └───────────────────────────┘   └───────────────────────────┘
```

---

## 3. Real-Time Support Ticket Tracker (`TICKET.md`)

```markdown
# 🎫 Support Ticket #001: [Issue Title]

**Status:** Awaiting Approval | **Severity:** High | **Branch:** Branch A (Contract)

## 1. Problem Description & Reproduction
- **Observed Behavior:** [Exact failure]
- **Expected Behavior:** [Intended behavior]
- **Reproduction Command:** `pytest tests/test_failure.py`

## 2. Diagnostic Investigation & Root Cause
- **Live Search Findings:** [Relevant GitHub Issue / 2026 doc insight]
- **Fault Pinpoint:** `src/services/auth.py` (Lines 42-55, `validate_token` method)
- **Root Cause:** Token format changed in SDK v2.3.0.

## 3. Proposed Surgical Patch Plan
- **Pre-Mutation Snapshot:** Take backup via `backup_manager.py`.
- **Targeted Diff:** Update token parsing logic in `validate_token`.
- **Blast Radius:** Max 15 lines in `src/services/auth.py`.

## 🚨 Approval Gate
- [ ] User Approval Received (`Approved` / `Proceed`)
```

---

## 4. Automated Testing Standards & AAA Pattern

All test suites engineered by **Subagent D** must follow the **Arrange-Act-Assert (AAA)** pattern and explicitly test both the happy path and failure modes:
- Multi-language coverage: Python (`pytest`), C# (`xUnit`), TypeScript (`Vitest`), Rust (`cargo test`), Go (`go test`).
- Mandatory failure modes: Network dropouts, malformed JSON, boundary values, resource exhaustion.

---

## 5. Completion Report & Final Verification Seal (`COMPLETION_REPORT.md`)

Upon completing development or debugging, generate `COMPLETION_REPORT.md` featuring test matrices, 1-click launch commands, and the **Final Verification Seal (خاتم المراجعة والتحقق الشامل)**.
