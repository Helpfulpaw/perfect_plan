# Agent Instructions

The repository defines processes for creating and executing tasks.

## Execute a Task
1. Locate the active task in `docs/planning/PROJECT_PLAN.md`.
2. Review the prompts for the responsible and reviewer roles in
   `docs/ROLES_PROMPTS.md`.
3. Read any notes for the task in `tasks/task_XX/`.
4. Record dialog and decisions in `tasks/task_XX/README.md` and update
   `followups.md` with dependencies.
5. Follow the checklist in `process/PROCESS_TEMPLATE.md`.

More detail is available in `process/EXECUTE_TASK.md`.

## Create a Task
When defining a new task or follow-up, use `process/CREATE_TASK.md` for the
steps to add it to the project plan and initialize the task folder.

- Work on one task at a time.

## Reflect on the Work
After completing a task:
1. Add a bullet under **Lessons Learned** summarizing what to repeat or avoid.
2. Update relevant process docs if a new step is required.

### Lessons Learned
- Avoid scanning the `tasks/` directory to discover new work. Use
  `docs/planning/PROJECT_PLAN.md` or `python src/random_task.py` to select a
  pending task.
