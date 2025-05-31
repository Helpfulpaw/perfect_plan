#!/usr/bin/env python3
"""Select a random unblocked task from PROJECT_PLAN.md."""

import random
from pathlib import Path

PLAN_PATH = Path(__file__).resolve().parents[1] / "docs" / "planning" / "PROJECT_PLAN.md"


def parse_plan(plan_path: Path) -> list:
    tasks = []
    with plan_path.open() as f:
        for line in f:
            if line.startswith('|') and line.count('|') >= 6:
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if not cells[0].isdigit():
                    continue
                status = cells[-1].lower()
                if status not in {"done", "blocked"}:
                    tasks.append(int(cells[0]))
    return tasks


def get_random_task() -> int | None:
    avail = parse_plan(PLAN_PATH)
    return random.choice(avail) if avail else None


def main() -> int:
    task = get_random_task()
    if task is None:
        print("No pending tasks")
        return 1
    print(f"task_{task:02d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
