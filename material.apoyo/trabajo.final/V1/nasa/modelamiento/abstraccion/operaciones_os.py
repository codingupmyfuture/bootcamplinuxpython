from typing import List
from abc import ABC, abstractmethod
from nasa.modelamiento.propiedades.instancias import ObjetoTransversal


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#8, ABSTRACCIÓN
class ArchivosDirectoriosABC(ABC):
    """Permite definir las acciones a realizar en el OS

    :param ABC: ABC
    :type ABC: ABC
    """

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self, objetoTransversal: ObjetoTransversal):
        """constuctor de clase

        :param objetoTransversal: objeto con las instancias y configuración requerida
        :type objetoTransversal: ObjetoTransversal
        """
        pass

    @abstractmethod
    def crear_carpeta(self, ruta_carpeta: str) -> None:
        """permite crear una carpeta a partir de parámetro enviado

        :param ruta_carpeta: ruta de carpeta a crear en el OS
        :type ruta_carpeta: str
        """
        pass

    @abstractmethod
    def mover_carpeta(self, carpeta_origen: str, carpeta_destino: str) -> None:
        """Permite mover una carpeta a otra

        :param carpeta_origen: carpeta de donde estan los datos a copiar
        :type carpeta_origen: str
        :param carpeta_destino: carpeta destino
        :type carpeta_destino: str
        """
        pass

    @abstractmethod
    def listar_archivos(self, ruta: str) -> List[str]:
        """permite listar los archivos que se encuentrán en una carpeta determinada

        :param ruta: ruta que se desea listar
        :type ruta: str
        :return: lista de archivos
        :rtype: List[str]
        """
        pass

    @abstractmethod
    def delta(self, ruta_archivo_delta: str, lectura: bool = True, valor_delta: int = 0) -> int:
        """método especial para calcular un delta, es decir, una secuencia de generación consecutiva.
        Por buenas prácticas, siempre se recomienda mantener trazabilidad de todas las acciones realizadas.
        Esta propuesta es sumamente simple y rudimentaria, pero eficiente para el propósito de este ejercicio.

        :param ruta_archivo_delta: ruta donde se almacenara el delta
        :type ruta_archivo_delta: str
        :param lectura: indica si es lectura o escritura, defaults to True
        :type lectura: bool, optional
        :param valor_delta: valor incremental que se calcula a partir de un delta previo, defaults to 0
        :type valor_delta: int, optional
        :raises Exception: si el delta esta es corrupto, no permite el avance
        :return: valor delta leido, en caso que sea escrutura, siempré retornará 0
        :rtype: int
        """
        pass

    def _preparar_nombre_carpeta(self, ruta: str, ciclo: int = 0) -> str:
        """computa el nombre de la carpeta a ser creada

        :param ruta: ruta principal
        :type ruta: str
        :param ciclo: nro de ciclo para agregar a la carpeta, defaults to 0
        :type ciclo: int, optional
        :return: ruta final para ser creada
        :rtype: str
        """
        pass
