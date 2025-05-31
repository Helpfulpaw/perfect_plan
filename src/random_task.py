#!/usr/bin/env python3
"""Select a random unblocked task and load its role prompt."""

import random
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT_DIR / "docs" / "planning" / "PROJECT_PLAN.md"
ROLES_DIR = ROOT_DIR / "docs" / "roles"


def slugify(role: str) -> str:
    return role.lower().replace(" ", "_")


def load_role_prompt(role: str) -> str:
    path = ROLES_DIR / f"{slugify(role)}.md"
    lines = path.read_text().splitlines()
    return lines[1].strip() if len(lines) > 1 else ""


def parse_plan(plan_path: Path) -> list[dict]:
    tasks = []
    with plan_path.open() as f:
        for line in f:
            if line.startswith('|') and line.count('|') >= 6:
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if not cells[0].isdigit():
                    continue
                tasks.append({
                    "id": int(cells[0]),
                    "task": cells[1],
                    "role": cells[2],
                    "reviewers": cells[3],
                    "dod": cells[4],
                    "status": cells[5].lower(),
                })
    return tasks


def get_random_task() -> dict | None:
    tasks = [t for t in parse_plan(PLAN_PATH) if t["status"] not in {"done", "blocked"}]
    if not tasks:
        return None
    chosen = random.choice(tasks)
    chosen["prompt"] = load_role_prompt(chosen["role"])
    chosen["root"] = str(ROOT_DIR)
    return chosen


def main() -> int:
    task = get_random_task()
    if task is None:
        print("No pending tasks")
        return 1
    print(f"task_{task['id']:02d}")
    print(task["task"])
    print(task["prompt"])
    print(task["root"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
