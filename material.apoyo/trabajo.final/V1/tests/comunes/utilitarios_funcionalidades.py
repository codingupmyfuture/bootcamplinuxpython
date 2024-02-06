import os
from datetime import datetime
from typing import Dict
from nasa.comunes.utilitarios import Funcionalidades

# defino una variable para obtener una unica instancia de fecha para todas las pruebas
fecha_unica: str = datetime.now().strftime('%d%m%Y%H%M%S')


def test_configurar_logger():
    """función para probar la configuración de loggin
    """
    funcionalidades: Funcionalidades = Funcionalidades()

    # configurar logger
    funcionalidades.configurar_logger(
        "app-test",
        os.path.join("/tmp", "log_{}.log".format(fecha_unica))
    )
    assert funcionalidades.LOGGER is not None


def test_escribir_yaml():
    """función para probar la escritura en yaml
    """
    datos: Dict[str, str] = {"demmo": "python"}
    error: bool = False
    try:
        Funcionalidades.escribir_yaml(datos, "/tmp/config_{}.yaml".format(fecha_unica))
    except Exception as ex:
        print(ex)
        error = True

    assert error is False


def test_leer_yaml():
    """función para probar la lectura en yaml
    """
    assert Funcionalidades.leer_yaml("/tmp/config_{}.yaml".format(fecha_unica)) is not None
    assert Funcionalidades.leer_yaml("/tmp/aaaaconfig_{}.yaml".format(fecha_unica)) is None


def test_obtener_encabezado():
    """función para probar generación de encabezado
    """
    logo: str = "TEST TEST TEST\n {} FECHA : {} APP  : {}"
    encabezado: str = Funcionalidades.obtener_encabezado(logo, "test")
    assert len(encabezado) > 50


def test_numeros_positivos():
    """función para probar números enteros a partir de texto
    """
    error: bool = False
    assert Funcionalidades.numeros_positivos("1") == 1

    try:
        Funcionalidades.numeros_positivos("a")
    except Exception:
        error = True

    assert error is True
