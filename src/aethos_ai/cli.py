"""Command-line interface for Aethos AI."""

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
