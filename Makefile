# ==============================================================================
# Makefile for Project Automation
#
# Provides a unified interface for common development tasks, such as running
# the application, formatting code, and running tests.
#
# Inspired by the self-documenting Makefile pattern.
# See: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
# ==============================================================================

# Default target when 'make' is run without arguments
.DEFAULT_GOAL := help

# Specify the Python executable and main app file name
PYTHON := ./.venv/bin/python
APP_FILE := ./src/main.py

# ==============================================================================
# HELP
# ==============================================================================

.PHONY: help
help: ## Show this help message
	@echo "Usage: make [target] [VAR=value]"
	@echo "Options:"
	@echo "  \033[36m%-15s\033[0m %s" "SUDO=true" "Run docker commands with sudo (e.g., make up SUDO=true)"
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ==============================================================================
# ENVIRONMENT SETUP
# ==============================================================================

.PHONY: setup
setup: ## Project initial setup: install dependencies
	@echo "🐍 Installing python dependencies with uv..."
	@uv sync


# ==============================================================================
# APPLICATION
# ==============================================================================

.PHONY: run
run: ## Launch the Textual application
	@echo "🚀 Starting Textual app..."
	@PYTHONPATH=. $(PYTHON) $(APP_FILE)

# ==============================================================================
# CODE QUALITY
# ==============================================================================

.PHONY: format
format: ## Automatically format code using Black and Ruff
	@echo "🎨 Formatting code with black and ruff..."
	@black .
	@ruff check . --fix

.PHONY: lint
lint: ## Perform static code analysis (check) using Black and Ruff
	@echo "🔬 Linting code with black and ruff..."
	@black --check .
	@ruff check .

# ==============================================================================
# TESTING
# ==============================================================================

.PHONY: test
test: ui-test e2e-test ## Run the full test suite

.PHONY: ui-test
ui-test: ## Run UI tests
	@echo "Running UI tests..."
	@$(PYTHON) -m pytest tests/ui -s

.PHONY: e2e-test
e2e-test: ## Run end-to-end tests
	@echo "Running end-to-end tests..."
	@$(PYTHON) -m pytest tests/e2e -s

# ==============================================================================
# CLEANUP
# ==============================================================================

.PHONY: clean
clean: ## Remove __pycache__ and .venv to make project lightweight
	@echo "🧹 Cleaning up project..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@rm -rf .venv
	@rm -rf .pytest_cache
	@rm -rf .ruff_cache
	@echo "✅ Cleanup completed"