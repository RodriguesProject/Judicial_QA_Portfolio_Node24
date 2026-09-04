# Judicial Information System — QA Engineering Portfolio

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688)
![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC)
![Status](https://img.shields.io/badge/QA%20Portfolio-Ready-brightgreen)

**Candidate:** Thiago Rodrigues  
**Repository:** RodriguesProject  
**Portfolio project:** Judicial Information System — Quality Assurance

> **Portfolio / academic project:** this repository is a fictional simulation created to demonstrate hands-on QA capabilities. It is not professional experience for UNDP, CNJ, any court, government institution, or real client.

## 2-minute recruiter overview

This project demonstrates a complete, traceable QA workflow for a fictional judicial information system, from requirements and risk analysis to manual test design, API testing, security/access-control testing, regression, end-to-end validation, automated tests and CI.

| Capability | Evidence | What to look at |
|---|---|---|
| Requirements analysis | Requirements + acceptance criteria | `docs/01_requirements.md` |
| Test planning | Test plan / strategy | `docs/02_test_plan.md`, `docs/09_portfolio_test_strategy.md` |
| Test design | Scenarios + test cases | `docs/03_test_scenarios.md`, `test-data/test-cases.csv` |
| Functional QA | Positive/negative validation | `tests/test_functional.py` |
| Integration QA | API/workflow integration | `tests/test_integration.py` |
| E2E testing | Judicial case workflow | `tests/test_e2e.py` |
| Security QA | Authorization / restricted actions | `tests/test_security.py`, `docs/06_risk_matrix.md` |
| Regression | Repeatable regression suite | `tests/test_regression.py`, `docs/07_regression_strategy.md` |
| Automation | Pytest suite | `tests/` |
| API | FastAPI application | `app/main.py` |
| CI/CD | Automated GitHub workflow | `.github/workflows/qa.yml` |
| Test reporting | Execution evidence + summary | `reports/` |
| Performance check | Lightweight local load check | `scripts/performance_check.py` |

## Current validation result

**Latest local run:**

```text
10 tests passed
0 tests failed
100% pass rate
```

Lightweight local performance check:

```text
100 requests
Average: 0.845 ms
Minimum: 0.633 ms
Maximum: 1.439 ms
```

These figures are local portfolio evidence only; they are not production benchmarks.

## Technical stack

- Python
- FastAPI
- Pytest
- HTTPX
- REST API concepts
- GitHub Actions
- Markdown / CSV test artifacts

## QA approach

The project uses a risk-based and traceable approach:

1. Define requirements and acceptance criteria.
2. Identify quality and security risks.
3. Design scenarios and test cases.
4. Prepare representative test data.
5. Validate functional, integration, E2E, regression and authorization behavior.
6. Automate repeatable checks with Pytest.
7. Execute the suite through GitHub Actions.
8. Record evidence, defects and residual risks.
9. Produce a test summary and release recommendation.

## Quick start

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run automated tests:

```bash
pytest -q
```

Run the API locally:

```bash
python -m uvicorn app.main:app --reload
```

Then open:

`http://127.0.0.1:8000/docs`

Run the lightweight performance check:

```bash
python scripts/performance_check.py
```

## Repository navigation

```text
RodriguesProject/
│
├── README.md
├── LICENSE
├── SECURITY.md
├── .gitignore
├── requirements.txt
├── pytest.ini
│
├── app/
│   └── main.py
│
├── tests/
│   ├── test_functional.py
│   ├── test_integration.py
│   ├── test_security.py
│   ├── test_e2e.py
│   └── test_regression.py
│
├── docs/
│   ├── 01_requirements.md
│   ├── 02_test_plan.md
│   ├── 03_test_scenarios.md
│   ├── 06_risk_matrix.md
│   ├── 07_regression_strategy.md
│   ├── 08_defect_report_template.md
│   ├── 09_portfolio_test_strategy.md
│   ├── 10_tdd_workflow.md
│   ├── 11_github_profile.md
│   └── 12_recruiter_walkthrough.md
│
├── test-data/
│   ├── test-cases.csv
│   └── test-data.csv
│
├── reports/
├── scripts/
└── .github/workflows/
    └── qa.yml
```

## Integrity and scope

No real judicial data, credentials, personal information, production infrastructure or UNDP/CNJ system components are used. The domain is fictional and exists only to demonstrate QA engineering practices.

## Recruiter walkthrough

For a fast review, start with:

1. This `README.md`.
2. `docs/01_requirements.md` — requirements and acceptance criteria.
3. `docs/02_test_plan.md` — test planning.
4. `test-data/test-cases.csv` — concrete test design.
5. `tests/` — executable automation.
6. `docs/06_risk_matrix.md` — risk-based quality thinking.
7. `reports/test-summary-report.md` — reporting and release view.
8. `.github/workflows/qa.yml` — CI execution.

## Why this domain was selected

The fictional judicial context allows the portfolio to demonstrate quality concerns that matter in information systems: data integrity, traceability, controlled access, auditability, process correctness and risk management. It also reflects the candidate's professional domain knowledge without presenting the project as experience with a real institution.

## CI/CD compatibility
The workflow uses current Node.js 24-compatible official GitHub Actions versions for checkout and Python setup.
