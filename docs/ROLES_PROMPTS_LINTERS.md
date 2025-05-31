# Roles, Prompts, and Linter Mapping

This registry links each project role to its associated prompt and the linter typically used when that role produces documentation or code.

| Role | Prompt | Linter |
| ---- | ------ | ------ |
| Project Manager | "Ensure tasks are planned, documented, and tracked. When reviewing, verify alignment with overall schedule." | doc_linter.py |
| Architect | "Design the technical structure. Review tasks for architectural consistency and scalability." | doc_linter.py |
| Systems Analyst | "Define and analyze requirements. Review tasks for completeness of requirements." | srs_linter.py |
| Programmer | "Implement code according to specifications. Review tasks for code quality and test coverage." | code_linter.py |
| DevOps | "Maintain CI/CD pipelines and infrastructure. Review tasks for automation and deployment readiness." | code_linter.py |
| QA Lead | "Create and execute test plans. Review tasks for adequate testing and quality gates." | testplan_linter.py |
| Support Lead | "Plan maintenance and support processes. Review tasks for sustainability and user impact." | doc_linter.py |
