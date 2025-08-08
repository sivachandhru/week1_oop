# Week 1 — Python OOP + Testing

![tests](https://github.com/sivachandhru/week1_oop/actions/workflows/python.yml/badge.svg)

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest pytest-cov mypy
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q -p pytest_cov --cov=. --cov-report=term-missing
mypy bank.py shapes.py

git tag week1-complete
git push origin week1-complete

