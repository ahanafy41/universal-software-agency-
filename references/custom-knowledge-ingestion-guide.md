# Custom Knowledge & Reference Ingestion Guide (دليل استيعاب المراجع والتوثيق المخصص)

This reference defines how the Universal Software & AI Engineering Agency ingests, indexes, and strictly adheres to user-provided reference documents, custom framework documentation, JSON/YAML schemas, and domain-specific knowledge bases.

---

## 1. The Core Ingestion Principle (مبدأ التأريض المعرفي الصارم)
When building applications involving unfamiliar, proprietary, specialized, or internal libraries (e.g., obscure SDKs, private APIs, custom JSON data schemas, proprietary screen reader/accessibility frameworks, hardware protocols, or specialized DSLs):
1. **Zero-Hallucination Grounding**: The agency treats user-provided reference materials as the single source of truth (Ground Truth). The agent is strictly prohibited from inventing non-existent method signatures, imagined parameters, or fake endpoints.
2. **Contract-Locked Synthesis**: All function calls, data models, and error handlers must map 1:1 to the documented specifications.
3. **Transparent Uncertainty**: If a specific behavior, parameter type, or edge case is missing from the reference documents, the agent MUST explicitly ask the user for clarification rather than making assumptions.

---

## 2. Supported Reference Formats & Ingestion Methods

| Format | Common Extensions | Typical Use Case | Agency Processing Method |
| :--- | :--- | :--- | :--- |
| **Markdown / Text Docs** | `.md`, `.txt`, `.rst` | API manuals, cheat-sheets, business rules, architecture notes | Full semantic parsing, extraction of function signatures, lifecycles, and constraints |
| **Data Schemas** | `.json`, `.yaml`, `.yml` | JSON Schemas (Draft-07/2020-12), OpenAPI/Swagger, config specs | Automatic generation of strongly-typed models (C# records, Python Pydantic/dataclasses, TypeScript interfaces) |
| **Code Stubs & Headers** | `.cs`, `.py`, `.d.ts`, `.h`, `.lua` | Type definitions, interface definitions, SDK header files | Direct contract extraction (`Requires`/`Ensures`) and interface implementation |
| **Golden Code Examples** | `.cs`, `.py`, `.js`, `.lua`, etc. | Proven working code snippets demonstrating correct usage | Pattern extraction for initialization, error trapping, thread safety, and resource disposal |

---

## 3. Project-Level Directory Standard (`docs/` and `references/`)

The agency automatically scans and indexes any user-supplied reference files located in standard directories within the project workspace:

```
MyProject/
├── PRD.md
├── project_spec.json
├── docs/                         # Project-specific documentation & guides
│   ├── api_guide.md              # Markdown API documentation
│   └── custom_library_syntax.md  # Specific syntax / language reference
├── references/                   # Machine-readable schemas & specs
│   ├── data_schema.json          # JSON Schema for payloads / storage
│   └── openapi.yaml              # REST API contract
├── src/                          # Application source code
└── build.bat
```

---

## 4. The 4-Stage Ingestion Workflow

### Stage 1: Ingestion & Symbol Extraction (خبير استيعاب التوثيق)
- The subagent parses the reference files and extracts an internal Symbol Table:
  * **Exported Classes / Namespaces**
  * **Function Signatures** (Name, Parameters, Types, Return Values, Async/Sync)
  * **Constants, Enums & Error Codes**
  * **Lifecycle Requirements** (e.g., `Initialize()`, `Dispose()`, Event Listeners)

### Stage 2: Schema-Driven Model Generation (توليد النماذج المطابقة للمخططات)
- When a JSON Schema or YAML spec is provided:
  * In C#: Generates immutable `record` or `class` with `[JsonPropertyName]` attributes and validation annotations.
  * In Python: Generates `dataclass` or `pydantic.BaseModel` with strict type hints.
  * In TypeScript/JavaScript: Generates strict interfaces and Zod/JSON-schema validators.

### Stage 3: Design-by-Contract (DbC) Binding
- Every routine calling the custom library or processing the custom schema wraps calls with preconditions (`Requires`) and postconditions (`Ensures`) reflecting the reference documentation.

### Stage 4: Static Verification Gatekeeper
- The verification agent cross-checks every external call in the generated code against the extracted Symbol Table to ensure 100% compliance before compilation.
