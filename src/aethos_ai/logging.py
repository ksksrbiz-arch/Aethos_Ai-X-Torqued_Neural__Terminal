"""Logging helpers for Aethos AI."""

from __future__ import annotations

import logging


def setup_logging(level: str) -> None:
    """Initialize logging configuration."""

    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
