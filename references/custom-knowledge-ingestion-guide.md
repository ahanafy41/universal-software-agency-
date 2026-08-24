# Custom Knowledge, Docs & Schema Ingestion Guide (دليل استيعاب المعارف والمواصفات المخصصة)

Protocol for parsing and compiling user-provided markdown documentation, custom JSON schemas, proprietary SDK guides, and domain-specific rules into strongly typed, zero-hallucination code models.

---

## 1. Zero-Hallucination Ingestion Invariant
When the user provides files in `docs/` or `references/` (Markdown files, JSON schemas, API specs, type definitions):
1. **Source of Truth**: These files serve as the definitive contract for all naming, data types, validation constraints, and API methods.
2. **Catalog Indexing**: Ingest all reference files into `references_manifest.json` conforming to `references/references-manifest-schema.json`.
3. **Model Generation**: Automatically synthesize typed models matching the schema across target languages (Python dataclasses/Pydantic, C# records, TypeScript interfaces, Rust structs, Go types).

---

## 2. Multi-Language Model Synthesis Examples

### Python (Pydantic / Dataclass)
```python
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class UserProfile:
    id: str
    username: str
    email: str
    is_active: bool = True
```

### C# .NET Record
```csharp
namespace MyProject.Core.Models;

public record UserProfile(
    string Id,
    string Username,
    string Email,
    bool IsActive = true
);
```

### TypeScript Interface
```typescript
export interface UserProfile {
  id: string;
  username: string;
  email: string;
  isActive: boolean;
}
```

### Rust Struct
```rust
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct UserProfile {
    pub id: String,
    pub username: String,
    pub email: String,
    pub is_active: bool,
}
```
