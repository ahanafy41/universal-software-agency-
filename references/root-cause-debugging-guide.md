# Universal 3-Branch Root-Cause Debugging Guide

Detailed diagnostic matrices across programming languages.

## Branch A: API / Contract / Reflection / Signature Mismatch
- Python: `AttributeError`, `TypeError: unexpected keyword argument`
- C# .NET: `MissingMethodException`, `TypeLoadException`, `InvalidCastException`
- TypeScript: `TS2345: Argument not assignable`, `TS2339: Property does not exist`
- Rust: `mismatched types`, `cannot find function in crate`

## Branch B: Lifecycle / Concurrency / State / Threading Fault
- UI thread violations (e.g. `InvalidOperationException: The calling thread cannot access this object...`)
- Uninitialized database connections or leaked sockets.
- Race conditions in async/await workflows.

## Branch C: Data Boundaries / Nullability / Parsing Corruption
- `NullReferenceException`, `NoneType has no attribute`, `Cannot read properties of undefined`
- Malformed JSON strings or unescaped delimiters.