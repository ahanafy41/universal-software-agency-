# Zero-Corruption & Blast-Radius Preservation Protocol (بروتوكول حماية سلامة الكود ومنع الإفساد)

Strict non-negotiable engineering invariants to prevent AI models from corrupting, breaking, or mutating existing working code during bug fixes and refactoring across ALL programming languages.

---

## 1. The Zero-Corruption Invariant (قانون السلامة المطلقة للكود)

When fixing a bug or applying an update to an existing codebase:

1. **Strict Blast-Radius Limiter (تطويق نطاق التعديل)**:
   - Modifications MUST be strictly restricted to the specific lines, functions, or AST nodes causing the fault.
   - The AI agent is **STRICTLY FORBIDDEN** from modifying, "refactoring", "optimizing", or cleaning up surrounding working code unless explicitly requested by the user.
2. **Prohibition of Accidental Deletions**:
   - Never delete existing comments, helper functions, exported methods, user configurations, or architecture layers.
   - Preserves exact formatting, naming conventions, and structural hierarchy.
3. **Automated Diff Verification Against Snapshot**:
   - Before applying any change, a snapshot is saved in `.backups/YYYYMMDD_HHMMSS/`.
   - After applying the patch, an automated diff check confirms that only the intended target entity was modified. If unintended files or functions were touched, the patch is automatically rolled back to the backup snapshot.

---

## 2. 4-Stage Safety Gatekeeper for Bug Fixing (بوابات الأمان الأربعة لتصحيح الأخطاء)

```
┌─────────────────────────────────────────────────────────────┐
│ Stage 1: Target Isolation & Blast Radius Definition          │
│ • Identify exact failing symbol, method, or line            │
│ • Lock all other files & routines as READ-ONLY               │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Stage 2: Pre-Mutation Snapshot (.backups/)                  │
│ • Full file snapshot with timestamp                         │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Stage 3: Surgical Patch Application                         │
│ • AST-level / line-level modification ONLY on target entity  │
│ • 0% speculative cleanup of unrelated code                  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Stage 4: Diff Audit & Integrity Validation                  │
│ • Run validate_code.py (Syntax + Bracket + Ast)             │
│ • Diff check against snapshot to confirm zero side effects  │
│ • Rollback immediately if unauthorized changes detected     │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Universal Polyglot Applicability (تطبيق عالمي عبر كافة اللغات)

This protocol applies universally across all software stacks:
- **Python**: Django, FastAPI, Flask, PyTorch, Pandas, AsyncIO, CLI tools.
- **C# / .NET**: WPF, WinForms, ASP.NET Core, MAUI, Unity, Blazor.
- **JavaScript / TypeScript**: Node.js, React, Next.js, Vue, Angular, Express, Electron, Svelte.
- **Java / Kotlin**: Android SDK, Spring Boot, Quarkus, Maven/Gradle.
- **Rust**: Actix, Tokio, Tauri, Cargo crates, CLI utilities.
- **Go**: Gin, Fiber, Goroutines, microservices, system tools.
- **C / C++**: Qt, CMake, embedded systems, desktop apps.
- **PHP / Ruby / Swift / Shell**: Web apps, macOS/iOS apps, DevOps scripts.
