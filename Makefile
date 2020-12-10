tests:
	make styles_check
	pytest -s
	python -m doctest README.md

clean:
	find . -name "*.pyc" -delete

styles:
	black .
	isort --ws .
	flake8

styles_check:
	black . --check
	isort --ws --check-only .
	flake8
