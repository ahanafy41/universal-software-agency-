# Architecture Blueprints & File Standards

## 1. 3-Tier Layer Separation
Every application regardless of stack separates concerns into 3 tiers:

```
src/
├── UI/              # User Interface, XAML, HTML/CSS, React components, Views
├── Core/            # Business Logic, State Machine, Domain Models, Contracts
└── Data/            # Storage, Repositories, Database Context, File I/O
```

---

## 2. Universal File Naming Standards
- **C#**: `PascalCase.cs` (e.g. `AudioRecorder.cs`, `MainWindow.xaml`)
- **Python**: `snake_case.py` (e.g. `audio_recorder.py`, `main_window.py`)
- **TypeScript**: `kebab-case.ts` or `PascalCase.tsx` (e.g. `audio-recorder.ts`, `DashboardView.tsx`)
- **Go**: `snake_case.go` (e.g. `audio_recorder.go`)
- **Rust**: `snake_case.rs` (e.g. `audio_recorder.rs`)

---

## 3. Platform-Agnostic 1-Click Launchers

### Linux / macOS / Termux (`run.sh` / `build.sh`)
```bash
#!/usr/bin/env bash
set -euo pipefail
echo "[1/2] Checking dependencies..."
command -v dotnet >/dev/null 2>&1 || command -v python3 >/dev/null 2>&1 || { echo "Error: Runtime not installed."; exit 1; }
echo "[2/2] Launching application..."
# Example Python launch
python3 main.py "$@"
```

### Windows (`run.bat` / `build.bat`)
```bat
@echo off
setlocal enabledelayedexpansion
echo [1/2] Checking environment...
where dotnet >nul 2>nul || where python >nul 2>nul || (
    echo Error: Required runtime not found.
    pause
    exit /b 1
)
echo [2/2] Starting application...
REM Example C# .NET launch
dotnet run --project src\App.csproj
pause
```
