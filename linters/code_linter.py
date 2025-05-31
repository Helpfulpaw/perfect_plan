#!/usr/bin/env python3
"""Simple code linter."""

import argparse
import sys
from pathlib import Path

from lint_utils import check_no_todo


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Code linter")
    parser.add_argument("files", nargs="+", help="Files to lint")
    args = parser.parse_args(argv)

    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"File not found: {path}")
            return 1
        if not check_no_todo(path):
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
