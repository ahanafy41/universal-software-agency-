# Universal Architecture Blueprints & Clean File Structures

This reference provides production-tested scaffolding templates and naming conventions for universal stacks (C#, Python, Web), incorporating project-level knowledge base and reference directories.

## 1. Clean File Naming & Directory Convention

Every project contains both the human-readable **`PRD.md`** and the machine-readable **`project_spec.json`** in the root directory, with optional `docs/` and `references/` folders for external knowledge.

### C# / .NET Desktop & Offline Tools
```
MyProject/
├── PRD.md                        # Product Requirements Document
├── project_spec.json             # Machine-readable architecture & module manifest
├── docs/                         # Custom API guides & Markdown documentation
├── references/                   # Custom JSON schemas & contracts
├── MyProject.csproj              # TargetFramework net8.0-windows / net8.0
├── Program.cs                    # Entry point & global exception handling
├── MainForm.cs / MainWindow.xaml # UI layer
├── Models/                       # Strongly-typed models matching JSON schemas
├── Services/                     # Business logic (e.g. FileProcessor.cs)
├── Data/                         # Offline storage (e.g. DatabaseContext.cs, SQLite)
├── build.bat                     # 1-click build: dotnet publish -c Release -r win-x64 --self-contained
└── run.bat                       # 1-click test launcher
```

### Python Desktop & Automation Tools
```
MyProject/
├── PRD.md                        # Product Requirements Document
├── project_spec.json             # Machine-readable architecture & module manifest
├── docs/                         # Custom API guides & Markdown documentation
├── references/                   # Custom JSON schemas & contracts
├── main.py                       # Application entry point & GUI/CLI runner
├── models/                       # Pydantic / dataclass schemas
├── ui/                           # User interface components (CustomTkinter, Tkinter)
├── core/                         # Core business logic & algorithms
├── storage/                      # Local SQLite / JSON state storage
├── requirements.txt              # Pinned dependencies
├── run.bat                       # 1-click launcher with venv setup
└── build_exe.bat                 # PyInstaller single-file packaging
```

### Web & Single-File Offline Tools
```
MyProject/
├── PRD.md                        # Product Requirements Document
├── project_spec.json             # Machine-readable architecture & module manifest
├── docs/                         # Documentation & reference notes
├── index.html                    # Self-contained single-file HTML/CSS/JS application
└── README.md                     # 3-step launch guide: Double-click index.html
```

## 2. 3-Tier Architecture Principles
1. **Presentation Layer (UI)**: Dispatches user events, renders feedback, non-blocking UI threads.
2. **Business Logic Layer (Core)**: Pure business rules, validations, algorithms, Design-by-Contract (`Requires`/`Ensures`).
3. **Data Layer (Storage)**: Offline SQLite/LiteDB/JSON stores, transactional ACID safety, resource disposal.
