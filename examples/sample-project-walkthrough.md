# Sample Project Walkthrough: Building an Offline Voice Notes App (C# WPF)

This walkthrough illustrates the full lifecycle of the Universal Software Agency constructing a complete desktop tool from scratch.

---

## Phase 0: Turn-by-Turn Scoping
- **Turn 1**: User asks to build a desktop audio notes app.
- **Agent Question 1**: "Who is the primary user, and what are the 3 non-negotiable MVP features?"
- **User Reply**: "For blind students to record lectures and search notes offline."
- **Agent Question 2**: "Do you have any custom reference docs, API specs, or audio formats we must follow?"
- **User Reply**: "Use standard WAV/MP3 and save metadata to SQLite."
- **Agent Action**: Generates `PRD.md`, `tasks.md`, and `project_spec.json`.

---

## Phase 1: Architecture & Contract
- Subagent A ingests SQLite schema and compiles `references_manifest.json`.
- Subagent C designs the 3-tier architecture:
  1. `UI/MainWindow.xaml` + `MainWindow.xaml.cs` (Accessible WPF UI).
  2. `Core/AudioRecorder.cs` + `Core/NoteManager.cs` (Domain Logic with DbC).
  3. `Data/DatabaseContext.cs` (SQLite Storage).

---

## Phase 2: Assembly & Pre-Mutation Snapshot
- Pre-mutation backup engine verifies target files.
- Code generated with full accessibility tags:
  ```xml
  <Button AutomationProperties.Name="Start Recording" 
          AutomationProperties.HelpText="Starts lecture audio capture"
          Click="OnRecordClicked" />
  ```
- Design-by-Contract enforced in C#:
  ```csharp
  public void SaveNote(Note note)
  {
      if (note == null) throw new ArgumentNullException(nameof(note));
      if (string.IsNullOrWhiteSpace(note.Title)) throw new ArgumentException("Title required", nameof(note));
      
      _dbContext.Notes.Add(note);
      _dbContext.SaveChanges();
  }
  ```

---

## Phase 3: QA & Delivery
- Validator runs: `python3 scripts/validate_code.py Core/AudioRecorder.cs` -> `[PASS]`.
- Launch script generated: `run.bat`.
- Agency outputs `COMPLETION_REPORT.md` with 100% Verification Seal.
