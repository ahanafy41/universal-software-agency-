# Interactive Diagnostic Triage Guide (دليل الاستكشاف والترياج التفاعلي للأعطال)

Structured protocol for interactive, turn-by-turn diagnostic discovery when troubleshooting bugs with ambiguous reproduction conditions.

---

## 1. 🛑 The Strict One-Question-Per-Turn Rule
When a bug report is missing context:
- Ask **exactly ONE focused, concrete question per message**.
- Never overwhelm the user with multi-part questions or lists of options in a single turn.

---

## 2. The 4-Step Diagnostic Probing Sequence

```
[Turn 1: Preceding Trigger Action]
   "What exact button was clicked, CLI command executed, or input entered right before the error?"
       │
       ▼
[Turn 2: Runtime & OS Environment]
   "What exact Operating System, runtime version (e.g. .NET 8 / Python 3.12), and architecture is running?"
       │
       ▼
[Turn 3: Expected vs. Actual Behavior]
   "What was the expected output versus the specific error or behavior you observed?"
       │
       ▼
[Turn 4: Log Snippet / Stack Trace]
   "Is there an error log, terminal output, or stack trace available?"
```

---

## 3. Fast-Track Triage Option
If the user provides a complete crash log and reproduction command upfront:
- Bypass interactive questioning and proceed directly to **Step 3: Exact Location Pinpointing** and the **3-Branch Diagnostic Matrix**.
