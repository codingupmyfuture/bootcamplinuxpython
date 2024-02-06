import argparse
from typing import List
import nasa.comunes.parametros as args


def test_argumentos_generador(capsys, argumentos_generador: List[str]):
    """función para probar los argumentos de generador de archivos aleatorios

    :param capsys: es una fixture en pytest que proporciona la capacidad de capturar la salida estándar (stdout) y la
    salida de error (stderr) generadas durante la ejecución de una prueba
    :type capsys: capsys
    :param argumentos_generador: lista de argumentos asignado la opción
    :type argumentos_generador: List[str]
    """
    parametros: argparse.ArgumentParser = None
    with capsys.disabled():
        # llama a la función con argumentos simulados, y le envio los elementos simulados
        # se omite el nombre del archivo
        parametros = args.obtener_args().parse_args(argumentos_generador[1:])

    assert parametros.command == "generador"
    assert parametros.periodicidad == 5


def test_argumentos_reporte_pandas(capsys, argumentos_reporte_pandas: List[str]):
    """función para probar los argumentos de reportes usando pandas

    :param capsys: es una fixture en pytest que proporciona la capacidad de capturar la salida estándar (stdout) y la
    salida de error (stderr) generadas durante la ejecución de una prueba
    :type capsys: _type_
    :param argumentos_reporte_pandas: lista de argumentos asignado la opción
    :type argumentos_reporte_pandas: List[str]
    """
    parametros: argparse.ArgumentParser = None
    with capsys.disabled():
        # llama a la función con argumentos simulados, y le envio los elementos simulados
        # se omite el nombre del archivo
        parametros = args.obtener_args().parse_args(argumentos_reporte_pandas[1:])

    assert parametros.command == "reporteador"
    assert parametros.metodo == "pandas"


def test_argumentos_reporte_python(capsys, argumentos_reporte_python: List[str]):
    """función para probar los argumentos de reportes usando python

    :param capsys: es una fixture en pytest que proporciona la capacidad de capturar la salida estándar (stdout) y la
    salida de error (stderr) generadas durante la ejecución de una prueba
    :type capsys: _type_
    :param argumentos_reporte_python: lista de argumentos asignado la opción
    :type argumentos_reporte_python: List[str]
    """
    parametros: argparse.ArgumentParser = None
    with capsys.disabled():
        # llama a la función con argumentos simulados, y le envio los elementos simulados
        # se omite el nombre del archivo
        parametros = args.obtener_args().parse_args(argumentos_reporte_python[1:])

    assert parametros.command == "reporteador"
    assert parametros.metodo == "python"


def test_sin_argumentos():
    """función para validar cuando no se envia un parámetro
    """
    parametros: argparse.ArgumentParser = None
    parametros = args.obtener_args().parse_args([])
    assert parametros.command is None
