test:
	make styles_check
	pytest -s
	python -m doctest README.md

clean:
	find . -name "*.pyc" -delete

styles:
	isort --ws .
	black .
	ruff check --fix .

styles_check:
	isort --ws --check-only .
	black . --check
	ruff check .
