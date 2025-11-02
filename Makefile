.PHONY: install lint test run

install:
	pip install -r requirements.txt

lint:
	ruff check .

test:
	python -m pytest -v

run:
	uvicorn app.main:app --reload
