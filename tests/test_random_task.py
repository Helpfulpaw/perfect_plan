import textwrap
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))
import random_task


def test_parse_plan(tmp_path, monkeypatch):
    plan = tmp_path / "PROJECT_PLAN.md"
    plan.write_text(textwrap.dedent(
        """
        | # | Task | Responsible Role | Reviewer Roles | DoD | Status |
        | 1 | Do thing | Dev | QA | Done when done | Pending |
        | 2 | Blocked task | Dev | QA | When done | Blocked |
        | 3 | Another | Dev | QA | When done | Done |
        """
    ))
    monkeypatch.setattr(random_task, "PLAN_PATH", plan)
    tasks = random_task.parse_plan(plan)
    assert tasks == [1]
    task = random_task.get_random_task()
    assert task == 1
