# Project Architecture & Mental Topology Mapping Template (`project_mindmap.md`)

```mermaid
graph TD
    A[Presentation Tier / UI] --> B[Core Logic & Services]
    B --> C[Data Persistence & Repositories]
    B --> D[External APIs & SDKs]
    C --> E[(SQLite / Local Store)]
```

## Symbol Directory
- **UI Components**: `MainWindow`, `ContactView`
- **Core Logic**: `ContactService`, `ValidationEngine`
- **Data Repositories**: `SqliteContactRepository`
- **Diagnostic Nodes**: `app_errors.log`