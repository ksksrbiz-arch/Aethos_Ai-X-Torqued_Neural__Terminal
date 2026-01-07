"""Registry for actuator providers."""

from __future__ import annotations

from dataclasses import dataclass, field

from aethos_ai.sensors.base import SensorReading

from .base import BaseActuator, PlannedAction
from .logger import LoggingActuator


@dataclass
class ActuatorRegistry:
    _actuators: dict[str, BaseActuator] = field(default_factory=dict)

    def load_defaults(self) -> None:
        self.register("logger", LoggingActuator())

    def register(self, name: str, actuator: BaseActuator) -> None:
        self._actuators[name] = actuator

    def available(self) -> list[str]:
        return sorted(self._actuators.keys())

    def plan(self, readings: list[SensorReading]) -> list[str]:
        return [
            f"{action.name}: {action.detail}"
            for actuator in self._actuators.values()
            for action in actuator.plan(readings)
        ]
