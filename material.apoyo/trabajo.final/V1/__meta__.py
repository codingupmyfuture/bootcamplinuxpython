import os
from datetime import datetime

"""__meta__

La elección del nombre __meta__.py es una convención que algunos desarrolladores usan para almacenar metadatos
relacionados con el paquete o módulo. Los metadatos podrían incluir información como la versión del paquete, el autor,
la licencia, o cualquier otra información relevante para el proyecto.
"""

"""RUTAS MULTI OS

Para garantizar que un programa pueda ser soportado de manera multiplataforma, es indispensable que, si se requiere
manejar rutas u otros elementos internos del programa, estos estén parametrizados. Hay muchas formas de hacerlo, pero
para resumirlas se presentan dos opciones principales:

1. Archivos de configuración.
3. Librerías.

Siempre es más recomendable usar bibliotecas, ya que calculan todo de manera dinámica, mientras que hacerlo a través de
archivos de configuración obliga al usuario a realizar esta tarea. La variable __basedir__ muestra un ejemplo de cómo
recuperar la ruta de manera elemental pero eficiente, adaptándose dinámicamente según la ubicación del proyecto.
Esto significa que el proyecto se puede mover a cualquier ruta o instalar en otra máquina, y se ajustará dinámicamente
"""

# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#3, ID#20, MANEJO DE RUTAS MULTI OS
__app__: str = "NASA"
__basedir__: str = os.path.dirname(os.path.abspath(__file__))
__empresa__: str = "Softserve"
__desarrollador__: str = "Luis Vasquez"
__copyright__: str = f"© Empresa: {__empresa__}, \
generado por: {__desarrollador__}. Todos los derechos reservados {datetime.now().year}."
