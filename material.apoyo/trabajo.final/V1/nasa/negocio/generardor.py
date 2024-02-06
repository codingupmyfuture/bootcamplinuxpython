import os
import time
import random
from datetime import datetime
from __meta__ import __basedir__
from nasa.modelamiento.modelo.archivos import ContenidoArchivo
from nasa.modelamiento.propiedades.instancias import ObjetoTransversal
from nasa.modelamiento.herencia.acciones_os import AccionesDirectorios


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#6, HERENCIA
class Archivos(AccionesDirectorios):
    """Esta clase esta dedicada a realizar la generación de los archivos aleatorios

    :param AccionesDirectorios: clase heredada con las acciones para OS
    :type AccionesDirectorios: AccionesDirectorios
    """

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self, objetoTransversal: ObjetoTransversal):
        """constructor de la clase

        :param objetoTransversal: objeto que tiene las instancias principales del programa
        :type objetoTransversal: ObjetoTransversal
        """
        # le cargamos la configuración a la clase heredada
        super().__init__(objetoTransversal)

        # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
        self.__app: ObjetoTransversal = objetoTransversal

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def __generar_archivos(self) -> None:
        """Clase privada que permite realizar la generación de los datos
        de manera aleatoria
        """
        # valor delta
        archivo_delta: str = os.path.join(__basedir__, "nasa", "config", "deltas", "generador")
        valor_delta: int = self.delta(archivo_delta, True) - 1

        while True:
            valor_delta += 1
            self.delta(ruta_archivo_delta=archivo_delta, lectura=False, valor_delta=valor_delta)

            # toma los segundos del argumento recibido de los parámetros de la app
            time.sleep(self.__app.args.periodicidad)

            # preparo el nombre que tendra el ciclo (para cada bloque de archivos generados)
            ruta_archivo_ciclos: str = self._preparar_nombre_carpeta(ruta=self.__app.ruta_archivos, ciclo=valor_delta)

            # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
            self.__app.utilitarios.LOGGER.info(
                self.__app.mensajes.generador["segundos"].format(self.__app.args.periodicidad)
            )

            # obtejer cantidad de archivos aleatorios
            archvivos_aleatorios: int = random.randint(
                self.__app.config.rango_archivos["inicial"],
                self.__app.config.rango_archivos["final"]
            )

            # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
            self.__app.utilitarios.LOGGER.info(
                self.__app.mensajes.generador["nro_aleatorios"].format(archvivos_aleatorios=archvivos_aleatorios)
            )

            for indice in range(1, archvivos_aleatorios):
                # TECDEV: SEC#2, ID#9, DATACLASSES O PYDENTIC
                # genenerar datos aleatorios
                contenidoArchivo: ContenidoArchivo = ContenidoArchivo(
                    date=datetime.now().strftime(self.__app.config.formato_fecha_archivo),
                    mission=random.choice(self.__app.config.misiones),
                    device_type=random.choice(self.__app.config.dispositivos),
                    device_status=random.choice(self.__app.config.estados_dispositivos)
                )
                if contenidoArchivo.mission == self.__app.constante.UNKN:
                    contenidoArchivo.device_status = self.__app.constante.UNKNOWN
                    contenidoArchivo.hash = self.__app.constante.UNKNOWN
                else:
                    # calculo del hash
                    contenidoArchivo.hash = hash(
                        (
                            contenidoArchivo.date,
                            contenidoArchivo.mission,
                            contenidoArchivo.device_type,
                            contenidoArchivo.device_status
                        )
                    )

                # nombre de archivo
                nombre_archivo = self.__app.config.nombre_archivos.format(
                    indice,
                    mision=contenidoArchivo.mission,
                    cantidad_digitos=self.__app.config.nro_digitos_formato
                )
                # archivo aleatorio
                ruta_archivo_aleatorio: str = os.path.join(ruta_archivo_ciclos, nombre_archivo)

                # una de las ventajas que tiene pydantic es que puede convertir la clase a JSON, esto se
                # se realiza para escribirlo en yaml que fue el formato que seleccione
                self.__app.utilitarios.escribir_yaml(contenidoArchivo.model_dump(mode='json'), ruta_archivo_aleatorio)

                # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
                self.__app.utilitarios.LOGGER.info(
                    self.__app.mensajes.generador["arc_generado"].format(ruta_archivo_aleatorio)
                )

                # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
                self.__app.utilitarios.LOGGER.debug(
                    self.__app.mensajes.generador["datos_generados"].format(contenidoArchivo.model_dump(mode='json'))
                )

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO | púyblico
    def ejecutar(self):
        """Metodo público para acceder a la clase
        """
        self.__generar_archivos()
