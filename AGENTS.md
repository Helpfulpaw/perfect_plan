# Agent Instructions

The repository defines two processes: executing an existing task or creating a
new one.

## Execute a Task
If the request is to **execute a task**, run `python src/random_task.py` to select a pending task. Then open the responsible role's prompt under `docs/roles/` and follow `process/EXECUTE_TASK.md`.

## Create a Task
If the request is to **create a task**, follow `process/CREATE_TASK.md` to add
it to the project plan and create its folder.

- Work on one task at a time.

## Reflect on the Work
After completing a task:
1. Add a bullet under **Lessons Learned** summarizing what to repeat or avoid.
2. Update relevant process docs if a new step is required.

### Lessons Learned
- Use stub commands in CI when dependencies are incomplete to keep workflows passing.
- Exclude test fixtures from repository-wide linters to avoid false failures.
- Record new reference documents in each task's `followups.md` so future
  contributors understand context.
- Split role prompts into individual files under `docs/roles/` and added a linter to enforce their format.
- Keep the role/prompt/linter registry updated whenever new roles or linters are introduced.
- Capture retrospectives on redundant steps to refine future processes.
