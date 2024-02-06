import pytest
from typing import List


"""CONFTEST
conftest.py en pytest es un archivo especial utilizado para configurar y compartir recursos entre varios archivos de
prueba. Este archivo puede contener funciones y definiciones de configuración que se aplicarán a los casos de prueba
dentro de un directorio y sus subdirectorios.

@pytest.fixture(scope="session") es un decorador en pytest utilizado para definir una fixture con un alcance de sesión.
Una fixture en pytest es una forma de proporcionar datos, recursos o configuraciones a las pruebas de manera organizada
y reutilizable.

La opción scope="session" indica que la fixture debe tener un alcance de sesión, lo que significa que se creará y se
ejecutará una vez para toda la sesión de prueba.
"""


@pytest.fixture(scope="session")
def argumentos_generador() -> List[str]:
    """genera datos de sesión simulandos los argumentos enviados para generar archivos temporales

    :return: lista de argumentos
    :rtype: List[str]
    """
    argumentos: List[str] = ['apolo-11.py', 'generador', '--periodicidad', '5']
    return argumentos


@pytest.fixture(scope="session")
def argumentos_reporte_pandas() -> List[str]:
    """genera datos de sesión simulandos los argumentos enviados para generar reportes
    usando pandas

    :return: lista de argumentos
    :rtype: List[str]
    """
    argumentos: List[str] = ['apolo-11.py', 'reporteador', '--metodo', 'pandas']
    return argumentos


@pytest.fixture(scope="session")
def argumentos_reporte_python() -> List[str]:
    """genera datos de sesión simulandos los argumentos enviados para generar reportes
    usando python

    :return: lista de argumentos
    :rtype: List[str]
    """
    argumentos: List[str] = ['apolo-11.py', 'reporteador', '--metodo', 'python']
    return argumentos
