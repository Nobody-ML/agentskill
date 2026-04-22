#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_PHRASES = [
    "如果你要",
    "如果你需要",
    "如果你想要",
]


DEFAULT_EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    "improvement",  # reference drafts may include forbidden phrases; do not gate the skill on them
    "diagrams",  # SVGs are not scanned
}


def iter_text_files(root: Path, ex_dirs: set[str]) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in ex_dirs for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in {".md", ".txt"}:
            files.append(path)
    return files


def scan_file(path: Path, phrases: list[str]) -> list[tuple[int, str, str]]:
    matches: list[tuple[int, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        return [(0, "<read_error>", f"{exc}")]

    for idx, line in enumerate(text.splitlines(), start=1):
        for phrase in phrases:
            if phrase in line:
                matches.append((idx, phrase, line.rstrip("\n")))
    return matches


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan AgentSkill markdown/text files for forbidden phrases.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Root directory to scan (default: AgentSkill/).",
    )
    parser.add_argument(
        "--phrase",
        action="append",
        default=[],
        help="Add a forbidden phrase (repeatable).",
    )
    args = parser.parse_args()

    root: Path = args.root.resolve()
    phrases = DEFAULT_PHRASES + list(args.phrase)

    files = iter_text_files(root, DEFAULT_EXCLUDE_DIRS)
    any_hit = False
    for file_path in files:
        hits = scan_file(file_path, phrases)
        for (lineno, phrase, line) in hits:
            any_hit = True
            print(f"{file_path}:{lineno}: contains '{phrase}' -> {line}")

    if any_hit:
        print("\nResult: FAIL (forbidden phrases detected)")
        return 1

    print("Result: PASS (no forbidden phrases detected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

