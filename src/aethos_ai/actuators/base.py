"""Actuator interfaces."""

from __future__ import annotations

from dataclasses import dataclass

from aethos_ai.sensors.base import SensorReading


@dataclass
class PlannedAction:
    name: str
    detail: str
    reading: SensorReading | None = None


class BaseActuator:
    name: str = "base"

    def plan(self, readings: list[SensorReading]) -> list[PlannedAction]:
        return []
