#!/usr/bin/env python3
"""Linter for architecture diagrams."""

import argparse
import sys
from pathlib import Path

from lint_utils import check_no_todo
from diagram_linter import check_puml


def check_arch_diagram(path: Path) -> bool:
    """Validate PlantUML architecture diagram."""
    if not check_puml(path):
        return False
    lines = path.read_text().splitlines()
    if not any("component" in line for line in lines):
        print(f"{path}: architecture diagram should define at least one component")
        return False
    return True


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Architecture linter")
    parser.add_argument("files", nargs="+", help="Files to lint")
    args = parser.parse_args(argv)

    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"File not found: {path}")
            return 1
        if not check_no_todo(path):
            return 1
        if path.suffix == ".puml" and not check_arch_diagram(path):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
