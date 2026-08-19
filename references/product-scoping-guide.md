# Product Manager & Business Scoping Guide

The Product Manager & Business Strategist agent ensures that every software project has a clear value proposition, realistic MVP scope, intuitive UX, and actionable ROI before technical engineering begins.

## 1. Turn-by-Turn Scoping to PRD Generation
The Orchestrator conducts a single-question-per-turn dialogue. Once the 6 discovery pillars (including custom knowledge/reference ingestion) are answered, the agency immediately compiles the answers into a formal **`PRD.md`** (Product Requirements Document) alongside **`project_spec.json`**.

## 2. Core Evaluation Dimensions

1. **Problem Clarity & User Persona**:
   - Who is the end user? (Self, internal team, non-technical clients, blind/visually impaired users, general public).
   - What pain point does this solve? Is it repetitive manual work, offline accessibility, data organization, or automation?

2. **Custom Knowledge & Reference Ingestion**:
   - Does this project rely on specialized, obscure, or internal libraries, private APIs, custom JSON schemas, or unique domain rules?
   - Has the user provided Markdown docs, JSON schemas, cheat sheets, or sample code in `docs/` or `references/`?
   - Ground truth rule: If custom docs are provided, lock all technical assumptions strictly to those documents.

3. **MVP Prioritization (The MoSCoW Framework)**:
   - **Must-Have (Core MVP)**: The minimal 2-3 features without which the tool is useless.
   - **Should-Have**: Important features deferred to v1.1.
   - **Could-Have**: Nice-to-have visual polish or extra integrations.
   - **Won't-Have**: Unnecessary bloat that adds complexity without tangible value.

4. **Frictionless Delivery Assessment**:
   - What is the easiest way for the user to run this?
     - Standalone `.exe` (C# .NET or PyInstaller)
     - Zero-dependency Single HTML/JS/CSS file opened in browser
     - Python script with automated `run.bat`
   - Does it need to work completely offline (no internet)?

5. **Product Risk & Edge-Case Checklist**:
   - What happens if the user enters invalid input?
   - What happens if target files/folders are missing?
   - How does the user know the tool succeeded (visual feedback, audio cue, status bar, log file)?
