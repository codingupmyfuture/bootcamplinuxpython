# Makefile es un archivo de configuración utilizado en sistemas Unix y otros, junto con la herramienta make,
# para automatizar la compilación y construcción de programas a partir de su código fuente. Contiene reglas
# que especifican cómo se deben construir los objetivos del proyecto y sus dependencias. 

# ejecutar sobre linux o mac
.PHONY: clean lint mypy lint dist

clean: clean-envs clean-pyc clean-test clean-dist clean-data

clean-data:
	rm -rf recursos > /dev/null

clean-envs:
	rm -rf env

clean-pyc: # remueve archivos temporales  de python
	find . -name '*.pyc' -exec rm -fr {} +
	find . -name '*.pyo' -exec rm -fr {} +
	find . -name '*~' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +	 

clean-mypy:
	find . -name '.mypy_cache' -exec rm -fr {} +

clean-test: # remueve los archivos generados por los coverage de pytest
	rm -rf .tox .coverage htmlcov coverage-reports tests.xml tests.html
	rm -rf .coverage.*
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf "$(pwd)tests/recursos" > /dev/null

clean-dist: # remueve cuando se crean compilados
	find . -name 'dist' -exec rm -fr {} +

# TECDEV: SEC#4, ID#29, FLAKE8
lint: # ejecuta flake8 a las pruebas y proyecto en general
	flake8 nasa
	flake8 tests

# TECDEV: SEC#4, ID#28, PRUEBAS UNITARIAS
test: clean-test # ejecuta las pruebas unitarias
	python -m pytest -v
