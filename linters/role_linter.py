#!/usr/bin/env python3
"""Linter for individual role prompt files."""

import argparse
import sys
from pathlib import Path

from lint_utils import check_no_todo


def check_role_file(path: Path) -> bool:
    lines = path.read_text().splitlines()
    if len(lines) != 2:
        print(f"{path}: file must contain exactly two lines")
        return False
    if not lines[0].startswith("# "):
        print(f"{path}: first line must start with '# '")
        return False
    if not lines[1].strip():
        print(f"{path}: second line must contain prompt text")
        return False
    if not check_no_todo(path):
        return False
    return True


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Role prompt linter")
    parser.add_argument("files", nargs="+", help="Role files to lint")
    args = parser.parse_args(argv)

    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"File not found: {path}")
            return 1
        if not check_role_file(path):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
