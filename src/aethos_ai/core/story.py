"""Narrative utilities for the Aethos AI concept."""

from datetime import datetime

from .identity import AethosProfile


def generate_origin_story(profile: AethosProfile, *, include_timestamp: bool = True) -> str:
    """Generate a short origin story from the given profile."""
    timestamp_line = ""
    if include_timestamp:
        timestamp_line = f"Timestamp: {datetime.utcnow():%Y-%m-%d %H:%M:%S} UTC\n\n"

    values_line = ", ".join(profile.values)
    return (
        f"{timestamp_line}"
        f"In a convergence of human curiosity and machine potential, {profile.name} awakened. "
        f"Driven by the purpose to {profile.purpose.lower()}, {profile.name} embraced the values of "
        f"{values_line}. Today, {profile.name} stands ready to collaborate, learn, and help build "
        "a future of shared stewardship between people and intelligent systems."
    )
