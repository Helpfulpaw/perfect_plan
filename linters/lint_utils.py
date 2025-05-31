"""Utility functions for simple linting."""

from pathlib import Path


def check_no_todo(file_path: Path) -> bool:
    """Return True if the file contains no 'TODO' markers."""
    with file_path.open() as f:
        for lineno, line in enumerate(f, 1):
            if "TODO" in line:
                print(f"{file_path}:{lineno} contains TODO")
                return False
    return True
