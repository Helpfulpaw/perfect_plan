import os
import subprocess
import sys
from pathlib import Path

LINTERS = [
    'linters/doc_linter.py',
    'linters/srs_linter.py',
    'linters/testplan_linter.py',
    'linters/code_linter.py',
]

def run_linter(script, file):
    return subprocess.run([sys.executable, script, file], capture_output=True)

def test_linter_pass(tmp_path):
    target = tmp_path / "clean.txt"
    target.write_text("All good\n")
    for script in LINTERS:
        result = run_linter(script, str(target))
        assert result.returncode == 0, result.stderr

def test_linter_fail(tmp_path):
    target = tmp_path / "bad.txt"
    target.write_text("TODO: fix me\n")
    for script in LINTERS:
        result = run_linter(script, str(target))
        assert result.returncode == 1
        assert b"contains TODO" in result.stdout
