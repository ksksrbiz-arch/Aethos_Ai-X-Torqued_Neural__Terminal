"""System telemetry sensor."""

from __future__ import annotations

import os
from datetime import datetime

from .base import BaseSensor, SensorReading


class SystemSensor(BaseSensor):
    name = "system"

    def read(self) -> SensorReading:
        payload = {
            "pid": os.getpid(),
            "cwd": os.getcwd(),
        }
        return SensorReading(source=self.name, timestamp=datetime.utcnow(), payload=payload)
