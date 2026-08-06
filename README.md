# Perfect Plan

A docs-as-code reference project for structuring agent-assisted software work with explicit roles, review gates, templates, linters, and CI.

> **Status:** experimental reference implementation. The repository demonstrates a workflow and supporting utilities; it is not a finished project-management product or a drop-in replacement for an issue tracker.

## Why this exists

Agent-assisted projects often accumulate plans, prompts, architecture notes, and test artifacts without a consistent structure or a way to check them. Perfect Plan explores a stricter model:

- project artifacts live in version control;
- each task has an accountable role and reviewer;
- templates encode the expected document structure;
- lightweight linters detect missing or malformed sections;
- CI checks documentation and code on every change;
- agent instructions describe how work is selected, executed, reviewed, and reflected back into the process.

## What is included

- Project-plan and specification templates
- Architecture and sequence-diagram examples
- Role definitions and role-specific prompts
- Markdown, SRS, test-plan, code, and diagram linters
- Pytest coverage for the command-line utilities
- GitHub Actions workflows for linting, tests, and repository metrics
- A small task selector used by the agent workflow
- Process documents for creating and executing tasks

## Repository map

```text
.
├── AGENTS.md                 # Instructions for agents working in the repository
├── docs/
│   ├── planning/             # Project plan, prompt, and reusable template
│   ├── architecture/         # Architecture templates and examples
│   ├── roles/                # Role definitions
│   └── spc/                  # Specification templates and examples
├── linters/                  # Documentation and code checks
├── metrics/                  # Repository metric utilities
├── process/                  # Task creation and execution workflows
├── src/                      # Supporting Python utilities
├── tasks/                    # Task-level working artifacts
└── tests/                    # Pytest suite
```

## Try it locally

Requirements: Python 3.10+ and Git.

```bash
git clone https://github.com/Helpfulpaw/perfect_plan.git
cd perfect_plan

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip pytest

pytest -q
python src/random_task.py
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

The CI workflow also demonstrates the full linter invocation in [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

## Core workflow

1. Define or select a task from [`docs/planning/PROJECT_PLAN.md`](docs/planning/PROJECT_PLAN.md).
2. Resolve the responsible role and reviewer.
3. Produce the required artifact from a repository template.
4. Run the relevant linters and tests.
5. Review the artifact against its Definition of Done.
6. Record lessons learned and update the process when a repeatable improvement is found.

See [`AGENTS.md`](AGENTS.md) for the repository's agent-facing instructions.

## Current limitations

- The project plan contains both completed examples and unfinished exploratory work.
- Several templates and role documents are intentionally minimal.
- The workflow has not yet been packaged as a reusable CLI or project generator.
- There is no compatibility matrix for different coding-agent environments.
- Metrics and process checks are prototypes rather than production observability.

## Good uses

This repository is most useful as:

- a reference for docs-as-code project governance;
- a starting point for agent instruction and artifact conventions;
- an example of validating project documents in CI;
- a source of templates and small utilities to adapt into another repository.

It should not be treated as a finished methodology without adapting the roles, gates, and artifacts to the project's actual risk.

## License

MIT. See [`LICENSE`](LICENSE).
