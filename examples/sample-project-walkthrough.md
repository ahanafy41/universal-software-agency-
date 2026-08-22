# Sample Walkthrough: Building an Offline-First SQLite Contact Book in C# .NET

This walkthrough demonstrates the Universal Software Agency lifecycle for a greenfield C# .NET application.

## Phase 0: Scoping (Turn-by-Turn)
- Turn 1: "Who is the primary user and what is the core problem?" -> Answer: "A solo desktop user who needs to manage contacts without internet."
- Turn 2: "What is the target framework and persistence choice?" -> Answer: "C# .NET 8 WPF, SQLite with Dapper."
- Turn 3: "Are there specific accessibility requirements?" -> Answer: "High contrast UI, tab navigation, screen reader labels."
- Result: Generated `PRD.md` and `project_spec.json`.

## Phase 1: Custom Knowledge & Architecture
- Subagent A parsed schema specs.
- Subagent G retrieved the latest Microsoft Learn guidelines for SQLite in .NET 8.
- Result: 3-tier architecture defined (UI -> ContactService -> SqliteRepository).

## Phase 2: Assembly
- Pre-mutation backup initialized.
- Subagent C generated `Contact.cs`, `IContactRepository.cs`, `SqliteContactRepository.cs`, and `MainWindow.xaml.cs`.
- Implemented Design-by-Contract guard clauses.

## Phase 3: Verification & Delivery
- Subagent D executed `validate_code.py`.
- Generated `COMPLETION_REPORT.md` and What's Next Roadmap.