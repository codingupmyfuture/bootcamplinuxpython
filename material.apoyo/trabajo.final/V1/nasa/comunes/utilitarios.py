import sys
import yaml
import logging
import argparse
from logging import handlers
from typing import Dict, Any
from datetime import datetime
from yaml.loader import SafeLoader


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
class Funcionalidades:

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self):
        """Permite configurar la variable privada para obtener la instancia configurada
        para el logger
        """
        self.__LOGGER: logging.Logger

    # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
    def configurar_logger(
        self,
        app_nombre: str,
        ruta_log: str,
        nivel_logger: int = logging.DEBUG
    ):
        """Creacion de logger personalizado para usar en la app
        :param app_nombre: nombre app
        :type app_name: str
        :param nivel_logger: CRITICAL=50, ERROR=40, WARNING=30,
            INFO=20, DEBUG=10, NOTSET=0, defaults to logging.DEBUG
        :type nivel_logger: int, optional
        """
        logger = logging.getLogger(app_nombre)
        logger.setLevel(nivel_logger)
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setLevel(nivel_logger)

        # no esta configurable, por que no deseo que funcione de esta manera.
        # los logger siempre siguen algún estandar empresarial
        # TODO: implementar configuración interna
        formatter = logging.Formatter(
            "[%(asctime)s] - [%(levelname)s] - [%(name)s] : %(message)s", "%d/%m/%Y %H:%M:%S"
        )
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)

        # para almacenarlo de manera fisica
        fileHandler = handlers.RotatingFileHandler(
            ruta_log,
            maxBytes=(1048576 * 5), backupCount=7
        )
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        self.__LOGGER = logger

    @property
    def LOGGER(self) -> logging.Logger:
        """permite utilizar una instancia de registrador configurada para almacenar
        e imprimir en la consola

        :return: logger instancia
        :rtype: logging.Logger
        """
        return self.__LOGGER

    # TECDEV: SEC#2, ID#15, MANEJO DE STATIC METHOD
    @staticmethod
    def numeros_positivos(valor: str, mensaje: str = "valor invalido: '{valor}', debe ser entero y mayor a 0.") -> int:
        mensaje = mensaje.format(valor=valor)
        valor_entero: int = 0
        try:
            valor_entero = int(valor)
            if valor_entero < 1:
                raise argparse.ArgumentTypeError(mensaje)
        # TECDEV: SEC#2, ID#11, EXCEPCIONES
        except Exception:
            raise argparse.ArgumentTypeError(mensaje)
        return int(valor)

    # TECDEV: SEC#2, ID#15, MANEJO DE STATIC METHOD
    @staticmethod
    def leer_yaml(ruta_archivo: str) -> Dict[str, Any]:
        """permite leer un archivo YAML y devolver el contenido en JSON

        :param ruta_archivo: ruta archivo configuracion
        :type ruta_archivo: str
        :return: configuracion cargada
        :rtype: Dict[str, Any]
        """
        content: Dict[str, Any] = {}
        try:
            with open(ruta_archivo) as file:
                content = yaml.load(file, Loader=SafeLoader)

        # TECDEV: SEC#2, ID#11, EXCEPCIONES
        except Exception:
            content = None
        return content

    # TECDEV: SEC#2, ID#15, MANEJO DE STATIC METHOD
    @staticmethod
    def obtener_encabezado(logotipo: str, app: str, delimitador: str = "-" * 50) -> str:
        """Permite definir el encabezado de la base de rutinas, el cual
            se mostrará cada vez que se ejecute la rutina

        :param logotipo: formato logotico
        :type logotipo: str
        :param app: nombre de la app
        :type app: str
        :param delimitador: delimitador para formato, defaults to "-"*50
        :type delimitador: str, optional
        :return: encabezado formateado con datos elementales
        :rtype: str
        """
        format_date = "%Y/%m/%d/ %H:%M:%S"
        return logotipo.format(delimitador, str(datetime.now().strftime(format_date)), app)

    # TECDEV: SEC#2, ID#15, MANEJO DE STATIC METHOD
    @staticmethod
    def escribir_yaml(datos: Dict[str, Any], archivo: str) -> None:
        # convertir a YAML y escribir en el archivo
        with open(archivo, 'w') as archivo_yaml:
            yaml.dump(datos, archivo_yaml, default_flow_style=False)

    @classmethod
    def describir_objeto(cls) -> None:
        cls.utilitarios.LOGGER.info("\n".join(dir(cls)))


class Struct:
    """
    Permite, a través de su constructor, enviar un diccionario y
    devolver un objeto estructurado con atributos de diccionario.
    """
    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self, **config: Dict[str, Any]):
        """Constructor de la clase Struct.

        :param config: diccionario con la configuracion
        :type config: Dict[str, Any]
        uso:
            >>> from nasa.comunes.utulitarios import Struct
            >>> estructura = Struct(**{'version':'1.0','createdby':'luis'})
            >>> estructura.version
            1.0
            >>> estructura.createdby
            'luis'
        """
        self.__dict__.update(config)
