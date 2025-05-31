import os
import subprocess
import sys
from pathlib import Path

LINTERS = [
    'linters/doc_linter.py',
    'linters/srs_linter.py',
    'linters/testplan_linter.py',
    'linters/code_linter.py',
    'linters/role_linter.py',
    'linters/diagram_linter.py',
    'linters/architecture_linter.py',
]

def run_linter(script, file):
    return subprocess.run([sys.executable, script, file], capture_output=True)

def test_linter_pass(tmp_path):
    target = tmp_path / "clean.txt"
    target.write_text("All good\n")
    role = tmp_path / "role.md"
    role.write_text("# Dev\nPrompt\n")
    diagram = tmp_path / "diagram.puml"
    diagram.write_text("@startuml\ncomponent A\nA --> B\n@enduml\n")
    for script in LINTERS:
        if script.endswith("role_linter.py"):
            file = role
        elif script.endswith("diagram_linter.py") or script.endswith("architecture_linter.py"):
            file = diagram
        else:
            file = target
        result = run_linter(script, str(file))
        assert result.returncode == 0, result.stderr

def test_linter_fail(tmp_path):
    target = tmp_path / "bad.txt"
    target.write_text("TODO: fix me\n")
    role = tmp_path / "role_bad.md"
    role.write_text("# Dev\nTODO: bad\n")
    diagram = tmp_path / "diagram_bad.puml"
    diagram.write_text("@startuml\nTODO: bad\n@enduml\n")
    for script in LINTERS:
        if script.endswith("role_linter.py"):
            file = role
        elif script.endswith("diagram_linter.py") or script.endswith("architecture_linter.py"):
            file = diagram
        else:
            file = target
        result = run_linter(script, str(file))
        assert result.returncode == 1
        assert b"contains TODO" in result.stdout
