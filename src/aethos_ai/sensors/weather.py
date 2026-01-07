"""Placeholder weather sensor."""

from __future__ import annotations

from datetime import datetime

from .base import BaseSensor, SensorReading


class WeatherSensor(BaseSensor):
    name = "weather"

    def read(self) -> SensorReading:
        payload = {
            "status": "unconfigured",
            "temperature_c": None,
        }
        return SensorReading(source=self.name, timestamp=datetime.utcnow(), payload=payload)
