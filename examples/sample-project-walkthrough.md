# Example Walkthrough: Building with Custom Knowledge & Schemas

This example demonstrates how the Universal Software & AI Engineering Agency builds an application using a user-provided custom JSON schema and a specialized API reference guide.

---

## Scenario
A developer wants to build a desktop telemetry reader in Python that parses IoT sensor payloads matching a custom JSON schema and logs readings to an offline SQLite database.

---

## Step 1: User Supplies Custom Reference Files
The user creates `references/sensor_payload_schema.json`:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SensorPayload",
  "type": "object",
  "required": ["sensor_id", "timestamp", "temperature", "humidity", "status"],
  "properties": {
    "sensor_id": { "type": "string" },
    "timestamp": { "type": "integer" },
    "temperature": { "type": "number", "minimum": -50, "maximum": 100 },
    "humidity": { "type": "number", "minimum": 0, "maximum": 100 },
    "status": { "type": "string", "enum": ["NORMAL", "WARNING", "CRITICAL"] }
  }
}
```

---

## Step 2: Agency Ingests Schema & Generates Models
The agency's **Knowledge Base Specialist** parses the schema and generates `models/sensor_model.py`:
```python
from dataclasses import dataclass
from typing import Literal

@dataclass(frozen=True)
class SensorPayload:
    sensor_id: str
    timestamp: int
    temperature: float
    humidity: float
    status: Literal["NORMAL", "WARNING", "CRITICAL"]

    def __post_init__(self):
        if not (-50 <= self.temperature <= 100):
            raise ValueError(f"Temperature out of range: {self.temperature}")
        if not (0 <= self.humidity <= 100):
            raise ValueError(f"Humidity out of range: {self.humidity}")
```

---

## Step 3: Dual Blueprint Generation
The agency compiles:
1. `PRD.md`: Documenting user stories, alert thresholds, and offline storage.
2. `project_spec.json`: Mapping `models/sensor_model.py`, `storage/sqlite_store.py`, and `ui/main_window.py`.

---

## Step 4: Verification & 1-Click Launch
The agency executes `scripts/validate_code.py` across all modules and creates `run.bat` and `build_exe.bat`.
