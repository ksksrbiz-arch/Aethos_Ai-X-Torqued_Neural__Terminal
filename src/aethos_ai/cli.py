"""Command-line interface for Aethos AI."""
"""Command-line interface for the Aethos AI starter kit."""

from __future__ import annotations

import argparse
import json

from aethos_ai.config import AethosConfig
from aethos_ai.logging import setup_logging
from aethos_ai.orchestrator import Orchestrator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Aethos AI control surface")
    parser.add_argument("--log-level", default=None, help="Override log level")

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("status", help="Show current status")

    run_parser = subparsers.add_parser("run", help="Run a single orchestration cycle")
    run_parser.add_argument("--emit-json", action="store_true", help="Emit JSON output")
from dataclasses import asdict

from .core.identity import AethosProfile
from .core.story import generate_origin_story


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aethos",
        description="Aethos AI starter toolkit",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("about", help="Show the default Aethos profile summary.")

    story_parser = subparsers.add_parser("story", help="Generate an Aethos origin story.")
    story_parser.add_argument("--no-timestamp", action="store_true", help="Omit timestamps.")

    manifest_parser = subparsers.add_parser("manifest", help="Output the profile manifest JSON.")
    manifest_parser.add_argument("--indent", type=int, default=2, help="JSON indentation level.")

    greet_parser = subparsers.add_parser("greet", help="Personalize the profile greeting.")
    greet_parser.add_argument("name", help="Name to greet.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    config = AethosConfig.from_env()
    log_level = args.log_level or config.log_level
    setup_logging(log_level)

    orchestrator = Orchestrator(config=config)
    orchestrator.boot()

    if args.command == "status":
        status = orchestrator.status()
        print(json.dumps(status, indent=2))
        return

    if args.command == "run":
        actions = list(orchestrator.run_cycle())
        if args.emit_json:
            print(json.dumps({"actions": actions}, indent=2))
        else:
            for action in actions:
                print(action)
        return

    raise SystemExit("Unknown command")
def handle_about(profile: AethosProfile) -> str:
    return profile.summary()


def handle_story(profile: AethosProfile, *, include_timestamp: bool) -> str:
    return generate_origin_story(profile, include_timestamp=include_timestamp)


def handle_manifest(profile: AethosProfile, indent: int) -> str:
    return json.dumps(profile.to_manifest(), indent=indent)


def handle_greet(profile: AethosProfile, name: str) -> str:
    return (
        f"Hello {name}, {profile.name} is ready to collaborate. "
        f"Shared values: {', '.join(profile.values)}."
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    profile = AethosProfile()

    if args.command == "about":
        print(handle_about(profile))
    elif args.command == "story":
        print(handle_story(profile, include_timestamp=not args.no_timestamp))
    elif args.command == "manifest":
        print(handle_manifest(profile, indent=args.indent))
    elif args.command == "greet":
        print(handle_greet(profile, args.name))
    else:
        parser.error("Unknown command")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
