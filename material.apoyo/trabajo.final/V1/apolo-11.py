import sys
import argparse
import traceback
from __meta__ import __basedir__
import nasa.comunes.parametros as args
from nasa.negocio.generardor import Archivos
from nasa.negocio.reportes import Pandas, Python
from nasa.comunes.excepcion import NasaAppException
from nasa.comunes.inicializador import Instanciador
from nasa.comunes.constantes import ValoresConstantesNoHarcodeados


# TECDEV: SEC#3, ID#18, MANEJO DE ENTRY POINT
# DOCDEV: PAG#4, nombre del programa (entry point)
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
class App:
    """Un "entry point" en programación es el punto de inicio de la ejecución de un programa.
    Es esencial para controlar la configuración inicial, manejar excepciones y dirigir la lógica principal del programa.
    Proporciona un punto centralizado y estructurado para comenzar la ejecución.

    Para mas información mirar: documentacion/diagramas/000.entry.point.png
    """
    print(sys.argv)
    if __name__ == "__main__":
        instanciador: Instanciador = None
        try:
            valoresConstantesNoHarcodeados = ValoresConstantesNoHarcodeados()
            # TECDEV: SEC#3, ID#24, MANEJO DE PARSEARGS
            # capturo los parametros de la app, mirar nasa.comunes.parametros
            parametros: argparse.ArgumentParser = args.obtener_args().parse_args()

            # objeto unico con las instancias de las clases comunes
            instanciador: Instanciador = Instanciador(parametros, __basedir__).obtener_instancias_configuracion()

            # cuando ejecutamos el programa, command almacena la opción del módulo
            # generar archivos
            if parametros.command == valoresConstantesNoHarcodeados.GENERADOR:
                # al ser generador, llamamos la clase que realiza el proceso
                archivos = Archivos(instanciador)
                archivos.ejecutar()

            # generar reportes
            elif parametros.command == valoresConstantesNoHarcodeados.REPORTES:
                # para los reportes, agregue dos modos, usando pandas o python sin librerias externas.
                if parametros.metodo == valoresConstantesNoHarcodeados.PANADAS:
                    Pandas(instanciador).generar_reportes()
                elif parametros.metodo == valoresConstantesNoHarcodeados.PYTHON:
                    Python(instanciador).generar_reportes()
        except Exception as ex:
            """esta es conocida como un control de excepción principal y normalmente van en los entry-points
            se utiliza para controlar cualquier fallo a nivel de la app, y pueda quedar registrado. No importa
            el nivel de donde ocurra.
            """
            nasaAppException: NasaAppException = NasaAppException(
                codigo_error=100,
                mensaje=str(ex) + "\n" + traceback.format_exc(),
                sys_info=sys.exc_info()
            )
            if instanciador is not None:
                instanciador.utilitarios.LOGGER.error(nasaAppException)
                instanciador.utilitarios.LOGGER.error(nasaAppException._error["excepcion"])
            else:
                print(nasaAppException)
                print(nasaAppException._error["excepcion"])
            sys.exit(1)
