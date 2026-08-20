# Universal Root-Cause Diagnostic & Debugging Engine (دليل التشخيص الجذري الشامل لكافة لغات البرمجة)

An enterprise-grade, framework-agnostic protocol for diagnosing, isolating, and resolving runtime exceptions, compilation errors, reflection breakdowns, memory leaks, and logic faults across ALL programming languages without corrupting existing working code.

---

## 1. The 3-Tier Multi-Agent Debugging Workflow (هيكل التشخيص متعدد الوكلاء)

```
                        ┌─────────────────────────────────────────────────┐
                        │              Error Ingestion & Log              │
                        │    (Stack trace, exception, compiler error)     │
                        └───────────────────────┬─────────────────────────┘
                                                │
                                                ▼
                        ┌─────────────────────────────────────────────────┐
                        │  Worker Subagent 1: Root-Cause Diagnostic       │
                        │  • Parses stack traces & compiler error codes   │
                        │  • Evaluates 3-Branch Diagnostic Matrix         │
                        │  • Checks official language/SDK specifications  │
                        └───────────────────────┬─────────────────────────┘
                                                │
                                                ▼
                        ┌─────────────────────────────────────────────────┐
                        │  Worker Subagent 2: Cross-Layer Blast Limiter   │
                        │  • Defines strict blast radius (target entity)  │
                        │  • Locks non-failing modules as READ-ONLY       │
                        │  • Analyzes callers & state flow for zero drift │
                        └───────────────────────┬─────────────────────────┘
                                                │
                                                ▼
                        ┌─────────────────────────────────────────────────┐
                        │  Worker Subagent 3: Surgical Patch & Verifier   │
                        │  • Creates pre-mutation snapshot in .backups/   │
                        │  • Applies surgical fix to exact target lines   │
                        │  • Runs validate_code.py & diff integrity audit │
                        └───────────────────────┬─────────────────────────┘
                                                │
                                                ▼
                        ┌─────────────────────────────────────────────────┐
                        │  Delivery & What's Next Roadmap                 │
                        │  • Clean root-cause summary & exact patch diff  │
                        │  • Step-by-step verification instructions       │
                        │  • Regression watchlist & future hardening      │
                        └─────────────────────────────────────────────────┘
```

---

## 2. Universal 3-Branch Diagnostic Matrix (مصفوفة التشخيص ثلاثية الفرضيات الشاملة)

Before touching any code in ANY language, evaluate these 3 core branches:

1. **Branch A: API / Contract / Reflection / Signature Mismatch**:
   - Does the method/function/property exist in the imported library or target SDK version?
   - Are argument types, counts, or optional parameter defaults misaligned?
   - In dynamic/reflection languages (Python `getattr`, Java/C# reflection, JS dynamic indexing, Lua table keys), is the member name misspelled or non-existent?

2. **Branch B: Lifecycle / Concurrency / State / Memory Management**:
   - Is an asynchronous promise, coroutine, goroutine, or thread accessing shared state without synchronization?
   - Is UI manipulation occurring off the Main/UI thread?
   - Was a resource (database connection, file descriptor, stream, socket) accessed after closing or before initialization?

3. **Branch C: Data Boundaries / Nullability / Parsing / Type Coercion**:
   - Is a `None` / `null` / `nil` / `undefined` value propagating unchecked into downstream operations?
   - Are boundary conditions (off-by-one errors, division by zero, string encoding/decoding, JSON malformation) unhandled?

---

## 3. Universal Polyglot Debugging Matrix (أمثلة عبر لغات البرمجة)

| Language / Stack | Common Error / Symptom | Root Cause | Universal Remedy |
|---|---|---|---|
| **Python** | `TypeError: 'NoneType' object is not subscriptable` | Upstream function returned `None` instead of dict/list | Add defensive `if obj is None` guard or fallback default |
| **Python** | `RuntimeError: dictionary changed size during iteration` | Mutating dict keys while looping | Iterate over list copy `for k in list(d.keys()):` |
| **C# / .NET** | `NullReferenceException: Object reference not set...` | Accessing uninstantiated class or missing DI service | Use null-conditional `?.` or register service in DI container |
| **C# / .NET** | `InvalidOperationException: Cross-thread operation` | Modifying UI from background Task | Use `Dispatcher.Invoke()` or `Control.Invoke()` |
| **JS / TypeScript** | `TypeError: Cannot read properties of undefined` | Nested property access on optional object | Use optional chaining `user?.profile?.name` |
| **JS / TypeScript** | `UnhandledPromiseRejection: fetch failed` | Missing try-catch in async function or network failure | Wrap in `try { ... } catch (err) { ... }` with user fallback |
| **Java / Kotlin** | `NoSuchMethodError` / `NoSuchFieldError` | Dependency version conflict or wrong class signature | Check imported jar/package version and method signature |
| **Rust** | `cannot borrow \`*self\` as mutable more than once` | Borrow checker conflict across closures or loops | Refactor to take ownership or use interior mutability (`RefCell`/`Mutex`) |
| **Go** | `panic: runtime error: invalid memory address or nil pointer` | Calling method on nil struct pointer or uninitialized channel | Check `if ptr == nil` and initialize channels with `make()` |
| **C / C++** | `Segmentation fault (core dumped)` | Dereferencing dangling/null pointer or out-of-bounds array | Validate pointers before dereference and use `std::vector` / `std::unique_ptr` |
| **PHP** | `Fatal error: Uncaught Error: Call to a member function on null` | Object variable is null | Use `?->` nullsafe operator |
| **Shell / Bash** | `unbound variable` or silent script exit | Unquoted variables with spaces or `set -u` trigger | Quote all variables `\"$VAR\"` and provide default `${VAR:-default}` |

---

## 4. Universal Post-Resolution \"What's Next?\" Roadmap Protocol

Every delivered solution must conclude with a standardized **What's Next** guide tailored to the project's language:
1. **Immediate Verification Command**: Exact terminal command or run action (e.g. `pytest`, `npm test`, `dotnet run`, `cargo test`, `python main.py`).
2. **Regression Watchlist**: 2-3 specific features or components adjacent to the fix that the user should manually test.
3. **Hardening Recommendations**: Defensive programming patterns (type hints, assertion checks, guard clauses) to permanently inoculate the codebase against related bugs.
4. **Next Feature Milestones**: Actionable suggestions for the next feature, optimization, or architecture refinement.
