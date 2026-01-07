"""Configuration primitives for Aethos AI."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _env(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)


@dataclass(frozen=True)
class AethosConfig:
    """Runtime configuration for the orchestrator."""

    profile: str
    data_dir: Path
    log_level: str

    @classmethod
    def from_env(cls) -> "AethosConfig":
        profile = _env("AETHOS_PROFILE", "local")
        data_dir = Path(_env("AETHOS_DATA_DIR", ".aethos"))
        log_level = _env("AETHOS_LOG_LEVEL", "INFO")
        return cls(profile=profile, data_dir=data_dir, log_level=log_level)
