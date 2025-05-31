#!/usr/bin/env python3
"""Simple PlantUML diagram linter."""

import argparse
import sys
from pathlib import Path

from lint_utils import check_no_todo


def check_puml(path: Path) -> bool:
    lines = path.read_text().splitlines()
    if not lines:
        print(f"{path}: file is empty")
        return False
    if not lines[0].startswith('@start'):
        print(f"{path}: missing @startuml")
        return False
    if not lines[-1].startswith('@end'):
        print(f"{path}: missing @enduml")
        return False
    return True


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Diagram linter")
    parser.add_argument("files", nargs="+", help="Diagram files to lint")
    args = parser.parse_args(argv)

    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"File not found: {path}")
            return 1
        if not check_no_todo(path):
            return 1
        if path.suffix == '.puml' and not check_puml(path):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
