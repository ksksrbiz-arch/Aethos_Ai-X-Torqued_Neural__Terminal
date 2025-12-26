"""Command-line interface for the Aethos AI starter kit."""

from __future__ import annotations

import argparse
import json
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
