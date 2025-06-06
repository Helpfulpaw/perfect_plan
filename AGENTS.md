# Agent Instructions

The repository defines two processes: executing an existing task or creating a
new one.

## Execute a Task
If the request is to **execute a task**, run `python src/random_task.py` to select a pending task. The script prints the responsible role's prompt and the contents of `process/EXECUTE_TASK.md`.

## Create a Task
If the request is to **create a task**, follow `process/CREATE_TASK.md` to add
it to the project plan and create its folder.

- Work on one task at a time.

## Reflect on the Work
After completing a task:
1. Add a bullet under **Lessons Learned** summarizing what to repeat or avoid.
2. Update relevant process docs if a new step is required.

### Lessons Learned

- Ensure test plans include a traceability matrix linking each requirement to at least one test case.
- Keep diagram examples minimal so linters remain simple.
- Verify role documents with `doc_linter` after updating methodologies.
- Place architecture templates in a dedicated folder and provide a specific linter.
- Create combined role prompt files when tasks reference multiple roles to avoid script errors.
- Clarify artifact ownership by including a `Responsible Role` section in templates.
- Confirm prerequisite tasks are completed before marking dependent tasks
- Provide detailed methodology bullet points when documenting each role.
- Leave a task pending if prerequisites are incomplete, even when the artifact is finished
