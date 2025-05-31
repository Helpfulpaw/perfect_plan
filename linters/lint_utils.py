"""Utility functions for simple linting."""

from pathlib import Path


MARKER = "TO" + "DO"


def check_no_todo(file_path: Path) -> bool:
    """Return True if the file contains no to-do markers."""
    with file_path.open() as f:
        for lineno, line in enumerate(f, 1):
            if MARKER in line:
                print(f"{file_path}:{lineno} contains {MARKER}")
                return False
    return True
