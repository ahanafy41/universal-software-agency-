# Architecture Blueprints & Clean Project Layouts

Guidelines for standard file organization across target languages.

## 1. 3-Tier Enterprise Structure (Python / C# / TypeScript)

```text
src/
├── presentation/ (UI Components, Views, ViewModels, CLI commands)
├── core/         (Domain Entities, Business Logic, Interfaces, State Machines)
└── data/         (Repositories, Database Contexts, File I/O, API Clients)
```

## 2. File Naming Invariants
- Python: `snake_case.py`
- C# .NET: `PascalCase.cs`
- TypeScript: `kebab-case.ts` or `PascalCase.tsx`
- Rust: `snake_case.rs`
- Go: `snake_case.go`

## 3. Build & Run Automation
Always provide a 1-click launcher script in the root directory:
- `run.sh` for Unix/Linux/macOS
- `run.bat` for Windows environments