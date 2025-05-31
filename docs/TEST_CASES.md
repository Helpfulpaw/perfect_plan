# Test Cases

## TC-1 Verify documentation templates exist
**Related Requirement:** REQ-1
1. Navigate to the `docs/` directory.
2. Confirm template files such as `TESTPLAN_TEMPLATE.md` are present.
**Expected Result:** Templates exist and contain section headings only.

## TC-2 Validate linters detect to-do markers
**Related Requirement:** REQ-2
1. Create a sample file containing the text `to-do`.
2. Run `python linters/doc_linter.py <file>`.
**Expected Result:** Linter exits with a non-zero status and reports the to-do marker.

## TC-3 Ensure example artifacts pass linters
**Related Requirement:** REQ-3
1. Run `doc_linter` on example documentation under `docs`.
2. Run `testplan_linter` on `docs/TEST_PLAN.md`.
**Expected Result:** All linters complete successfully with return code 0.
