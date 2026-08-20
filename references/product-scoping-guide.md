# Product Management Scoping Guide

The agency uses a turn-by-turn interactive scoping protocol to define project boundaries before writing any code.

---

## 1. The Strict One-Question-Per-Message Rule
To avoid cognitive overload and ensure crisp alignment:
- The agent **MUST NEVER** output a list or questionnaire of multiple questions.
- Ask **exactly ONE question per turn**, analyzing the user's response before formulating the next question.

---

## 2. The 6 Discovery Pillars
1. **Pillar 1: Business Problem & Persona**: Who is the user? What is the single biggest pain point?
2. **Pillar 2: Knowledge Ingestion**: Are there existing specs, JSON schemas, or reference docs in `docs/` or `references/`?
3. **Pillar 3: Form Factor & Deployment Track**:
   - **Track A**: Desktop Application (C# WPF/WinForms, Python GUI).
   - **Track B**: Standalone Web Tool / API (Single-file HTML/JS, Node/Express, Flask).
   - **Track C**: Automation & Systems (Shell scripts, Termux, CLI tools).
4. **Pillar 4: Offline & Data Persistence**: Does it require 100% offline support? Local DB preference (SQLite, LiteDB, JSON)?
5. **Pillar 5: UI/UX & Accessibility**: Screen reader compatibility, high-contrast dark theme, keyboard navigation.
6. **Pillar 6: Error Handling & Resilience**: Logging to `app_errors.log`, fallback states.

---

## 3. Locking MVP Scope (MoSCoW)
- **Must-Have**: The absolute minimum 2-3 features required for the product to be useful.
- **Out of Scope**: All non-essential features are deferred to prevent scope creep.
