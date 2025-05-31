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
    role_dir = tmp_path / "roles"
    role_dir.mkdir()
    (role_dir / "dev.md").write_text("# Dev\nPrompt\n")
    exec_file = tmp_path / "EXECUTE_TASK.md"
    exec_file.write_text("Do it\n")
    monkeypatch.setattr(random_task, "ROOT_DIR", tmp_path)
    monkeypatch.setattr(random_task, "PLAN_PATH", plan)
    monkeypatch.setattr(random_task, "ROLES_DIR", role_dir)
    monkeypatch.setattr(random_task, "EXECUTE_PATH", exec_file)
    tasks = random_task.parse_plan(plan)
    assert tasks[0]["id"] == 1
    task = random_task.get_random_task()
    assert task["id"] == 1
    assert task["prompt"] == "Prompt"
    assert task["instructions"] == "Do it"
    assert task["root"] == str(tmp_path)
