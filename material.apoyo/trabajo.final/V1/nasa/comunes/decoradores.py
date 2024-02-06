import os
import time
import pandas as pd
from typing import Any, Dict
from tabulate import tabulate
from datetime import datetime
from __meta__ import __basedir__
from nasa.comunes.utilitarios import Funcionalidades


"""
Muchas veces, las aplicaciones pueden experimentar picos de demanda, y en esos momentos críticos, su rendimiento puede
deteriorarse. Uno de los cometidos comunes de los arquitectos es optimizar la aplicación. Sin embargo, para llevar a
cabo este proceso, lo primero que se debe hacer es comprender dónde surgen los mayores problemas. Este decorador es
una introducción básica a ello, donde se puede aplicar a cualquier función o método para determinar su duración en
tiempo de ejecución y generar un archivo de auditoría.

NOTA: al ser un archivo de auditoria y uso interno, no se requiere tanta parametrización
"""


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#14, DECORADORES
class App:
    # TECDEV: SEC#2, ID#16, MANEJO DE CLASS METHOD
    @classmethod
    def tiempo_ejecucion(cls, mostrar_reporte: bool, ruta_logs: str = None):
        """permite medir el tiempo de ejecucion de una funcion y mostrar
        los resultandos en formato de tabla

        :param mostrar_reporte: para saber si muestra tiempos o no de la función ejecutada
        :type mostrar_reporte: bool
        :param ruta_logs: ruta para alacenar en carpeta especifica, defaults to None
        :type ruta_logs: str, optional
        """
        def decorador(funcion):
            def wrapper(*args, **kwargs):
                if mostrar_reporte:
                    funcionalidades = Funcionalidades()

                    # validamos que exista la carpeta interna
                    if ruta_logs is None:
                        ruta_carpeta: str = os.path.join(__basedir__, "recursos", "auditoria")
                    else:
                        ruta_carpeta: str = os.path.join(ruta_logs, "recursos", "auditoria")
                    if not os.path.exists(ruta_carpeta):
                        os.makedirs(ruta_carpeta)

                    # configurar logger
                    funcionalidades.configurar_logger(
                        "AUDITORIA",
                        os.path.join(
                            ruta_carpeta,
                            "funcion_{}_{}.log".format(funcion.__name__, datetime.now().strftime('%d%m%Y%H%M%S'))
                        )
                    )

                    # calcular inicio de tiempo
                    inicio = time.time()

                # ejecutar función
                resultado = funcion(*args, **kwargs)

                if mostrar_reporte:
                    fin = time.time()

                    # generar datos para calcular la tabla
                    datos: Dict[str, Any] = {
                        "funcion": funcion.__name__,
                        "inicio": inicio,
                        "fin": fin,
                        "duracion_seg": fin - inicio,
                    }

                    funcionalidades.LOGGER.info("*" * 100)
                    funcionalidades.LOGGER.info(f"REPORTE FUNCIÓN: {funcion.__name__}".center(100))
                    funcionalidades.LOGGER.info("*" * 100)
                    # imprimir args
                    funcionalidades.LOGGER.info("\n args: \n")
                    for arg in args:
                        funcionalidades.LOGGER.info(f"\t{arg}")

                    # imprimir kwargs
                    funcionalidades.LOGGER.info("\n kwargs: \n")
                    for kwarg in kwargs:
                        funcionalidades.LOGGER.info(f"\t{kwarg}")

                    # imprimir tablas de resultados
                    df: pd.DataFrame = pd.DataFrame(datos, index=[0])
                    funcionalidades.LOGGER.info(("\n" + tabulate(df, headers="keys", tablefmt="psql")))
                return resultado
            return wrapper
        return decorador
