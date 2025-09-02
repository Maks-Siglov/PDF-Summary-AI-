.PHONY: lint, run, test

lint:
	@echo "Running linters..."
	poetry run black .
	poetry run isort .
	poetry run flake8 src/ tests/

run:
	@echo "Running application..."
	poetry run sh entrypoints/prod_entrypoint.sh

test:
	@echo "Running tests..."
	poetry run pytest .