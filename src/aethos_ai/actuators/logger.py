"""Simple logging actuator."""

from __future__ import annotations

from aethos_ai.sensors.base import SensorReading

from .base import BaseActuator, PlannedAction


class LoggingActuator(BaseActuator):
    name = "logger"

    def plan(self, readings: list[SensorReading]) -> list[PlannedAction]:
        return [
            PlannedAction(
                name=self.name,
                detail=f"Observed {reading.source} payload",
                reading=reading,
            )
            for reading in readings
        ]
