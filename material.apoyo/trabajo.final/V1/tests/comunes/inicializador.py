import os
import argparse
from typing import List
import nasa.comunes.parametros as args
from nasa.comunes.inicializador import Instanciador
from nasa.comunes.utilitarios import Funcionalidades, Struct
from nasa.comunes.constantes import ValoresConstantesNoHarcodeados


def test_obtener_instancias_configuracion(capsys, argumentos_generador: List[str]):
    """función para validar la clase de objetos transversales

    :param capsys: es una fixture en pytest que proporciona la capacidad de capturar la salida estándar (stdout) y la
    salida de error (stderr) generadas durante la ejecución de una prueba
    :type capsys: capsys
    :param argumentos_generador: lista de argumentos asignado la opción
    :type argumentos_generador: List[str]
    """
    # definición de rutas temporales
    parametros: argparse.ArgumentParser = None
    __basedir__: str = os.path.dirname(os.path.abspath(__file__))
    __basedir__ = f"{os.sep}".join(__basedir__.split(os.sep)[:-1])

    # mapeo de parámetros
    with capsys.disabled():
        parametros = args.obtener_args().parse_args(argumentos_generador[1:])

    # se crea el objeto de instancias
    instanciador: Instanciador = Instanciador(parametros, __basedir__).obtener_instancias_configuracion()

    # validacion de tipos
    assert isinstance(instanciador.utilitarios, Funcionalidades)
    assert instanciador.args is not None
    assert isinstance(instanciador.config, Struct)
    assert isinstance(instanciador.mensajes, Struct)
    assert isinstance(instanciador.ruta_archivos, str)
    assert isinstance(instanciador.ruta_respaldo, str)
    assert isinstance(instanciador.ruta_reportes, str)
    assert isinstance(instanciador.constante, ValoresConstantesNoHarcodeados)

    error: bool = False
    try:
        Instanciador(parametros, "xyx").obtener_instancias_configuracion()
    except Exception:
        error = True

    assert error is True
