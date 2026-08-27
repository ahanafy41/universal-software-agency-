# 🔬 Diagnostics, Root-Cause Analysis & Quality Assurance Playbook

This playbook governs bug triage, root-cause isolation, automated testing suites, and completion verification.

---

## 1. Mandatory Pre-Fix Diagnostic & Triage Gate

When addressing a defect or bug in an existing codebase, **DO NOT modify any code prematurely**.

### Step-by-Step Triage Workflow:
1. **Codebase Ingestion & Mental Topology**: Dispatch **Subagent B** to scan the project, map entry points, and construct `project_mindmap.md`.
2. **Interactive Triage**: If reproduction steps, stack traces, or environment details are missing, ask **ONE focused question per turn**.
3. **3-Branch Root-Cause Matrix**:
   - **Branch A (API Contract Mismatch)**: Signature drift, wrong payload shape, type mismatches.
   - **Branch B (Concurrency / Lifecycle)**: Race conditions, unhandled async states, leaked handles.
   - **Branch C (Data Boundary / Syntax)**: Null pointer exceptions, encoding mismatches, schema violations.
4. **Diagnostic Manifest**: Record findings in `debug_manifest.json` conforming to `references/agency-schemas.json`.

---

## 2. Automated Testing & Verification Standards

### 2.1. Arrange-Act-Assert (AAA) Pattern
Unit tests must strictly follow the AAA pattern:
- **Arrange**: Set up mocks, fixtures, and inputs.
- **Act**: Invoke the target method.
- **Assert**: Verify outputs, state changes, and side-effects.

### 2.2. Failure-Mode & Edge-Case Coverage
Test suites must include:
- Network dropouts and HTTP timeout simulations.
- Corrupted or empty input payloads.
- Concurrency race conditions and boundary limits.

---

## 3. Completion Report & Verification Seal

Upon passing all automated tests and AST verification (`python3 scripts/validate_code.py --strict <file>`), output `COMPLETION_REPORT.md` featuring the **Final Verification Seal (خاتم المراجعة والتحقق الشامل)**.
