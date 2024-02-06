import os
import argparse
from typing import Dict, Any
from datetime import datetime
from nasa.comunes.decoradores import App
from nasa.comunes.utilitarios import Funcionalidades, Struct
from nasa.modelamiento.herencia.acciones_os import AccionesDirectorios
from nasa.modelamiento.propiedades.instancias import ObjetoTransversal
from nasa.comunes.constantes import ValoresConstantesNoHarcodeados


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#6, HERENCIA
class Instanciador(AccionesDirectorios):
    """EXPLICACIÓN

    El propósito de esta clase es crear un objeto que contenga todas las instancias y realice todos los cálculos
    necesarios del proceso, para luego enviarlo al constructor. De esta manera, todo estará calculado en una única
    ocasión, y la aplicación dispondrá de todos los insumos necesarios para funcionar. La ventaja de esta metodología
    radica en que, al agregar un parámetro a un archivo de configuración o a una de las clases agrupadas en un solo
    objeto, la instancia lo cargará automáticamente la próxima vez. Además, en caso de necesitar realizar cálculos
    iniciales para toda la aplicación, este proceso estará centralizado en un único lugar. Esto facilita la
    administración y el mantenimiento del código.

    Para mas información mirar: documentacion/diagramas/001.transversal.png
    """

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self, args: argparse.ArgumentParser, ruta_base: str):
        """constructor de la clase Instanciador

        :param args: argumentos de la app para generar
        :type args: argparse.ArgumentParser
        :param ruta_base: ruta donde se almacenaran los archivos generados
        :type ruta_base: str
        """
        self.__args = args
        self.__basedir: str = ruta_base

    def __cargar_configuracion_app(self, nombre_archivo: str) -> Struct:
        """permite leer el archivo de configuracion de la app
        y convertirlo a una clase con atributos dinamicos

        Mirar doc: nasa.comunes.utilitarios.Struct
        :param nombre_archivo: nombre del archivo a cargar
        :type nombre_archivo: str

        :raises Exception: si no encuentra el archivo de config
        :return: Struct con la configuracion cargada
        :rtype: Struct
        """
        config: Dict[str, Any] = Funcionalidades.leer_yaml(
            os.path.join(self.__basedir, "nasa", "config", "archivos", nombre_archivo)
        )

        if config is None:
            raise Exception("la configuracion de la app no pudo ser cargada.")
        return Struct(**config)

    # TECDEV: SEC#2, ID#14, DECORADORES
    @App.tiempo_ejecucion(mostrar_reporte=False)
    def obtener_instancias_configuracion(self) -> ObjetoTransversal:
        """Permite obtener todas las instancias y configuración transversal
        que estaran usando el proyecto

        :return: Una clase con las instancias requeridas transversalmente
        :rtype: ObjetoTransversal
        """
        # instancias
        funcionalidades = Funcionalidades()
        objetoTransversal = ObjetoTransversal()
        valoresConstantesNoHarcodeados = ValoresConstantesNoHarcodeados()

        # setear configuracion de la app en forma de struct
        objetoTransversal.config = self.__cargar_configuracion_app(valoresConstantesNoHarcodeados.CONFIGAPP)

        # setear configuracion de los mensajes en forma de struct
        objetoTransversal.mensajes = self.__cargar_configuracion_app(valoresConstantesNoHarcodeados.CONFMSG)

        # setear argumentos app
        objetoTransversal.args = self.__args

        # setear constantes
        objetoTransversal.constante = valoresConstantesNoHarcodeados

        # ruta archivos aleatorios
        objetoTransversal.ruta_archivos = os.path.join(
            self.__basedir,
            f"{os.sep}".join(objetoTransversal.config.ruta_archivos_generados.split(","))
        )

        # ruta respaldo
        objetoTransversal.ruta_respaldo = os.path.join(
            self.__basedir,
            f"{os.sep}".join(objetoTransversal.config.ruta_respaldo.split(","))
        )

        # ruta reportes
        objetoTransversal.ruta_reportes = os.path.join(
            self.__basedir,
            f"{os.sep}".join(objetoTransversal.config.ruta_reportes.split(","))
        )

        # ruta logs
        ruta_log: str = os.path.join(
            self.__basedir,
            f"{os.sep}".join(objetoTransversal.config.ruta_logs.split(","))
        )

        # ruta auditoria
        ruta_auditoria: str = os.path.join(
            self.__basedir,
            f"{os.sep}".join(objetoTransversal.config.ruta_auditoria.split(","))
        )

        # crear carpeta archivos
        self.crear_carpeta(objetoTransversal.ruta_archivos)

        # crear carpeta backup
        self.crear_carpeta(objetoTransversal.ruta_respaldo)

        # crea caroeta de logs
        self.crear_carpeta(ruta_log)

        # crear ruta de dereportes
        self.crear_carpeta(objetoTransversal.ruta_reportes)

        # crear ruta de auditoria
        self.crear_carpeta(ruta_auditoria)

        # configurar logger
        funcionalidades.configurar_logger(
            objetoTransversal.config.nombre_app,
            os.path.join(
                ruta_log,
                objetoTransversal.config.nombre_logs.format(
                    datetime.now().strftime(objetoTransversal.config.formato_log)
                )
            )
        )

        # setear clase de utilidades con loger y todo definido
        objetoTransversal.utilitarios = funcionalidades

        # mostrar header
        with open(
            os.path.join(self.__basedir, "nasa", "config", "logotipos", objetoTransversal.config.logotipo)
        ) as file:
            # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
            funcionalidades.LOGGER.info(
                "\n" + funcionalidades.obtener_encabezado(file.read(), objetoTransversal.args.command)
            )
        return objetoTransversal
