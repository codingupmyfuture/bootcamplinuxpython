import pandas as pd
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from nasa.modelamiento.propiedades.instancias import ObjetoTransversal


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#8, ABSTRACCIÓN
class Misiones(ABC):
    """Esta abstracción permite definir los metodos que debe tener la generación de
    reportes, ya sea usando pandas o python (sin libs).

    :param AccionesDirectorios: clase heredada con los metodos
    :type AccionesDirectorios: AccionesDirectorios
    """

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self, objetoTransversal: ObjetoTransversal):
        """constructor de la clase

        :param objetoTransversal: objeto que tiene las instancias principales del programa
        :type objetoTransversal: ObjetoTransversal
        """
        pass

    @abstractmethod
    def _preparar_nombre_carpeta(self, ruta: str, ciclo: int = 0) -> str:
        """Este metodo esta definido en AccionesDirectorios, pero acá se
        da un comportamiento diferente para adecuarlo al nombre de los archivos

        :param ruta: ruta principal
        :type ruta: str
        :param ciclo: nro de ciclo para agregar a la carpeta, defaults to 0
        :type ciclo: int, optional
        :return: ruta final para ser creada
        :rtype: str
        """
        pass

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    @abstractmethod
    def _obtener_info_archivos(self, ruta_archivos: str) -> List[Dict[str, Any]]:
        """Permite obtener la información de cada uno de los archivos generados asociados al ciclo

        :param ruta_archivos: ruta del ciclo
        :type ruta_archivos: str
        :return: lista con la información de cada ciclo
        :rtype: List[Dict[str, Any]]
        """
        pass

    @abstractmethod
    def _generar_analisis_eventos(self, df: pd.DataFrame, ruta_reporte: str, ciclo: str, reporte: str) -> None:
        """Generación del reporte de analisis de eventos

        :param df: datos consolidados para calcular el reporte
        :type df: pd.DataFrame
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        """
        pass

    @abstractmethod
    def _generar_desconexiones(self, df: pd.DataFrame, ruta_reporte: str, ciclo: str, reporte: str) -> None:
        """Generación del reporte de dispositivos de desconexiones

        :param df: datos consolidados para calcular el reporte
        :type df: pd.DataFrame
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        """
        pass

    @abstractmethod
    def _generar_dispositivos_inoperables(self, df: pd.DataFrame, ruta_reporte: str, ciclo: str, reporte: str) -> None:
        """Generación del reporte de dispositivos inoperables

        :param df: datos consolidados para calcular el reporte
        :type df: pd.DataFrame
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        """
        pass

    @abstractmethod
    def _calcular_porcentajes(self, df: pd.DataFrame, ruta_reporte: str, ciclo: str, reporte: str) -> pd.DataFrame:
        """Generación del reporte de porcentajes de datos por dispositivos

        :param df: datos consolidados para calcular el reporte
        :type df: pd.DataFrame
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        :return: datos de porcentajes calculados para generar el dashboard
        :rtype: pd.DataFrame
        """
        pass

    @abstractmethod
    def _generar_dashboard(self, df_consolidado: pd.DataFrame, ruta_reporte: str, ciclo: str, reporte: str) -> None:
        """Generación del dashboard

        :param df_consolidado: datos consolidados para generar el dashboard
        :type df: pd.DataFrame
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        """
        pass

    @abstractmethod
    def _preparar_nombre_reporte(self, nombre_reporte: str, ruta_reporte: str, formato_fecha: str) -> str:
        """Permite preparar el nombre del reporte y la ruta donde quedará almacenado

        :param nombre_reporte: nombre del reporte a generar
        :type nombre_reporte: str
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param formato_fecha: formato de fecha que tendra el reporte
        :type formato_fecha: str
        :return: la ruta donde se almacenará el archivo
        :rtype: str
        """
        pass

    @abstractmethod
    def generar_reportes(self) -> None:
        """metodo de entrada para generar los reportes
        """
        pass
