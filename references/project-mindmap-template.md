# Project Mental Topology & Mindmap Protocol (`project_mindmap.md`)

```markdown
# 🗺️ Project Mental Topology & Architecture Mindmap

```mermaid
graph TD
    subgraph UI_Layer [UI & Universal Accessibility Tier]
        MainWindow[Accessible UI / Terminal Dashboard]
        KeyNav[Keyboard Navigation & Focus Manager]
    end

    subgraph Core_Layer [Core Logic & State Management]
        AppService[Application Service & Business Rules]
        StateEngine[Finite State Machine]
    end

    subgraph Data_Layer [Data & Persistence Tier]
        Repository[Data Repository]
        LocalDB[(Offline SQLite / JSON Store)]
    end

    subgraph Testing_DevOps [QA & Automation]
        Tests[Automated Test Suite]
        Docker[Multi-stage Dockerfile]
    end

    MainWindow --> KeyNav
    MainWindow --> AppService
    AppService --> StateEngine
    AppService --> Repository
    Repository --> LocalDB
    Tests --> AppService
    Tests --> Repository
```

---

## 🔎 Rapid Search & Symbol Index

| Tier / Layer | Component / File | Key Classes / Functions | Responsibility |
| :--- | :--- | :--- | :--- |
| **UI** | `ui/accessible_dashboard.py` | `DashboardView` | Keyboard-first rendering |
| **Core** | `core/business_service.py` | `AppService` | Domain operations |
| **Data** | `data/sqlite_store.py` | `DatabaseContext` | Atomic data storage |
| **Tests** | `tests/test_service.py` | `test_valid_operations` | Automated unit testing |
```
