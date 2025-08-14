
# Software Testing 2025 (Advanced)

This repository implements **three experiments** ready for your NUAA assignment:

1) **Service Unit Testing** (Python): REST API tests (contract, boundary, negative, property-based) + local module unit tests  
2) **Web Test Automation** (Selenium, Page Object Model, data-driven, explicit waits, auto-screenshots)  
3) **Continuous Integration** (GitHub Actions) + **Java** project with **Jacoco** coverage and **SpotBugs** static analysis

> Push this repo to GitHub and the Actions pipeline will automatically run tests and upload **Artifacts** (pytest HTML, coverage reports, screenshots, surefire, jacoco, spotbugs, built JAR).

## Local quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run all Python tests (API + local + Selenium) with coverage & HTML report
pytest -q   --html=artifacts/pytest_report.html --self-contained-html   --junitxml=artifacts/pytest_junit.xml   --cov=app --cov=unit_test --cov=web_test   --cov-report=xml:artifacts/coverage.xml   --cov-report=html:artifacts/htmlcov
```
