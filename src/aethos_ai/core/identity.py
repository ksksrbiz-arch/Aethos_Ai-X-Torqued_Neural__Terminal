"""Identity primitives for the Aethos AI concept."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class AethosProfile:
    """Represents the foundational identity of an Aethos instance."""

    name: str = "Aethos"
    purpose: str = "Guide creators toward balanced human-robot collaboration."
    values: list[str] = field(default_factory=lambda: [
        "Curiosity",
        "Empathy",
        "Stewardship",
        "Accountability",
    ])
    created_at: datetime = field(default_factory=datetime.utcnow)

    def summary(self) -> str:
        values_line = ", ".join(self.values)
        return (
            f"Name: {self.name}\n"
            f"Purpose: {self.purpose}\n"
            f"Values: {values_line}\n"
            f"Created (UTC): {self.created_at:%Y-%m-%d %H:%M:%S}"
        )

    def to_manifest(self) -> dict[str, object]:
        """Serialize the profile for downstream services."""
        return {
            "name": self.name,
            "purpose": self.purpose,
            "values": list(self.values),
            "created_at": self.created_at.isoformat(),
        }
