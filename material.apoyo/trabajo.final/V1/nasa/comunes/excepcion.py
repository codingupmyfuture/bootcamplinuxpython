import sys
import json


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#2, ID#11, EXCEPCIONES
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
class NasaAppException(Exception):
    """clase personalizada para generar excepciones del proyecto

    :param Exception: Hereda de la clase padre
    :type Exception: Exception
    """

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self, codigo_error: int, mensaje: str, sys_info: sys.exc_info, nivel: str = "CRITICO") -> None:
        """constructor de la clase, para recibir los atributos requeridos para dar un buena
        trazabilidad del error.

        :param codigo_error: muchas empresas manejan códigos para saber que hacer o referir a manuales
        :type codigo_error: int
        :param mensaje: mensaje del error
        :type mensaje: str
        :param nivel: muchas empresas manejan niveles de errores, para determinar el tiempo de solución
        :type nivel: str
        :param sys_info: obtiene información detallada del sistema.
        :type sys_info: sys.exc_info
        """
        self.__codigo_error = codigo_error
        self.__mensaje: str = mensaje
        self.__nivel: str = nivel
        self._error: str = None
        self.__sysinfo: sys.exc_info = sys_info
        self.__helper()

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def __helper(self) -> None:
        exc_type, _, exc_traceback = self.__sysinfo
        self._error: dict = {
            'nombre_archivo': exc_traceback.tb_frame.f_code.co_filename,
            'linea_nro': exc_traceback.tb_lineno,
            'modulo': exc_traceback.tb_frame.f_code.co_name,
            'tipo_error': exc_type.__name__,
            "codigo_error": self.__codigo_error,
            "excepcion": self.__mensaje,
            "nivel_error": self.__nivel
        }

    # TECDEV: SEC#13, ID#5, MANEJO DE MÉTODOS ESPECIALES
    def __str__(self) -> str:
        """permite definir una representación de la instancia en formato en string

        :return: representación de la clase
        :rtype: str
        """
        return json.dumps(self._error, indent=4)
