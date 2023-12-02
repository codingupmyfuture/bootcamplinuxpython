<img src="https://i.postimg.cc/cCjTSn8r/ss-cumf.png" alt="reporte" border="0"/>



# **CREACIÓN DE PROYECTO**


La creación de un proyecto Python se refiere al proceso de establecer la estructura inicial, configuración y archivos necesarios para iniciar un desarrollo específico en Python. Esto implica la creación de carpetas, archivos de código fuente, configuraciones de entorno y, a menudo, la gestión de dependencias.


Al construir un proyecto en Python, hay ciertos elementos fundamentales que suelen ser esenciales para un desarrollo robusto y organizado. Algunos de estos elementos clave son:

**1. Estructura de carpetas organizada**:
* **Código fuente:** Un directorio donde se almacena el código Python
* **Tests:** Una carpeta separada para pruebas unitarias o de integración
* **Documentación:** Si es posible, una sección para documentación, como docs
* **Archivos de configuración:** Para archivos de configuración específicos

**2. Entorno virtual**: Utilizar un entorno virtual (Virtualenv, Conda, etc.) para aislar las dependencias del proyecto. Esto ayuda a evitar conflictos entre diferentes proyectos que puedan requerir diferentes versiones de las mismas bibliotecas.

**3. Archivo de requerimientos (requirements.txt, pyproject.toml, etc)**: Especifica las dependencias del proyecto y sus versiones. Esto garantiza que otros desarrolladores puedan recrear exactamente el mismo entorno que tú.

**4. Gestión de dependencias**: Utilizar herramientas como Poetry, Pipenv o pip para administrar las dependencias del proyecto y facilitar su instalación en otros entornos.

**5. Documentación**: Incluir documentación legible y clara. Puedes usar herramientas como Sphinx para generar documentación a partir de docstrings.

**6. Pruebas (tests)**: Implementar pruebas unitarias y, si es posible, pruebas de integración. Estas pruebas son fundamentales para asegurar el buen funcionamiento del código y detectar errores.

**7. Control de versiones**: Utilizar un sistema de control de versiones como Git para gestionar cambios en el código y colaborar eficientemente con otros desarrolladores.

**8. Estándares de codificación**: Seguir convenciones de estilo de código, como PEP 8, para mantener consistencia y legibilidad en el código.

**9. Archivo README**: Un archivo README.md bien redactado que explique la finalidad del proyecto, cómo instalarlo, configurarlo y ejecutarlo, junto con ejemplos si es necesario.

**10. Licencia**: Incluir un archivo de licencia que especifique los términos de uso del código para cualquier persona que desee utilizarlo.


## **POETRY**

<img src="https://miro.medium.com/v2/resize:fit:640/format:webp/0*oek9uPntF7vtHJP8.png" alt="reporte" border="0"/>

Es una herramienta y administrador de dependencias para proyectos de Python. Poetry ayuda en la gestión de paquetes, entornos virtuales y dependencias de un proyecto Python. Permite definir las dependencias en un archivo pyproject.toml, manejar versiones, crear entornos virtuales, instalar y desinstalar paquetes de manera organizada.

Para trabajar con Poetry, debes asegurarte de que tu proyecto contenga el archivo `pyproject.toml` de lo contrario, podrás ver algo como:

```bash
Poetry could not find a pyproject.toml file in /your/folder
```


### DEPENDENCIAS

`Poetry` y `pip` son herramientas diferentes que gestionan las dependencias de manera distinta, aunque tienen objetivos similares: administrar las bibliotecas y paquetes necesarios para proyectos Python. Acá puedes encontrar una guía detallada:


<head>
  <meta charset="UTF-8">
  <title>Preview de página web</title>
  <style>
    /* Estilos opcionales para el iframe */
    body, html {
      margin: 0;
      padding: 0;
      height: 100%;
      overflow: hidden;
    }
    iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  </style>
</head>
<body>
  <iframe src="https://python-poetry.org/docs/dependency-specification/#caret-requirements" title="Preview de página web"></iframe>

### OTROS COMANDOS

1. crear un proyecto Poetry
```bash
poetry new proyect_name

# o
poetry new proyect_name --name alias
```


2. agregar dependencias
```bash
poetry add library [--group name] 
```


3. remover dependencias
```bash
poetry remove library 
```

4. ver librerías instaladas en Poetry
```bash
poetry show [--tree]
```

5. actualizar
```bash
poetry update
```

6. crear un archivo whl y gz
```bash
poetry build
    
# pip install file
```

7. instalar librerías
```bash 
poetry install [--with name] 

```

8. manejo de ambientes virtuales
    

    8.1 creación de ambiente
    ```bash 
    poetry env use python3.9 # o solo 3.9
    ```


    8.2 obtener info del ambiente
    ```bash 
    poetry env info 
    ```

    8.3 obtener ruta del ambiente
    ```bash 
    poetry env info --path
    ```
    
    8.4 listar los ambientes
    ```bash 
    poetry env list
    ```
    
    8.5 eliminar un ambiente
    ```bash 
    poetry env remove  python3.9 
    ```

    8.6 eliminar todos los ambientes
    ```bash 
    poetry env remove  --all
    ```

    8.7 activar ambiente
    ```bash 
    poetry shell
    ```

9. validar la configuración del archivo pyproject.toml
```bash 
poetry check
```
    
10. mostrar la configuración de Poetry
```bash 
poetry config --list
```
    
11. enviar librería a **PyPI** 
    
**PyPI** significa *Python Package Index*. Es el repositorio oficial de paquetes de software de Python. Funciona como un almacén centralizado donde los desarrolladores pueden publicar sus paquetes de Python de código abierto para que otros puedan instalarlos y utilizarlos en sus propios proyectos.
    
Para ver como hacerlo, puede seguir este [link](https://www.digitalocean.com/community/tutorials/how-to-publish-python-packages-to-pypi-using-poetry-on-ubuntu-22-04)

Hacer los pasos del link, después
    
```bash 
poetry push
```

    
12. Atributos adicionales para **pyproject.toml**

```bash
license = "MIT"
homepage = "https://ejemplo.com"
repository = "https://github.com/usuario/repo"
documentation = "https://ejemplo.com/docs"
keywords = ["python", "ejemplo", "proyecto"]
    
```
Nota: [info liencias](https://aprendeinformaticas.com/que-son-las-licencias-de-software/)
    


## **TIPS TRABAJO FINAL**
    
1. El proyecto debe contar con una estructura definida para pruebas, configuración y código
2. Debe contar con un correcto manejo de versionamiento para el producto, así como información del desarrollador, licencia, etc.