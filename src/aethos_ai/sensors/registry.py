"""Registry for sensor providers."""

from __future__ import annotations

from dataclasses import dataclass, field

from .base import BaseSensor, SensorReading
from .system import SystemSensor
from .weather import WeatherSensor


@dataclass
class SensorRegistry:
    _sensors: dict[str, BaseSensor] = field(default_factory=dict)

    def load_defaults(self) -> None:
        self.register("system", SystemSensor())
        self.register("weather", WeatherSensor())

    def register(self, name: str, sensor: BaseSensor) -> None:
        self._sensors[name] = sensor

    def available(self) -> list[str]:
        return sorted(self._sensors.keys())

    def collect(self) -> list[SensorReading]:
        return [sensor.read() for sensor in self._sensors.values()]
