<img src="https://i.postimg.cc/cCjTSn8r/ss-cumf.png" alt="reporte" border="0"/>


# **FLAKE8**

Flake8 es una librería Python que incluye PyFlakes, Pycodestyle y Ned Batchelder's McCabe script. Es un gran kit de herramientas para comprobar su código base contra el estilo de codificación (PEP8), errores de programación como `library imported but unused`, `Undefined name` y código que no está indentado.

Documentación oficial:
https://flake8.pycqa.org/en/latest/

## **ACCIONES ELEMENTRALES**

### **1. CONDIFURACIÓN**
1. installar la librería:
```
# usando pip
pip install flake8

# usando poetry
poetry add flake8 [--group nombre]
```

2. Dentro de la carpeta principal del proyecto, usar o crear el archivo de configuración `setup.cfg`, y agregar esta sección:

```
[flake8]
ignore = 
max-line-length = 120
max-complexity = 10
```

**Glosario**:


* `ignore`: se utiliza para especificar códigos de errores específicos que se deben ignorar durante la verificación del estilo del código.

* `max-line-length`: se refiere a una regla de estilo que controla la longitud máxima de una línea de código en un archivo fuente. 

* `max-complexity`: regla que establece un límite en la complejidad ciclomática permitida para las funciones o métodos en el código fuente.

Lista completa de comandos:
https://flake8.pycqa.org/en/latest/user/options.html

### **3. COMANDOS**

Para realizar la validación de código:

```bash
flake8 ruta_proyecto
```