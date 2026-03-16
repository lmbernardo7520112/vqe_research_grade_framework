.PHONY: install dev-install test lint format clean help

install:
	pip install .

dev-install:
	pip install -e ".[dev]"

test:
	pytest tests/

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf build/ dist/

help:
	@echo "Available commands:"
	@echo "  install      - Install the package"
	@echo "  dev-install  - Install in editable mode with dev dependencies"
	@echo "  test         - Run tests"
	@echo "  lint         - Check code style and types"
	@echo "  format       - Format code using Black and isort"
	@echo "  clean        - Remove build artifacts and caches"
