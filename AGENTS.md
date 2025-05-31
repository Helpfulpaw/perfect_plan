# Agent Instructions

The repository defines two processes: executing an existing task or creating a
new one.

## Execute a Task
If the request is to **execute a task**, follow the step-by-step instructions
provided by the script. Role prompts are located in
`docs/ROLES_PROMPTS.md` and each role may have a template under
`docs/roles/`.

## Create a Task
If the request is to **create a task**, follow `process/CREATE_TASK.md` to add
it to the project plan and create its folder.

- Work on one task at a time.

## Reflect on the Work
After completing a task:
1. Add a bullet under **Lessons Learned** summarizing what to repeat or avoid.
2. Update relevant process docs if a new step is required.

### Lessons Learned
- Avoid scanning the `tasks/` directory to discover new work. Use
  `docs/planning/PROJECT_PLAN.md` or `python src/random_task.py` to select a
  pending task.
- Record new reference documents in each task's `followups.md` so future
  contributors understand context.
