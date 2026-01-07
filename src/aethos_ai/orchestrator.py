"""Core orchestration for Aethos AI."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Iterable

from .config import AethosConfig
from .integrations.registry import IntegrationRegistry
from .memory.store import MemoryStore
from .sensors.registry import SensorRegistry
from .actuators.registry import ActuatorRegistry

logger = logging.getLogger(__name__)


@dataclass
class Orchestrator:
    """Coordinates integrations, sensors, and actuators."""

    config: AethosConfig
    integrations: IntegrationRegistry = field(default_factory=IntegrationRegistry)
    sensors: SensorRegistry = field(default_factory=SensorRegistry)
    actuators: ActuatorRegistry = field(default_factory=ActuatorRegistry)
    memory: MemoryStore | None = None

    def boot(self) -> None:
        logger.info("Booting Aethos profile '%s'", self.config.profile)
        self.config.data_dir.mkdir(parents=True, exist_ok=True)
        self.memory = MemoryStore(self.config.data_dir / "memory.db")
        self.memory.initialize()
        self.integrations.load_defaults()
        self.sensors.load_defaults()
        self.actuators.load_defaults()
        logger.info("Aethos boot sequence completed")

    def status(self) -> dict[str, object]:
        return {
            "profile": self.config.profile,
            "integrations": self.integrations.available(),
            "integration_statuses": [
                status.__dict__ for status in self.integrations.statuses()
            ],
            "sensors": self.sensors.available(),
            "actuators": self.actuators.available(),
            "memory_path": str(self.memory.path) if self.memory else None,
        }

    def run_cycle(self) -> Iterable[str]:
        """Run a single perception-decision-action cycle."""

        if self.memory is None:
            raise RuntimeError("Orchestrator must be booted before running cycles")
        readings = self.sensors.collect()
        summary = f"Collected {len(readings)} sensor readings"
        self.memory.write_event("sensor", summary)
        logger.info(summary)
        actions = self.actuators.plan(readings)
        for action in actions:
            self.memory.write_event("actuator", action)
            yield action
