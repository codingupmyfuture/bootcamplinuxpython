<img src="https://i.postimg.cc/cCjTSn8r/ss-cumf.png" alt="reporte" border="0"/>


# **PYTEST**

PyTest es un marco de trabajo que permite realizar pruebas unitarias para un software en Python.

Documentación oficial:
https://docs.pytest.org/en/7.4.x/

## **ACCIONES ELEMENTRALES**

### **1. CONDIFURACIÓN**
1. installar la librería:
```
# usando pip
pip install pytest
pip install pytest-cov

# usando poetry
poetry add pytest [--group nombre]
poetry add pytest-cov [--group nombre]
```

2. Dentro de la carpeta principal del proyecto, usar o crear el archivo de configuración `setup.cfg`, y agregar esta sección:

```
[tool:pytest]
addopts = --doctest-modules tests 
    --cov-config .coveragerc 
    --cov-report term-missing 
    --cov-report html 
    --cov ruta_proyecto/
    --cov-fail-under 60
python_files = tests/*/*.py
filterwarnings =
    ignore::FutureWarning
```

**Glosario**:


* `addopts`: se utiliza para pasar opciones de línea de comandos adicionales a pytest a través del archivo de configuración .

* `python_files`: e utiliza para especificar un patrón de búsqueda que define qué archivos deben ser considerados como archivos de código fuente de Python durante la ejecución de las pruebas. 

* `filterwarnings`: se utiliza para especificar una lista de filtros que controlan cómo pytest maneja las advertencias durante la ejecución de las pruebas.

Lista completa de comandos:
https://docs.pytest.org/en/7.4.x/reference/reference.html#confval-python_files

### **3. COMANDOS**

Para realizar la validación de código:

```bash
# nota deben estar ubicados en la raiz donde esta la carpeta test y el archivo setp.cfg
python -m pytest -v
```



### **4. TERMINOS ADICIONALES**

* `mock data`: se refiere a datos simulados o ficticios que se utilizan en lugar de datos reales durante la ejecución de las pruebas

* ` conftest.py`: Es un archivo especial que se utiliza para compartir configuraciones, fixtures y plugins entre diferentes pruebas o módulos de prueba dentro de un proyecto. 

IMPORTANTE: todos las funciones que se realicen para probar dentro de la carpeta test, todas
deben empezar con la palabra `test_`