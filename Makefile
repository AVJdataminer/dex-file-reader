# Makefile for DEX File Reader Package

.PHONY: help install install-dev install-notebook install-full clean build test test-package publish clean-build clean-pyc clean-test clean-venv

help: ## Show this help message
	@echo "DEX File Reader Package - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package in development mode
	pip install -e .

install-dev: ## Install the package with development dependencies
	pip install -e ".[dev]"

install-notebook: ## Install the package with notebook dependencies
	pip install -e ".[notebook]"

install-full: ## Install the package with all dependencies
	pip install -e ".[full]"

clean: clean-build clean-pyc clean-test clean-venv ## Remove all build, test, cache and Python artifacts

clean-build: ## Remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/

clean-pyc: ## Remove Python file artifacts
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete
	find . -name '__pycache__' -type d -exec rm -rf {} +

clean-test: ## Remove test and coverage artifacts
	rm -rf .tox/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/

clean-venv: ## Remove virtual environment
	rm -rf venv/

build: ## Build source and wheel distributions
	python -m build

test: ## Run tests quickly with the default Python
	python -m pytest

test-package: ## Test the package structure and imports
	python test_package.py

lint: ## Check code style with flake8
	flake8 dex_reader tests

format: ## Format code with black
	black dex_reader tests

type-check: ## Run type checking with mypy
	mypy dex_reader

check: lint type-check test ## Run all checks (lint, type-check, test)

publish: ## Package and upload a release
	python -m build
	python -m twine upload dist/*

# Development setup
setup-dev: ## Set up development environment
	python -m venv venv
	. venv/bin/activate && pip install --upgrade pip setuptools wheel
	. venv/bin/activate && make install-dev

# Documentation
docs: ## Generate documentation
	python setup.py build_sphinx

# Jupyter notebook setup
setup-notebook: ## Set up Jupyter notebook environment
	python setup_notebook.py

# Quick start
quickstart: ## Quick start - install and test
	make install
	make test-package
	@echo "✅ Package is ready to use!"
	@echo "   Try: python -c \"from dex_reader import DEXReader; print('Success!')\""
