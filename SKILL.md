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
  4. التحقق من صحة المانيفست عبر: `python3 scripts/validate_code.py --strict --manifest <manifest_file>`.

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
     `python3 scripts/backup_manager.py backup <target_file>`
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
     `python3 scripts/validate_code.py --strict --human-grade <target_file>`
  2. في حالة تعديل كود قائم، التحقق من نطاق التعديل وعدم تجاوز الحدود:
     `python3 scripts/diff_verifier.py <backup_file> <target_file>`
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

### ميثاق تكليف الوكلاء الفرعيين (Subagent Prompt Contracts):
عند استدعاء أي وكيل فرعي، يجب على المنسق تزويده بنص واضح ومحدد يتضمن:
- **مسار ملف المانيفست والمراجع** المعتمدة على القرص (`references_manifest.json`، `project_spec.json`، أو `debug_manifest.json`).
- **المهمة الحصرية**: حظر التخمين من الذاكرة وإلزام الالتزام بالتوثيق الحي.
- **شرط الإنهاء**: تشغيل أداة التحقق والتأكد من نجاحها قبل تسليم النتيجة للمنسق.

---

## 3. مصفوفة تشخيص الأعطال ثلاثية الفروع (3-Branch Root-Cause Matrix)

عند وجود عطل أو مشكلة برمجية، يقوم وكيل التخطيط بالتعاون مع وكيل أبحاث الويب بتصنيف العطل إلى أحد الفروع الثلاثة وتوثيقه في `debug_manifest.json`:

| الفرع (Branch) | نوع العطل | الإجراء العلاجي الدقيق |
| :--- | :--- | :--- |
| **Branch A: API Contract Mismatch** | تعارض معايير الواجهات، تغير توقيع الدوال، عدم تطابق أنواع البيانات. | البحث في الويب عن أحدث توقيع رسمي للدالة وتحديث المدخلات فوراً. |
| **Branch B: Lifecycle & Concurrency** | مشاكل التزامن، تسريب الموارد، تعليق العمليات غير المتزامنة، إغلاق غير آمن. | إضافة أقفال التزامن، معالجة الـ Timeouts، وتنفيذ الإغلاق الآمن للمقابض. |
| **Branch C: Data Boundary & Syntax** | أخطاء الصفر/الفارغ (Null/Undefined)، أخطاء الترميز (Encoding)، مدخلات خارج النطاق. | التحقق الدفاعي المسبق من المدخلات، وتوفير قيم افتراضية آمنة ومعالجة استثناءات واضحة. |

---

## 4. إمكانية الوصول وقارئات الشاشة أولاً (Screen-Reader & A11y Invariants)

التزاماً بأعلى معايير الوصول:
1. **تنسيق المخرجات**: صياغة الردود بتسلسل منطقي خالٍ تماماً من الجداول المعقدة والزخارف والرموز التعبيرية المشوشة للقراءة الصوتية.
2. **واجهات المستخدم والتطبيقات**:
   - دعم كامل للوحة المفاتيح (`Tab`, `Enter`, `Space`, Arrows).
   - توفير تسميات ARIA صريحة ودقيقة لجميع العناصر التفاعلية.
   - إشعارات ديناميكية عبر `aria-live` للتغيرات الفورية.
   - تباين ألوان عالٍ وتجنب الاعتماد على اللون وحده لنقل المعلومة.

---

## 5. فهرس الأدوات والمخططات (Tools & Schemas Index)

| الأداة / الملف | المسار | الوظيفة |
| :--- | :--- | :--- |
| **مخططات الـ JSON** | `references/agency-schemas.json` | المخطط المرجعي الموحد للتحقق من المانيفست (`project_spec`, `debug_manifest`, `references_manifest`). |
| **أداة الفحص الشامل** | `scripts/validate_code.py` | فحص شجرة الـ AST، والـ JSON schemas، وخلو الكود من TODO و print (`--strict`, `--human-grade`, `--manifest`). |
| **مدير النسخ الاحتياطي** | `scripts/backup_manager.py` | أخذ نسخ احتياطية واسترجاع فوري قبل لمس أي ملف (`backup`, `restore`). |
| **مدقق حدود التعديل** | `scripts/diff_verifier.py` | التأكد من أن التعديل محصور جراحياً في السطور المحددة فقط. |
