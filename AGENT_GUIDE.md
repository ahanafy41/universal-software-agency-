# 🤖 Agent Integration & Optimization Guide (v2.1)
### دليل استدعاء وتفعيل وكالة هندسة البرمجيات للوكلاء الأذكياء (v2.1)

هذا الدليل مخصص لنماذج وتطبيقات الذكاء الاصطناعي (مثل Gemini, Claude Code, Google Antigravity 2.0, Cursor, Windsurf, Roo Code, GitHub Copilot) لتشغيل واستدعاء المهارة بأقصى كفاءة ودون هدر للرموز (Tokens).

---

## ⚡ 1. مبادئ التشغيل الأساسية (Operational Invariants)

1. **الترشيق ومنع تضخم السياق (Zero Main-Loop Bloat)**:
   - يمنع على الوكيل القائد (Lead Orchestrator) تحليل المراجع الضخمة أو كتابة الأكواد المتعددة أو تتبع الأخطاء الطويلة في المحادثة الرئيسية.
   - يتم تفويض المهام المعقدة للوكلاء الفرعيين (`invoke_subagent`).

2. **البحث الحي والتوثيق لعام 2026 (Live 2026 Google Search)**:
   - قبل توليد أو تعديل أي كود لمكتبة خارجية أو إطار عمل، يلزم البحث عن التوثيق الرسمي لعام 2026 والتأكد من توافق التواقيع البرمجية.

3. **حظر الترقيع المبكر (Pre-Fix Diagnostic Gate)**:
   - يمنع تعديل أي كود قائم قبل إتمام الاستيعاب، ورسم الخريطة الذهنية (`project_mindmap.md`)، وعزل السبب الجذري عبر مصفوفة الفروع الثلاثة (`3-Branch Matrix`).

4. **تطويق نطاق التعديل (Strict Blast Radius Control)**:
   - أخذ نسخة احتياطية آلية قبل التعديل (`backup_manager.py`).
   - حصر التعديل في العقدة المعطوبة فقط مع التحقق من الفروقات (`diff_verifier.py`).

---

## 🧭 2. خريطة استدعاء المراجع (On-Demand Loading Map)

لا تقم بقراءة جميع الملفات دفعة واحدة. استدعِ الملف المناسب للمرحلة الحالية فقط:

```text
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ المرحلة المطلوبة                      │ الملف المرجعي للتحميل الفوري                    │
├──────────────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. بدء مشروع جديد / مواصفات / تخطيط    │ references/project-lifecycle.md                  │
│ 2. تشخيص أعطال / فحص واختبارات       │ references/diagnostics-and-qa.md                 │
│ 3. كتابة كود / حماية / نشر وحاويات     │ references/craftsmanship-and-devops.md           │
│ 4. التحقق من صحة مخططات الـ JSON     │ references/agency-schemas.json                   │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ 3. أدوات التحقق والأتمتة المدمجة (Local Tooling)

- **فحص الكود والمخططات والمراجع**:
  ```bash
  python3 scripts/validate_code.py --strict <target_file_or_dir>
  python3 scripts/validate_code.py --manifest references_manifest.json <source_file>
  ```
- **النسخ الاحتياطي اللحظي**:
  ```bash
  python3 scripts/backup_manager.py backup <file_path>
  python3 scripts/backup_manager.py restore <backup_id>
  ```
- **تدقيق الفروقات ونطاق التعديل**:
  ```bash
  python3 scripts/diff_verifier.py <backup_file> <modified_file>
  ```
