.PHONY: init, check
init:
		alembic init migrations

check:
		black . --line-length 120
		isort .
		flake8 .