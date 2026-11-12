# 🌐 Universal Socratic Software Engineering Council (v4.0 Lean Powerhouse)
### المنظومة البرمجية التفاعلية الموحدة لكافة المنصات ولغات البرمجة (الإصدار الرابع الرشيق)

[![Version: 4.0](https://img.shields.io/badge/Version-4.0%20Lean%20Powerhouse-blue.svg)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero%20External-brightgreen.svg)](SKILL.md)
[![File Limit](https://img.shields.io/badge/Code%20Limit-100%20Lines%20Max-orange.svg)](SKILL.md)
[![Logic Verified](https://img.shields.io/badge/Testing-100%25%20Assertion%20Pass-purple.svg)](scripts/validate_code.py)
[![A11y Ready](https://img.shields.io/badge/Accessibility-Screen%20Reader%20Ready-teal.svg)](SKILL.md)

منظومة برمجية مؤسسية مستقلة بنسبة 100% (**Zero External Dependencies**) ومبنية بهندسة خماسية رشيقة فائقة السرعة (**5-File Lean Architecture**). مصممة لتمكين المبتدئين وغير المبرمجين إلى جانب كبار المطورين من بناء برمجيات قوية عبر **حوار عصف ذهني سقراطي مستمر**، وتطبيق **قاعدة الـ 100 سطر للملفات**، واختبار المنطق ميكانيكياً بنسبة 100% عبر كافة المنصات ولغات البرمجة (Python, TypeScript, Go, Rust, C#, Java, Shell, Lua).

---

## 🌟 الركائز الأساسية للإصدار الرابع الرشيق (v4.0)

1. **الاستقلالية التامة (Zero External Dependencies)**:
   - مهارة قائمة بذاتها بالكامل؛ لا تحتاج أي مهارة إضافية، وتعمل بنظام التشغيل الفوري (Zero-Config).
2. **العصف الذهني السقراطي الدائم**:
   - حوار مستمر مع المستخدم في كل مرحلة (سؤال إلى سؤالين بخيارات واضحة باللغة العربية)، وتوثيق دائم للقرارات على القرص في `BRAINSTORMING.md` و `DECISIONS.md`.
3. **قاعدة الـ 100 سطر الصارمة للملفات**:
   - حظر تام لأي ملف كود يتجاوز 100 سطر كود لضمان تقسيم الكود إلى وحدات معمارية صغيرة وسهلة القراءة ومريحة لقارئات الشاشة وتمنع كسل النماذج الصغيرة.
4. **فحص المنطق والـ Assertions الميكانيكي**:
   - حظر الاكتفاء بفحص السنتاكس؛ تشغيل حقيقي للاختبارات وتأكيد صحة المعادلات والنتائج بالأرقام والـ `assert` بنسبة 100% نجاح.
5. **التسليم السهل لغير المبرمجين**:
   - تسليم الكود دائماً مع سكريبت تشغيل فوري بنقرة واحدة (`run.sh` أو `run.bat`) وشرح مبسط لما سيظهر على الشاشة.

---

## 📂 خريطة ملفات المهارة الخماسية الرشيقة (The 5-File Map)

| الملف / الأداة | المسار | الوظيفة والمسؤولية |
| :--- | :--- | :--- |
| **`SKILL.md`** | `SKILL.md` | النواة التوجيهية الشاملة، ميثاق الفريق الرباعي الرشيق، والمسار التنفيذي الشامل (79 سطراً مركزة). |
| **`README.md`** | `README.md` | الدليل التوثيقي الكامل للمستخدم والوكلاء لشرح المنظومة وآلية استخدامها. |
| **`scripts/validate_code.py`** | `scripts/validate_code.py` | الفاحص الشامل الموحد (الـ AST، حد الـ 100 سطر، تشغيل اختبارات المنطق `--run-tests`، وتدقيق الفروقات `--diff-check`). |
| **`scripts/backup_manager.py`** | `scripts/backup_manager.py` | مدير النسخ الاحتياطي اللحظي قبل لمس أي ملف والاسترجاع بنقرة واحدة. |
| **`references/agency-schemas.json`** | `references/agency-schemas.json` | المخطط المرجعي الموحد للمشاريع والتشخيص وعقود الكود. |

---

## ⚡ التشغيل والاستخدام

المهارة تعمل فوراً بمجرد نسخها إلى مجلد المهارات:
- فور طلب أي مهمة برمجية، يطلق الوكيل جلسة العصف الذهني الاستكشافية فوراً.
- يتم إنشاء ملفات `BRAINSTORMING.md` و `DECISIONS.md` و `tasks.md`.
- ينفذ الوكيل الكود خطوة بخطوة، مع نسخ احتياطي لحظي، وبكود لا يتجاوز 100 سطر للملف.
- يتم تشغيل الفاحص الشامل:
  ```bash
  python3 scripts/validate_code.py --strict --human-grade --run-tests .
  ```
- لا يُعتمد الكود إلا بعد ظهور: `[PASS] All behavioral and assertion tests passed 100%!`.
