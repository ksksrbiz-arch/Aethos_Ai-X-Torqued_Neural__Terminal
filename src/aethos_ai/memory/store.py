"""SQLite-backed memory store."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class MemoryStore:
    path: Path

    def initialize(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    detail TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            connection.commit()

    def write_event(self, category: str, detail: str) -> None:
        timestamp = datetime.utcnow().isoformat()
        with sqlite3.connect(self.path) as connection:
            connection.execute(
                "INSERT INTO events (category, detail, created_at) VALUES (?, ?, ?)",
                (category, detail, timestamp),
            )
            connection.commit()
