"""Sensor interfaces."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class SensorReading:
    source: str
    timestamp: datetime
    payload: dict[str, object]


class BaseSensor:
    name: str = "base"

    def read(self) -> SensorReading:
        return SensorReading(source=self.name, timestamp=datetime.utcnow(), payload={})
