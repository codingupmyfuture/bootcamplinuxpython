import sys
import argparse
from datetime import datetime as dt
from nasa.comunes.utilitarios import Funcionalidades
"""
Este módulo está definido de forma procedural, donde se establece el encabezado que contendrá el menú, así como los
diversos parámetros que tendrá la aplicación.
"""


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#3, ID#24, MANEJO DE PARSEARGS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
def obtener_args() -> argparse.ArgumentParser:
    """funcion para obtener los parametros de entrada de la aplicación
    esto permitira segmentar los modulos del trabajo.

    :return: retorna el objeto con los parametros requeridos
    :rtype: argparse.ArgumentParser
    """

    # crea opciones de la aplicación, header
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog=f'\npython {sys.argv[0]} [opciones]',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="© todos los derechos reservados {}.".format(dt.now().year),
        add_help=True,
        usage='%(prog)s [opciones]',
        conflict_handler='resolve',
        description='''\
Herramienta para realizarla generación de mock data y cálculo de
reportes; ejemplo de solución para el trababo final de python lvl4:
--------------------------------------------------------------

    - generador
    - reporteador
'''
    )
    # permite modularizar, y asignar la variable donde va a recibir el módulo: generador o reporteador
    # mirar parametros.command en apolo-11.py
    subparsers = parser.add_subparsers(
        title="[app-opciones]",
        dest="command",
        help='sub-command help'
    )
    # crear su subparcer para el generador de archivos
    generador = subparsers.add_parser(
        "generador",
        help="herramienta para generar archivos aleatorios"
    )

    # DOCDEV: PAG#3,4, periodicidad
    # se realiza por medio de parametros, por si el valor cambia, no tener que modificar los archivos de config
    # simplemente se cambia el comando de ejecución y sale
    generador.add_argument(
        '--periodicidad',
        type=Funcionalidades.numeros_positivos,
        required=True,
        help="frecuencia de generación"
    )

    # crear su subparcer para los reportes
    reportes = subparsers.add_parser(
        "reporteador",
        help="herramienta para generar reportes, a partir de losarchivos aleatorios"
    )
    # indica si se generan los reportes con pandas o python puro
    reportes.add_argument(
        '--metodo',
        type=str,
        choices=["pandas", "python"],
        required=True,
        help="metodo de generación de los reportes"
    )

    # valida si la cantidad de argumentos es menor a 1, inmediatamente lanza el menú de ayuda
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit()
    return parser
