#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_MARKERS = [
    "# State",
    "Memory",
    "Decision Log",
    "Evidence Index",
    "Next Action",
]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate that State.md contains the minimum long-running workflow fields.",
    )
    parser.add_argument(
        "--state",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "State.md",
        help="Path to State.md (default: AgentSkill/State.md).",
    )
    args = parser.parse_args()

    state_path: Path = args.state.resolve()
    if not state_path.exists():
        print(f"State: FAIL (file not found): {state_path}")
        return 1

    text = state_path.read_text(encoding="utf-8", errors="replace")
    missing: list[str] = [m for m in REQUIRED_MARKERS if m not in text]
    if missing:
        for m in missing:
            print(f"State: missing marker: {m!r}")
        print("Result: FAIL (State.md missing required markers)")
        return 1

    print("Result: PASS (State.md contains required markers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

