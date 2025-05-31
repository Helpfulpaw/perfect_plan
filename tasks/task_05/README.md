# Dialogs for task 05

## Review for Task 5
**Responsible:** Programmer
**Reviewer:** QA Lead

### Task Description
Implement linters `doc_linter.py`, `srs_linter.py`, `testplan_linter.py`, `code_linter.py`. Linters execute via CLI and exit non-zero on first rule violation; unit tests cover ≥90% branches; CI passes.

### Review Notes
- **Clarity:** DoD specifies execution and coverage targets, but specific lint rules and dependencies are not yet defined.
- **Blockers:** Need guidance on required libraries and rule sets before implementing logic.
- **Resources:** Will consult project stakeholders for recommended linting libraries.
- Placeholder linter scripts will be created with basic CLI to ensure they run.

## AI Notes 2024-05-25
- Checked prompts for **Programmer** and **QA Lead** in `docs/ROLES_PROMPTS.md`.
- Verified task description in `docs/planning/PROJECT_PLAN.md`.
- Decided to keep placeholder lint rules; each linter will fail if a file contains the string `TODO`.
- Will add unit tests invoking the CLI via `subprocess.run` and expect proper exit codes.
