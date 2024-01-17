

.PHONY: clean lint mypy lint dist

clean: clean-envs clean-pyc clean-test clean-dist

clean-envs:
	rm -rf env

clean-pyc:
	find . -name '*.pyc' -exec rm -fr {} +
	find . -name '*.pyo' -exec rm -fr {} +
	find . -name '*~' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +	 

clean-mypy:
	find . -name '.mypy_cache' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -rf .tox .coverage htmlcov coverage-reports tests.xml tests.html
	rm -rf .coverage.*
	rm -rf .pytest_cache
	rm -rf .mypy_cache

clean-dist: ## remove binary files
	find . -name 'dist' -exec rm -fr {} +

lint:

	flake8 calidad

test: ## Install and run tests
	python -m pytest -v

