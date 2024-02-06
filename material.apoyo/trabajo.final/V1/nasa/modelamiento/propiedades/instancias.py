import argparse
from nasa.comunes.utilitarios import Funcionalidades, Struct
from nasa.comunes.constantes import ValoresConstantesNoHarcodeados


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#10, PROPERTIES
class ObjetoTransversal:
    """
    Valida diferentes reglas asociadas a datos.
    Cada regla está definida por el usuario.
    """

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self):
        """
        constructor de la clase ObjetoTransversal.
        """
        self.__utilitarios: Funcionalidades
        self.__args: argparse.ArgumentParser
        self.__config: Struct
        self.__ruta_archivos: str
        self.__ruta_respaldo: str
        self.__ruta_reportes: str
        self.__constantes: ValoresConstantesNoHarcodeados
        self.__mensajes: str

    @property
    def utilitarios(self) -> Funcionalidades:
        """property para cargar instancia de Funcionalidades

        :return: utilidades propias de python
        :rtype: Funcionalidades
        """
        return self.__utilitarios

    @utilitarios.setter
    def utilitarios(self, util: Funcionalidades):
        """seteador para la instancia de Funcionalidades

        :param util: utilidades propias de python
        :type util: Funcionalidades
        """
        self.__utilitarios = util

    @property
    def args(self) -> argparse.ArgumentParser:
        """ Permite devolver el valor de los argumentos de la consola.

        :return: instancia y configuracion de los argumentos recibidos en consola
        :rtype: argparse.ArgumentParser
        """
        return self.__args

    @args.setter
    def args(self, args: argparse.ArgumentParser):
        """Permite establecer la instancia de argparse.

        :param args: instancia y configuracion de los argumentos recibidos en consola
        :type args: argparse.ArgumentParser
        """
        self.__args = args

    @property
    def config(self) -> Struct:
        """Permite devolver el valor de la configuración.

        :return: Struct con los datos de configuracion de la app
        :rtype: Struct
        """
        return self.__config

    @config.setter
    def config(self, config: Struct):
        """Permite establecer el valor de la configuración.

        :param config: Struct con los datos de configuracion de la app
        :type config: Struct
        """
        self.__config = config

    @property
    def ruta_archivos(self) -> str:
        """permite obtener la ruta de los archivos aleatorios

        :return: ruta donde se almacenaran los valores
        :rtype: str
        """
        return self.__ruta_archivos

    @ruta_archivos.setter
    def ruta_archivos(self, ruta: str):
        """permite asignar la ruta donde se almacenaran los archivos aleatorios

        :param ruta: ruta donde se almacenaran los valores
        :type ruta: str
        """
        self.__ruta_archivos = ruta

    @property
    def ruta_respaldo(self) -> str:
        """permite obtener la ruta de los archivos de respaldo

        :return: ruta donde se almacenaran los valores
        :rtype: str
        """
        return self.__ruta_respaldo

    @ruta_respaldo.setter
    def ruta_respaldo(self, ruta: str):
        """permite asignar la ruta de los archivos de respaldo

        :param ruta: ruta donde se almacenaran los archivos
        :type ruta: str
        """
        self.__ruta_respaldo = ruta

    @property
    def ruta_reportes(self) -> str:
        """permite obtener la ruta de los archivos de reporte

        :return: ruta donde se almacenaran los archivos
        :rtype: str
        """
        return self.__ruta_reportes

    @ruta_reportes.setter
    def ruta_reportes(self, ruta: str):
        """permite asignar la ruta de los archivos de reporte

        :param ruta: ruta donde se almacenaran los archivos
        :type ruta: str
        """
        self.__ruta_reportes = ruta

    @property
    def constante(self) -> ValoresConstantesNoHarcodeados:
        """permite obtener la rinstanca de consantes

        :return: ruta donde se almacenaran los archivos
        :rtype: str
        """
        return self.__constantes

    @constante.setter
    def constante(self, constantes: ValoresConstantesNoHarcodeados):
        """permite configurar la instanca de consantes

        :param ruta: ruta donde se almacenaran los archivos
        :type ruta: str
        """
        self.__constantes = constantes

    @property
    def mensajes(self) -> Struct:
        """Permite devolver el valor de la configuración.

        :return: Struct con los datos de configuracion de la app
        :rtype: Struct
        """
        return self.__mensajes

    @mensajes.setter
    def mensajes(self, mensajes: Struct):
        """Permite establecer el valor de la configuración.

        :param config: Struct con los datos de configuracion de la app
        :type config: Struct
        """
        self.__mensajes = mensajes
