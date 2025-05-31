# Create Task Process

Use this process whenever you add a new task or generate a follow-up task.

1. Review `docs/planning/PROJECT_PLAN.md` to determine the next task number.
2. Define the task summary, Responsible Role and Reviewer Roles. Ensure the
   roles exist in `docs/ROLES_PROMPTS.md`.
3. Append a new row to `docs/planning/PROJECT_PLAN.md` with the task details and
   status `Pending`.
4. Create a directory `tasks/task_XX` where `XX` is the task number.
   - Add `README.md` with the heading `# Dialogs for task XX`.
   - Add `followups.md` and list any dependencies in the form
     `Depends on: <task numbers>`.
5. Decompose large work into smaller follow-up tasks and record them in
   `followups.md`.
6. Reference related documentation using relative paths.
7. If the task introduces a new role or linter, update
   `docs/ROLES_PROMPTS_LINTERS.md` to keep the registry current.

