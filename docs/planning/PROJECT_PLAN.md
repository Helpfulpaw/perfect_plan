# 🚀 To‑Do List & Definition‑of‑Done (DoD)

*This file enumerates every task required to fully generate and operationalize the **Waterfall‑Docs‑Repo**. Each task includes a clear Definition of Done so contributors can verify completion.*

| #  | Task | Responsible Role | DoD (Definition of Done) | Status |
| -- | ---- | ---------------- | ------------------------ | ------ |
| 1  | **Initialize repository scaffold** (root folders `/docs`, `/src`, `/linters`, `/metrics`, `.github/workflows`) | Project Manager | All directories created, pushed to `main`, README stub present. | Pending |
| 2  | **Add README.md & LICENSE** | Project Manager | README outlines purpose & structure; LICENSE file committed; both pass `doc_linter`. | Pending |
| 3  | **Author core templates** (`ARCHITECTURE_TEMPLATE.md`, `SRS_TEMPLATE.md`, `TESTPLAN_TEMPLATE.md`, etc.) | Architect | Each template contains only section headings + field descriptions; token ≤ 3000; passes `doc_linter`. | Pending |
| 4  | **Create example artifacts** (`*_EXAMPLE.md`) demonstrating template use | Systems Analyst & Architect | Example docs fully populated for this repo, reference IDs valid, lint‑clean. | Pending |
| 5  | **Implement linters** (`doc_linter.py`, `srs_linter.py`, `testplan_linter.py`, `code_linter.py`) | Programmer | Linters execute via CLI and exit non‑zero on first rule violation; unit tests cover ≥90% branches; CI passes. | Pending |
| 6  | **Add metrics scripts** (`metrics/count_tokens.py`, `metrics/complexity.py`, `metrics/pr_latency.py`) | Architect | Scripts output JSON with metric name/value; integration test proves Prometheus push succeeds (mock). | Pending |
| 7  | **Configure CI workflows** (`ci.yml`, `metrics.yml`) | DevOps | On every PR CI runs all linters + tests; status badge green on `main`; secrets set for metrics push. | Pending |
| 8  | **Write QA Test Plan & test cases** (`docs/TEST_PLAN.md`, `docs/TEST_CASES.md`) | QA Lead | Documents exist, pass `testplan_linter`; traceability matrix links each requirement to at least one test case. | Pending |
| 9  | **Populate Role / Prompt / Linter registry** (`ROLES_PROMPTS_LINTERS.md`) | Project Manager | Table lists all roles, prompt skeletons, linter mapping; reviewed by Architect & QA. | Pending |
| 10 | **Implement architecture metrics dashboard config** (`metrics/grafana/*.json`) | DevOps | JSON dashboards imported into Grafana test instance showing real data; screenshot attached to PR. | Pending |
| 11 | **Add CONTRIBUTING.md & pre‑commit hook** to run linters pre‑push | Project Manager & Programmer | Hook blocks commit on linter failure; CONTRIBUTING lists setup steps; validated on a fresh clone. | Pending |
| 12 | **Create Maintenance & Support Plan** (`docs/MAINTENANCE_PLAN.md`) | Support Lead | Plan covers issue triage, SLAs, routine tasks; approved by PM; passes `doc_linter`. | Pending |
| 13 | **Phase‑gate review & baseline** | Project Manager | All artifacts frozen at v1.0 tag; RTM complete; milestone closed in project board. | Pending |
> **Progress Tracking:** Update the Status column and add ✅ in the DoD column once criteria are met.

---

*End of To‑Do list*
