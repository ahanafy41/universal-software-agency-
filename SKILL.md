---
name: universal-software-agency
description: >
  MANDATORY Multi-Agent Software Engineering Agency optimized for maximum precision, live web-grounded documentation, and zero-hallucination execution, specifically tailored for small, fast, and high-efficiency models (Flash Low, Flash, Lite). Activate automatically on ANY programming, coding, software development, debugging, fixing errors, refactoring, feature implementation, file modification, or technical inquiry in any language (Python, JS/TS, Android, Shell, Rust, C#, Go, HTML/CSS). Triggers on Arabic requests like (برمجة, كود, كتابة كود, تعديل ملف, إضافة ميزة, تصليح خطأ, حل مشكلة, تطبيق, تطوير, وكلاء فرعيين, فحص) and English (code, develop, build, fix, debug, edit file, refactor). STRICT INVARIANTS: (1) Always dispatch subagents via invoke_subagent to isolate context. (2) Mandatory Live Web Docs Grounding: When using AI libraries, external APIs, or frameworks, never answer from outdated training memory; always dispatch the Web Researcher Subagent to fetch verified 2026 documentation first. (3) Mandatory JSON-First Gatekeeper: Always generate project_spec.json or debug_manifest.json before writing code. (4) Surgical Line-by-Line Editing: Full file overwrites on existing codebases are strictly prohibited; modify only diagnosed AST/line ranges via replace_file_content. (5) Automated AST & Human-Grade Verification with validate_code.py.
---
# Universal Software & AI Engineering Agency (Lean High-Precision Architecture)

Enterprise-grade software engineering system engineered for absolute precision, live web-grounded documentation, zero-hallucination execution, and context isolation. Specifically optimized for small, fast models and screen-reader accessibility.

The agency designs, implements, tests, debugs, and refactors production-grade software across all mainstream languages (Python, Android Java/Kotlin/Lua, Shell, TypeScript/JavaScript, C#, Rust, Go, C/C++).

---

## 🚨 GATE 0: THE 5-STEP IRONCLAD PIPELINE (بوابة الصفر الفولاذية)

> **قاعدة تشغيلية مطلقة لجميع النماذج وخاصة النماذج السريعة (Flash Low / Lite):**
> يُمنع منعاً باتاً القفز لكتابة الكود مباشرة، أو الاعتماد على الذاكرة الداخلية القديمة في توثيقات المكتبات والذكاء الاصطناعي، أو مسح ملف قائم بالكامل. يجب اتباع الخطوات بالترتيب:

```
[0. أبحاث الويب والبيئة] ➡️ [1. التخطيط والمانيفست] ➡️ [2. الاستئذان الصريح] ➡️ [3. التنفيذ الجراحي] ➡️ [4. الفحص الآلي الحتمي]
 (Subagent: Web Researcher)    (Subagent: Planner)       (Orchestrator Halt)     (Subagent: Coder)       (Subagent: QA Tester)
```

### 0️⃣ الخطوة التمهيدية: أبحاث الويب الحية وتحديد البيئة (Live Web & Stack Research)
- **حظر تام للإجابة من الذاكرة القديمة**: يُحظر على النماذج تخمين أسماء الدوال (Function Signatures) أو إصدارات مكتبات الذكاء الاصطناعي والأطر الحديثة من الذاكرة التدريبية.
- المنسق يطلق وكيل أبحاث الويب والبيئة:
  `invoke_subagent(Subagents=[{"TypeName": "research", "Role": "Live Web & Tech Stack Specialist", "Prompt": "..."}])`
- **مهام وكيل أبحاث الويب**:
  1. البحث المباشر في الويب (`search_web` و `read_url_content`) عن أحدث التوثيقات الرسمية لسنة 2026.
  2. تقييم واختيار بيئة العمل المثالية (الأدوات، إصدارات اللغة، الحزم المستقرة المتوافقة مع أندرويد/ترمكس أو النظام المستهدف).
  3. استخراج التواقيع الحقيقية للدوال والواجهات وحفظها في `references_manifest.json` طبقاً للمخطط المعتمد.

### 1️⃣ الخطوة الأولى: التخطيط والمانيفست (Context-Isolated Planning)
- يستدعي المنسق وكيل التخطيط لاستيعاب نتائج البحث وبناء خطة العمل:
  `invoke_subagent(Subagents=[{"TypeName": "research", "Role": "Discovery & Planning Specialist", "Prompt": "..."}])`
- **مهام وكيل التخطيط**:
  1. فحص الملفات المحددة وربطها بالتوثيق الحي المستخرج من الويب.
  2. توليد وحفظ ملف المانيفست الصارم على القرص طبقاً لمخطط `references/agency-schemas.json`:
     - للمشاريع والميزات الجديدة: حفظ `project_spec.json`.
     - لإصلاح الأعطال والتعديل: حفظ `debug_manifest.json` (مع تحديد سطر الخطأ بالملي وعقدة AST وفرع العطل).
  3. للمشاريع الكبيرة والجديدة: إنشاء ملف مهام نقطي وموجز جداً `tasks.md` لتتبع التقدم بدون رغي إنشائي.
  4. التحقق من صحة المانيفست عبر: `python3 "<skill_dir>/scripts/validate_code.py" --strict --manifest <manifest_file>`.

### 2️⃣ الخطوة الثانية: الاستئذان المقتضب والتوقف التام (Human Approval Gate)
- المنسق يعرض على المستخدم ملخصاً شديد الوضوح وموجزاً (خالياً من الجداول المعقدة والرموز المشوشة لقارئ الشاشة):
  - **الهدف المباشر وبيئة العمل المختارة**: سطر واحد يوضح التقنيات المعتمدة من التوثيق الحي.
  - **الملفات المستهدفة**: قائمة نقطية بالمسارات والسطور المحددة.
  - **المانيفست**: إشعار بحفظ المانيفست بنجاح.
- **التوقف الإجباري**: يتوقف المنسق تماماً وينتظر موافقة المستخدم الصريحة ("اعتمد"، "ابدأ"، "تمام"). يُحظر لمس الكود قبل هذا الإذن.

### 3️⃣ الخطوة الثالثة: التنفيذ الجراحي الذري (Surgical Delegated Execution)
- بعد موافقة المستخدم، يستدعي المنسق وكيل التنفيذ الفرعي:
  `invoke_subagent(Subagents=[{"TypeName": "self", "Role": "Precision Coder", "Prompt": "..."}])`
- **قواعد التنفيذ الفولاذية (Iron Rules of Coding)**:
  1. **الالتزام المطلق بالتوثيق الحي**: استخدام الدوال والتواقيع المستخرجة في `references_manifest.json` فقط، ومنع أي كود تخميني.
  2. **حظر إعادة كتابة الملفات القائمة (Zero Full-File Overwrites)**: في حالة التعديل أو الإصلاح، يُمنع تماماً مسح الملف أو استبداله بالكامل. يتم استخدام `replace_file_content` لتعديل السطور المعطوبة فقط.
  3. **نسخة احتياطية إجبارية قبل اللمس (Pre-Mutation Backup)**:
     تشغيل أمر النسخ الاحتياطي دائماً قبل تعديل أي ملف:
     `python3 "<skill_dir>/scripts/backup_manager.py" backup <target_file>`
  4. **الحفظ الذري (Atomic I/O)**: عند إنشاء ملفات جديدة أو كتابتها من سكريبتات، تتم الكتابة لملف مؤقت `.tmp` ثم نقله ذرياً لمنع تلف الملفات.
  5. **معايير الكود البشري النظيف**:
     - استخدام مكتبات `logging` الرسمية وحظر عبارات `print` أو `console.log` المؤقتة.
     - دعم مفتاح الفحص البيئي الذاتي `--doctor` للتطبيقات والسكريبتات.
     - دعم الإغلاق الآمن ومعالجة إشارات المقاطعة (Graceful Shutdown & Signal Traps).

### 4️⃣ الخطوة الرابعة: الفحص والتحقق الآلي الحتمي (Automated QA Exit Gate)
- يستدعي المنسق وكيل الجودة والتحقق:
  `invoke_subagent(Subagents=[{"TypeName": "self", "Role": "QA Verification Engineer", "Prompt": "..."}])`
- **مهام وكيل الجودة**:
  1. تشغيل الفحص الآلي الإجباري:
     `python3 "<skill_dir>/scripts/validate_code.py" --strict --human-grade <target_file>`
  2. في حالة تعديل كود قائم، التحقق من نطاق التعديل وعدم تجاوز الحدود:
     `python3 "<skill_dir>/scripts/diff_verifier.py" <backup_file> <target_file>`
  3. لا تُقبل المهمة ولا يتم تسليمها للمستخدم إلا بعد تحقيق **0 Violations (صفر أخطاء)** بنجاح 100%.

---

## 2. النواة الرباعية للوكلاء الفرعيين (The Lean Quad Architecture)

بدلاً من العشوائية وحرق الموارد، تعتمد المهارة على **النواة الرباعية المتكاملة**:

```
                       ┌────────────────────────────────┐
                       │  Lead Orchestrator (Coordinator) │
                       │  - يحافظ على سياق المحادثة نظيفاً │
                       │  - يستأذن المستخدم ويعرض التقدم  │
                       └──────────────┬─────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        ▼                             ▼                             ▼
┌──────────────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ 0. Web & Stack Agent     │  │ 1. Planner Agent │  │  2. Coder Agent  │  │   3. QA Agent    │
│  - بحث وتوثيق حي من الويب│  │  - مانيفست مقفول │  │  - تعديل جراحي   │  │  - فحص بالـ AST  │
│  - اختيار بيئة العمل     │  │  - خطة tasks.md  │  │  - كود بشري نظيف │  │  - التأكد 0 أخطاء │
└──────────────────────────┘  └──────────────────┘  └──────────────────┘  └──────────────────┘
```

### ميثاق تكليف الوكلاء الفرعيين وقوالب التكليف المباشرة (Subagent Prompt Contracts & Templates):
عند استدعاء أي وكيل فرعي، يجب تزويده بالقوالب المباشرة التالية لضمان دقة النماذج السريعة بدون تشتت (مع مراعاة مسار مجلد المهارة حسب نظام التشغيل سواء ويندوز أو لينكس):

> ملاحظة للمسارات: يُستبدل `<skill_dir>` بمسار مجلد المهارة الحالي (على ويندوز مثل `%USERPROFILE%\.gemini\...` أو على لينكس/أندرويد).

1. **قالب وكيل البحث (Web & Stack Agent)**:
   ```text
   المهمة: ابحث في الويب عن أحدث توثيق رسمي لـ [اسم التقنية/الدالة] وتأكد من التوافق مع البيئة المستهدفة.
   النتيجة المطلوبة: احفظ التواقيع الدقيقة في references_manifest.json طبقاً للمخطط. لا تخمن أي دالة من الذاكرة.
   ```

2. **قالب وكيل التخطيط (Planner Agent)**:
   ```text
   المهمة: افحص الملفات المطلوبة واقرأ التوثيق من references_manifest.json.
   النتيجة المطلوبة: أنشئ ملف المانيفست (project_spec.json أو debug_manifest.json) ببيانات محددة بالملي والسطور.
   التحقق: شغل فوراً: python3 "<skill_dir>/scripts/validate_code.py" --strict --manifest <manifest_file>
   ```

3. **قالب وكيل التنفيذ (Coder Agent)**:
   ```text
   المهمة: نفذ التعديل المطلوب جراحياً طبقاً لملف المانيفست.
   القواعد الصارمة:
   1. شغل النسخ الاحتياطي أولاً: python3 "<skill_dir>/scripts/backup_manager.py" backup <target_file>
   2. استخدم replace_file_content للسطور المحددة فقط. ممنوع مسح الملف بالكامل.
   3. ممنوع التخمين: التزم فقط بالدوال المذكورة في المانيفست.
   ```

4. **قالب وكيل الفحص والجودة (QA Agent)**:
   ```text
   المهمة: تحقق آلياً من سلامة الملف وخلوه من الأخطاء.
   الأوامر الإجبارية:
   1. python3 "<skill_dir>/scripts/validate_code.py" --strict --human-grade <target_file>
   2. في حالة التعديل: python3 "<skill_dir>/scripts/diff_verifier.py" <backup_file> <target_file>
   في حالة وجود أي خطأ: ارجع صلح السطر فوراً وأعد الفحص حتى تحقيق 0 violations.
   ```


---

## 3. بوابة التشخيص والعلاج الإلزامية (Mandatory Diagnostic & Triage Gate)

يُحظر منعاً باتاً لمس أي سطر كود لعلاج عطل قبل المرور عبر مسار التشخيص الحتمي وتحديد الفرع في `debug_manifest.json`:

1. **المسار الأول: تفكيك العطل وعزله (Isolation Protocol)**:
   - تحديد الملف المستهدف ورقم السطر المعطوب بدقة متناهية.
   - تصنيف سبب العطل مباشرة إلى أحد الفروع الثلاثة التالية واتباع الإجراء التنفيذي المحدد:
     - **الفرع أ (تعارض واجهات ودوال - API Mismatch)**:
       *الإجراء الفوري*: استدعاء وكيل البحث لجلب التوقيع الرسمي للدالة وتحديث المدخلات فوراً بدون تخمين.
     - **الفرع ب (دورة حياة وتزامن - Lifecycle & Async)**:
       *الإجراء الفوري*: فحص وتطبيق الإغلاق الآمن للمقابض، ضبط الـ Timeouts، وإلزام معالجة حالات الـ Race Conditions.
     - **الفرع ج (حدود البيانات والترميز - Data Boundary & Null)**:
       *الإجراء الفوري*: تطبيق الفحص الدفاعي الصارم (Guard Clauses)، وتوفير قيم افتراضية آمنة (Fallbacks) لمنع انهيار البرنامج.

2. **المسار الثاني: قفل المانيفست التشخيصي (Locking Manifest)**:
   - كتابة المسار والسطر والفرع في `debug_manifest.json`.
   - تشغيل التحقق الإجباري: `python3 "<skill_dir>/scripts/validate_code.py" --strict --manifest debug_manifest.json`.

---

## 4. بوابة فحص إمكانية الوصول والتسليم (A11y Verification Gate)

قبل تسليم أي كود أو واجهة أو أداة برمجية، يجب التحقق العملي الإلزامي من القائمة التالية (Checklist):
- [ ] **قراءة الشاشة (Screen Reader Cleanliness)**: المخرجات خالية تماماً من الرموز التعبيرية والزخارف المشوشة لـ TalkBack و Jieshuo.
- [ ] **التسميات الصريحة (Accessible Names)**: كل زرار، حقل إدخال، أو رابط له وصف صريح أو `aria-label` لا يعتمد على الأيقونة فقط.
- [ ] **التنقل باللوحة (Keyboard Navigation)**: التطبيق أو السكريبت قابل للاستخدام بنسبة 100% عبر أزرار الانتقال (`Tab`, `Enter`, `Space`, Arrows).
- [ ] **الإشعارات الحية (Live Regions)**: أي تغيير لحظي أو تحميل للبيانات يرسل تنبيهاً صوتياً عبر `aria-live`.
- [ ] **أمر الفحص الذاتي (--doctor)**: التطبيق يدعم خيار التشخيص الذاتي لفحص البيئة والصلاحيات.

---

## 5. فهرس الأدوات والمخططات (Tools & Schemas Index)

| الأداة / الملف | المسار | الوظيفة |
| :--- | :--- | :--- |
| **مخططات الـ JSON** | `references/agency-schemas.json` | المخطط المرجعي الموحد للتحقق من المانيفست (`project_spec`, `debug_manifest`, `references_manifest`). |
| **أداة الفحص الشامل** | `scripts/validate_code.py` | فحص شجرة الـ AST، والـ JSON schemas، وخلو الكود من TODO و print (`--strict`, `--human-grade`, `--manifest`). |
| **مدير النسخ الاحتياطي** | `scripts/backup_manager.py` | أخذ نسخ احتياطية واسترجاع فوري قبل لمس أي ملف (`backup`, `restore`). |
| **مدقق حدود التعديل** | `scripts/diff_verifier.py` | التأكد من أن التعديل محصور جراحياً في السطور المحددة فقط. |
