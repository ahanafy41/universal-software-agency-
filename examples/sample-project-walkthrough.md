# Example Walkthrough: Building with Custom Knowledge, Automated Tests & Accessibility

This example demonstrates how the Universal Software & AI Engineering Agency builds a production-grade application using a user-provided custom JSON schema, proactive 2026 live search, automated unit testing, and keyboard-first accessibility.

---

## Scenario
A developer wants to build a desktop telemetry monitor in Python that parses IoT sensor payloads matching a custom JSON schema, logs readings to an offline SQLite database, provides an accessible terminal UI, and runs automated tests.

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
The agency's **Subagent A (Knowledge & Specs)** parses the schema and generates `models/sensor_model.py`:
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

## Step 3: Dual Blueprint & Architecture Generation
The agency compiles:
1. `PRD.md`: Documenting user stories, alert thresholds, and offline storage.
2. `project_spec.json`: Mapping `models/sensor_model.py`, `storage/sqlite_store.py`, `ui/accessible_dashboard.py`, and `tests/test_sensor.py`.
3. `project_mindmap.md`: Mapping 3-tier architecture with clean keyboard navigation hooks.

---

## Step 4: Automated Testing & Verification
The agency's **Subagent D (QA & Testing Engineer)** authors `tests/test_sensor.py`:
```python
import pytest
from models.sensor_model import SensorPayload

def test_valid_sensor_payload():
    payload = SensorPayload(
        sensor_id="sensor-01",
        timestamp=1700000000,
        temperature=22.5,
        humidity=45.0,
        status="NORMAL"
    )
    assert payload.sensor_id == "sensor-01"

def test_invalid_temperature_raises_value_error():
    with pytest.raises(ValueError):
        SensorPayload(
            sensor_id="sensor-01",
            timestamp=1700000000,
            temperature=150.0,
            humidity=45.0,
            status="CRITICAL"
        )
```

---

## Step 5: AST Static Analysis & 1-Click Launch
1. Run `python3 scripts/validate_code.py --strict` across all source files.
2. Provide `run.sh` / `run.bat` and `tests/run_tests.sh`.
3. Deliver `COMPLETION_REPORT.md` with the Final Verification Seal.
