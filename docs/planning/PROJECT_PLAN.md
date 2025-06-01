# 🚀 To‑Do List & Definition‑of‑Done (DoD)

*This file enumerates every task required to fully generate and operationalize the **Waterfall‑Docs‑Repo**. Each task includes a clear Definition of Done so contributors can verify completion.*

| #  | Task | Responsible Role | Reviewer Roles | DoD (Definition of Done) | Status |
| -- | ---- | ---------------- | -------------- | ------------------------ | ------ |
| 0  | **Create reviewer roles and prompts** (`docs/ROLES_PROMPTS.md`, `AGENTS.md`) | Project Manager | Architect | Roles file with prompts exists; root instructions reference it. | Done |
| 1  | **Initialize repository scaffold** (root folders `/docs`, `/src`, `/linters`, `/metrics`, `.github/workflows`) | Project Manager | Architect | All directories created, pushed to `main`, README stub present. ✅ | Done |
| 2  | **Add README.md & LICENSE** | Project Manager | Systems Analyst | README outlines purpose & structure; LICENSE file committed; both pass `doc_linter`. ✅ | Done |
| 3  | **Author core templates** (`docs/architecture/ARCHITECTURE_TEMPLATE.md`, `SRS_TEMPLATE.md`, `TESTPLAN_TEMPLATE.md`, etc.) | Architect | Project Manager | Each template contains only section headings + field descriptions; token ≤ 3000; passes `doc_linter`. ✅ | Done |
| 4  | **Create example artifacts** (`*_EXAMPLE.md`) demonstrating template use | Systems Analyst & Architect | QA Lead | Example docs fully populated for this repo, reference IDs valid, lint‑clean. | Pending |
| 5  | **Implement linters** (`doc_linter.py`, `srs_linter.py`, `testplan_linter.py`, `code_linter.py`) | Programmer | QA Lead | Linters execute via CLI and exit non‑zero on first rule violation; unit tests cover ≥90% branches; CI passes. ✅ | Done |
| 6  | **Add metrics scripts** (`metrics/count_tokens.py`, `metrics/complexity.py`, `metrics/pr_latency.py`) | Architect | DevOps | Scripts output JSON with metric name/value; integration test proves Prometheus push succeeds (mock). | Pending |
| 7  | **Configure CI workflows** (`ci.yml`, `metrics.yml`) | DevOps | Programmer | On every PR CI runs all linters + tests; status badge green on `main`; secrets set for metrics push. | Pending |
| 8  | **Write QA Test Plan & test cases** (`docs/TEST_PLAN.md`, `docs/TEST_CASES.md`) | QA Lead | Support Lead | Documents exist, pass `testplan_linter`; traceability matrix links each requirement to at least one test case. ✅ | Done |
| 9  | **Populate Role / Prompt / Linter registry** (`ROLES_PROMPTS_LINTERS.md`) | Project Manager | Architect | Table lists all roles, prompt skeletons, linter mapping; reviewed by Architect & QA. ✅ | Done |
| 10 | **Implement architecture metrics dashboard config** (`metrics/grafana/*.json`) | DevOps | Architect | JSON dashboards imported into Grafana test instance showing real data; screenshot attached to PR. | Pending |
| 11 | **Add CONTRIBUTING.md & pre‑commit hook** to run linters pre‑push | Project Manager & Programmer | QA Lead | Hook blocks commit on linter failure; CONTRIBUTING lists setup steps; validated on a fresh clone. | Pending |
| 12 | **Create Maintenance & Support Plan** (`docs/MAINTENANCE_PLAN.md`) | Support Lead | Project Manager | Plan covers issue triage, SLAs, routine tasks; approved by PM; passes `doc_linter`. | Pending |
| 13 | **Phase‑gate review & baseline** | Project Manager | Architect, QA Lead | All artifacts frozen at v1.0 tag; RTM complete; milestone closed in project board. | Pending |
| 14 | **Audit task list for role & reviewer coverage** | Project Manager | Architect | Every task has clearly defined responsible and reviewer roles. | Pending |
| 15 | **Add task DAG linter** (`linters/task_dag_linter.py`) | Programmer | QA Lead | Linter verifies tasks form a DAG and docs are up to date. | Pending |
| 16 | **Populate architecture folder** (`docs/architecture/`) with templates, prompts, example diagrams and dedicated linters | Architect | Project Manager | Folder README outlines structure; files exist as separate templates, prompts, examples; each diagram validated by its linter. ✅ | Done |
| 17 | **Populate specification folder** (`docs/spc/`) with templates, prompts, examples and diagram linters | Systems Analyst | Architect | README explains layout; individual files added; lint passes for each diagram. ✅ | Done |
| 18 | **Research retrospective on redundant steps** | Project Manager | Architect | Document detailing redundant steps and lessons learned added to `docs/RESEARCH_RETROSPECTIVE.md`. ✅ | Done |
| 19 | **Create roles folder with templates** (`docs/roles/`) | Project Manager | Architect | Folder contains one template per role and a README explaining usage. | Pending |

| 20 | **Define Project Manager methodologies** (`docs/roles/project_manager.md`) | Project Manager | Architect | Document lists Agile and Waterfall best practices; passes `doc_linter`. | Pending |
| 21 | **Define Architect methodologies** (`docs/roles/architect.md`) | Architect | Programmer | Document details Domain-Driven Design and patterns; passes `doc_linter`. | Pending |
| 22 | **Define Systems Analyst methodologies** (`docs/roles/systems_analyst.md`) | Systems Analyst | Architect | Document explains requirement analysis methods; passes `doc_linter`. | Pending |
| 23 | **Define Programmer methodologies** (`docs/roles/programmer.md`) | Programmer | QA Lead | Document describes TDD, DRY, OOP approach; passes `doc_linter`. | Pending |
| 24 | **Define DevOps methodologies** (`docs/roles/devops.md`) | DevOps | QA Lead | Document covers CI/CD and IaC guidelines; passes `doc_linter`. ✅ | Done |
| 25 | **Define QA Lead methodologies** (`docs/roles/qa_lead.md`) | QA Lead | Support Lead | Document describes test automation and BDD; passes `doc_linter`. ✅ | Done |
| 26 | **Define Support Lead methodologies** (`docs/roles/support_lead.md`) | Support Lead | Project Manager | Document includes ITIL processes and root cause analysis; passes `doc_linter`. | Pending |
| 27 | **Refactor role prompts** (`src/role_utils.py`, template + linter) | Programmer | QA Lead | Role registry lists slugs only; prompts stored separately; linter validates each role file. | Pending |
| 28 | **Integrate metrics scripts into workflow** (`metrics.yml`) | DevOps | Architect | `metrics.yml` runs scripts from task 6 and pushes results; CI shows success. | Pending |
| 29 | **Audit role methodology documents** (`docs/roles/*.md`) | QA Lead | Project Manager | Each role file lists at least three methodologies and passes `doc_linter`; tasks 20‑26 marked Done. | Pending |
| 30 | **Add Responsible Role field to templates** (`docs/*_TEMPLATE.md`, examples, `linters/artifact_role_linter.py`) | Architect | Systems Analyst, Programmer | Templates and examples include a `Responsible Role` section; new linter ensures presence. | Pending |
> **Progress Tracking:** Update the Status column and add ✅ in the DoD column once criteria are met.

---

*End of To‑Do list*
