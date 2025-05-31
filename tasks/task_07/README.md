# Dialogs for task 07

## Review for Task 7
**Responsible:** DevOps
**Reviewer:** Programmer

### Task Description
Configure CI workflows (`ci.yml`, `metrics.yml`). On every PR CI runs all linters + tests; status badge green on `main`; secrets set for metrics push.

### Review Notes
- **Clarity:** Workflows must install Python, run tests, run custom linters, and prepare for metrics publishing.
- **Blockers:** Metrics scripts from task 6 are not yet available, so the metrics workflow uses placeholder commands.
- **Resources:** `docs/planning/PROJECT_PLAN.md`, GitHub Actions examples.

## AI Notes 2025-06-01
- Created `.github/workflows/ci.yml` running pytest and linters on push and pull requests.
- Added `.github/workflows/metrics.yml` with placeholder metrics steps and secret `METRICS_ENDPOINT`.
- Inserted CI status badge in `README.md`.
- Updated followups to remind integration once metrics scripts exist.
