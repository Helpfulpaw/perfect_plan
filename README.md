# Perfect Plan Repository
[![CI](https://github.com/Helpfulpaw/perfect_plan/actions/workflows/ci.yml/badge.svg)](https://github.com/Helpfulpaw/perfect_plan/actions/workflows/ci.yml)

This repository houses planning documents and utilities for the **Waterfall-Docs-Repo** project.
The main checklist lives in [docs/planning/PROJECT_PLAN.md](docs/planning/PROJECT_PLAN.md).

For new projects, start from the [Project Plan Template](docs/planning/PROJECT_PLAN_TEMPLATE.md)
and see [PROJECT_PLAN_PROMPT.md](docs/planning/PROJECT_PLAN_PROMPT.md) for the prompt
that generated the current plan.

Role prompts are documented in [docs/ROLES_PROMPTS.md](docs/ROLES_PROMPTS.md).
Review processes are outlined in [process/PROCESS_TEMPLATE.md](process/PROCESS_TEMPLATE.md),
and dialog transcripts reside in the `tasks/` directory.

Use `python src/random_task.py` to fetch a random task from the project plan.

## Repository Structure

- `docs/` – planning documents and templates
  - `architecture/` – templates, prompts, and examples for design diagrams
  - `spc/` – specification templates and example artifacts
- `linters/` – custom linting scripts
- `metrics/` – metrics collection utilities
- `process/` – process documentation
- `src/` – project source code samples including `random_task.py`
- `tasks/` – conversation transcripts and follow-ups
- `tests/` – unit tests for repository tools

The project evolves through a series of tasks defined in the project plan.
