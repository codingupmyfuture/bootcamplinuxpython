import os
import time
import argparse
import multiprocessing
from typing import List
import nasa.comunes.parametros as args
from nasa.negocio.generardor import Archivos
from nasa.negocio.reportes import Pandas, Python
from nasa.comunes.inicializador import Instanciador


def test_generar_archivos_pandas(capsys, argumentos_generador: List[str]):
    """permite generar archivos aleatorios y probar la generación de reportes usando el metodo pandas

    :param capsys: es una fixture en pytest que proporciona la capacidad de capturar la salida estándar (stdout) y la
    salida de error (stderr) generadas durante la ejecución de una prueba
    :type capsys: CaptureFixture
    :param argumentos_generador: lista de parametros
    :type argumentos_generador: List[str]
    """
    # simulación  de parametros y definición de rutas temporales
    parametros: argparse.ArgumentParser = None
    __basedir__: str = os.path.dirname(os.path.abspath(__file__))
    __basedir__ = f"{os.sep}".join(__basedir__.split(os.sep)[:-1])

    # se realiza un mapping de los argumentos
    with capsys.disabled():
        parametros = args.obtener_args().parse_args(argumentos_generador[1:])

    # se obtienen las instancias
    instanciador: Instanciador = Instanciador(parametros, __basedir__).obtener_instancias_configuracion()

    # se genera los archivos, al archivos.ejecutar tener un bucle infinito, debemos aplicar otra técnica
    # llamadas hilos (ejecución aislada)
    archivos = Archivos(instanciador)
    hilo = multiprocessing.Process(target=archivos.ejecutar)
    hilo.start()
    time.sleep(15)
    hilo.terminate()

    # validar si genero archivos
    assert len(os.listdir(instanciador.ruta_archivos)) > 0

    # generación de reportes usando pandas
    Pandas(instanciador).generar_reportes()
    assert len(os.listdir(instanciador.ruta_reportes)) > 0


def test_generar_archivos_python(capsys, argumentos_generador):
    """permite generar archivos aleatorios y probar la generación de reportes usando el metodo python

    :param capsys: es una fixture en pytest que proporciona la capacidad de capturar la salida estándar (stdout) y la
    salida de error (stderr) generadas durante la ejecución de una prueba
    :type capsys: CaptureFixture
    :param argumentos_generador: lista de parametros
    :type argumentos_generador: List[str]
    """
    # simulación  de parametros y definición de rutas temporales
    parametros: argparse.ArgumentParser = None
    __basedir__: str = os.path.dirname(os.path.abspath(__file__))
    __basedir__ = f"{os.sep}".join(__basedir__.split(os.sep)[:-1])

    # se realiza un mapping de los argumentos
    with capsys.disabled():
        parametros = args.obtener_args().parse_args(argumentos_generador[1:])

    # se obtienen las instancias unicas
    instanciador: Instanciador = Instanciador(parametros, __basedir__).obtener_instancias_configuracion()

    # al ser generador, llamamos la clase que realiza el proceso
    archivos = Archivos(instanciador)
    hilo = multiprocessing.Process(target=archivos.ejecutar)
    hilo.start()
    time.sleep(15)
    hilo.terminate()

    # valida que se tengan archivos
    assert len(os.listdir(instanciador.ruta_archivos)) > 0

    # se genera reportes y valida cantidad
    Python(instanciador).generar_reportes()
    assert len(os.listdir(instanciador.ruta_reportes)) > 0
