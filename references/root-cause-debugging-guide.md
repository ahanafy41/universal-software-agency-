# Universal 3-Branch Root-Cause Diagnostics Matrix (دليل التشخيص الجذري الشامل لكافة اللغات)

Enterprise diagnostic framework for isolating software faults across any programming language without speculative guesswork.

---

## 1. The 3 Diagnostic Hypotheses

```
                              ┌────────────────────────────────────────┐
                              │     Runtime Error / Compiler Fault     │
                              └───────────────────┬────────────────────┘
                                                  │
                 ┌────────────────────────────────┼────────────────────────────────┐
                 ▼                                ▼                                ▼
   [Branch A: API / Contract]       [Branch B: Lifecycle / Thread]    [Branch C: Data / Boundaries]
   • Method signature mismatch       • Cross-thread UI mutation        • Null / None dereference
   • Missing library symbol          • Resource accessed after dispose • Index out of range
   • Reflection / dynamic binding    • Race condition / Deadlock       • JSON syntax corruption
```

---

## 2. Polyglot Diagnostic Forensics Table

| Language | Branch A (Contract / API) | Branch B (Lifecycle / Concurrency) | Branch C (Data / Nullability) |
| :--- | :--- | :--- | :--- |
| **Python** | `AttributeError`, `TypeError: unexpected keyword` | `RuntimeError: loop already running`, Task Cancelled | `KeyError`, `IndexError`, `NoneType has no attribute` |
| **C# .NET** | `MissingMethodException`, `TypeLoadException` | `InvalidOperationException: Cross-thread operation`, `ObjectDisposedException` | `NullReferenceException`, `ArgumentNullException` |
| **TypeScript** | `TypeError: x is not a function`, missing property | Unhandled Promise Rejection, async state race | `Cannot read properties of undefined/null` |
| **Rust** | Trait not implemented, mismatched types | Borrow checker (`E0382: use of moved value`), deadlock | `panic! index out of bounds`, unhandled `Option::None` |
| **Go** | Interface satisfaction failure | `fatal error: concurrent map writes`, Goroutine leak | `panic: runtime error: invalid memory address or nil pointer` |
| **Java** | `NoSuchMethodError`, `ClassNotFoundException` | `IllegalStateException: Not on FX application thread` | `NullPointerException`, `ArrayIndexOutOfBoundsException` |
| **C / C++** | Undefined reference linker error, header mismatch | Data race, mutex deadlock, use-after-free | Segmentation fault (`SIGSEGV`), buffer overflow |
