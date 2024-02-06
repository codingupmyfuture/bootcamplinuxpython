import os
import json
import yaml
import pandas as pd
from datetime import datetime
from tabulate import tabulate
from typing import Any, Dict, List
from __meta__ import __basedir__, __copyright__
from nasa.comunes.decoradores import App
from nasa.modelamiento.abstraccion.reportes import Misiones
from nasa.modelamiento.enumeradores.reportes import CodigoReportes
from nasa.modelamiento.herencia.acciones_os import AccionesDirectorios
from nasa.modelamiento.propiedades.instancias import ObjetoTransversal


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#8, ABSTRACCIÓN
# TECDEV: SEC#2, ID#6, HERENCIA
class Pandas(AccionesDirectorios, Misiones):
    """Esta clase permite generar los reportes usando la librería pandas, la cual
    fue una de las recomendaciones (para que saliera mas facil)

    :param AccionesDirectorios: clase heredada con los metodos
    :type AccionesDirectorios: AccionesDirectorios
    """

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self, objetoTransversal: ObjetoTransversal):
        """constructor de la clase

        :param objetoTransversal: objeto que tiene las instancias principales del programa
        :type objetoTransversal: ObjetoTransversal
        """
        self.__app: ObjetoTransversal = objetoTransversal

    # TECDEV: SEC#2, ID#7, POLIMORFISMO
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        ciclo: str = ruta.split(os.sep)[-1].replace(self.__app.constante.NOREPORT, "")
        ruta_reportes: str = os.path.join(self.__app.ruta_reportes, ciclo)

        # crear carpeta
        self.crear_carpeta(ruta_reportes)

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["ruta"].format(ruta_reportes=ruta_reportes)
        )
        return ruta_reportes

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def _obtener_info_archivos(self, ruta_archivos: str) -> List[Dict[str, Any]]:
        """Permite obtener la información de cada uno de los archivos generados asociados al ciclo

        :param ruta_archivos: ruta del ciclo
        :type ruta_archivos: str
        :return: lista con la información de cada ciclo
        :rtype: List[Dict[str, Any]]
        """
        datos: List[Dict[str, Any]] = []
        for archivo in self.listar_archivos(ruta_archivos):
            # si son .log, see lee el archivo
            if archivo.endswith(self.__app.constante.LOG):
                with open(os.path.join(ruta_archivos, archivo)) as leer_archivo:
                    contenido = yaml.safe_load(leer_archivo)
                    datos.append(contenido)
        return datos

    # DOCDEV: PAG#6, REPORTE: Análisis de eventos | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        # calculo reporte
        df_tmp: pd.DataFrame = df.where(df.mission != self.__app.constante.UNKN).groupby(
            ['mission', 'device_type', 'device_status']
        ).size().reset_index(name='counter')

        # almacenar reporte
        df_tmp.to_csv(ruta_reporte, index=False)

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["reporte_generado"].format(
                tabulate(df_tmp, headers='keys', tablefmt='psql'),
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )

    # DOCDEV: PAG#6, REPORTE: Gestión de desconexiones | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        # calculo reporte
        df_tmp: pd.DataFrame = df.where(df.mission == self.__app.constante.UNKN).groupby(
            ['mission', 'device_type', 'device_status']
        ).size().reset_index(name='counter')

        # almacenar reporte
        df_tmp.to_csv(ruta_reporte, index=False)

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["reporte_generado"].format(
                tabulate(df_tmp, headers='keys', tablefmt='psql'),
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )

    # DOCDEV: PAG#6, REPORTE: Consolidación de misiones | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        # calculo reporte
        df_tmp: pd.DataFrame = df.where(
            df.mission != self.__app.constante.UNKN
        ).where(df.device_status == self.__app.constante.KILLED).groupby(
            ['mission', 'device_type', 'device_status']
        ).size().reset_index(name='counter')

        # almacenar reporte
        df_tmp.to_csv(ruta_reporte, index=False)

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["reporte_generado"].format(
                tabulate(df_tmp, headers='keys', tablefmt='psql'),
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )

    # DOCDEV: PAG#6, REPORTE: Cálculo de porcentajes | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        # calculo reporte
        df_tmp: pd.DataFrame = df.groupby(['mission', 'device_type']).size().reset_index(name='count')
        total_datos: int = df_tmp['count'].sum()
        df_tmp['percentage'] = round((df_tmp['count'] / total_datos) * 100, 2)

        # almacenar reporte
        df_tmp.to_csv(ruta_reporte, index=False)

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["reporte_generado"].format(
                tabulate(df_tmp, headers='keys', tablefmt='psql'),
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )
        return df_tmp

    # DOCDEV: PAG#6, REPORTE: Generación de tablero de control | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        # generar reporte
        with open(ruta_reporte, 'w') as reporte:
            with open(os.path.join(__basedir__, "nasa", "config", "logotipos", self.__app.config.logotipo)) as logo:
                reporte.write("\n" + self.__app.utilitarios.obtener_encabezado(logo.read(), "dashboard") + "\n")
                reporte.write(tabulate(df_consolidado, headers='keys', tablefmt='psql', showindex=False))
                reporte.write("\n" + __copyright__ + "\n")

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["dashboard"].format(
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        return os.path.join(
            ruta_reporte,
            self.__app.config.nombre_reportes.format(
                reporte=nombre_reporte,
                formato_fecha_archivo=formato_fecha
            )
        )

    # TECDEV: SEC#2, ID#14, DECORADORES
    @App.tiempo_ejecucion(mostrar_reporte=True)
    def generar_reportes(self) -> None:
        """metodo de entrada para generar los reportes
        """
        # lista de carpetas generada
        lista_carpetas: List[str] = [
            carpeta for carpeta
            in self.listar_archivos(self.__app.ruta_archivos) if self.__app.constante.NOREPORT in carpeta
        ]

        # Generación de reportes por cada carpeta
        for carpeta in lista_carpetas:
            # calcular variables basada sobre cada carpeta
            carpeta = os.path.join(self.__app.ruta_archivos, carpeta)
            fecha_reporte: str = datetime.now().strftime(self.__app.config.formato_fecha_archivo)
            ruta_reporte: str = self._preparar_nombre_carpeta(carpeta)
            contenido_ciclo: List[Dict[str, Any]] = self._obtener_info_archivos(carpeta)
            ciclo: str = carpeta.split(os.sep)[-1].replace(self.__app.constante.NOREPORT, "")

            # los archivos asociados al la carpeta quedan cargados a un solo dataframe (mirar logs)
            # recursos/logs
            df: pd.DataFrame = (pd.DataFrame(contenido_ciclo))[self.__app.config.orden_columnas.split(",")]

            # se deben generar 5 reportes, para esto use Enums
            for reporte in CodigoReportes:
                match reporte:
                    # sección para generar preporte análisis de reporte
                    case CodigoReportes.REP_ANALISIS_EVENTOS:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_ANALISIS_EVENTOS.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        self._generar_analisis_eventos(
                            df,
                            ruta_reporte_tmp,
                            ciclo,
                            CodigoReportes.REP_ANALISIS_EVENTOS.name
                        )
                    # sección para generar preporte de desconexiones
                    case CodigoReportes.REP_GEST_DESCONEXIONES:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_GEST_DESCONEXIONES.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        self._generar_desconexiones(
                            df,
                            ruta_reporte_tmp,
                            ciclo,
                            CodigoReportes.REP_GEST_DESCONEXIONES.name
                        )
                    # sección para generar dispositivos inoperables
                    case CodigoReportes.REP_CONS_MIS_INOP:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_CONS_MIS_INOP.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        self._generar_dispositivos_inoperables(
                            df,
                            ruta_reporte_tmp,
                            ciclo,
                            CodigoReportes.REP_CONS_MIS_INOP.name
                        )
                    # sección para generar distribución de dispositivos
                    case CodigoReportes.REP_CALC_PORCENTAJES:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_CALC_PORCENTAJES.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        df_procentajes: pd.DataFrame = self._calcular_porcentajes(
                            df,
                            ruta_reporte_tmp,
                            ciclo,
                            CodigoReportes.REP_CALC_PORCENTAJES.name
                        )
                    # sección para generar tablero de control
                    case CodigoReportes.REP_TABLERO_CONTROL:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_TABLERO_CONTROL.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        self._generar_dashboard(
                            df_procentajes,
                            ruta_reporte_tmp,
                            ciclo, CodigoReportes.REP_TABLERO_CONTROL.name
                        )

            # DOCDEV: PAG#6, REPORTE: Limpieza de archivos | seccion 4.4
            # mover archivos en este punto
            self.mover_carpeta(
                carpeta,
                os.path.join(
                    self.__app.ruta_respaldo,
                    carpeta.split(os.sep)[-1].replace(self.__app.constante.NOREPORT, self.__app.config.segmento_ok)
                )
            )


# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#8, ABSTRACCIÓN
# TECDEV: SEC#2, ID#6, HERENCIA
class Python(AccionesDirectorios, Misiones):
    """Esta clase permite generar los reportes usando python elemental,  es decir
    lo visto en los niveles 1 y 2.

    :param AccionesDirectorios: clase heredada con los metodos
    :type AccionesDirectorios: AccionesDirectorios
    """

    # TECDEV: SEC#2, ID#12, CONSTRUCTORES
    def __init__(self, objetoTransversal: ObjetoTransversal):
        """constructor de la clase

        :param objetoTransversal: objeto que tiene las instancias principales del programa
        :type objetoTransversal: ObjetoTransversal
        """
        self.__app: ObjetoTransversal = objetoTransversal

    # TECDEV: SEC#2, ID#7, POLIMORFISMO
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        ciclo: str = ruta.split(os.sep)[-1].replace(self.__app.constante.NOREPORT, "")
        ruta_reportes: str = os.path.join(self.__app.ruta_reportes, ciclo)

        # crear carpeta
        self.crear_carpeta(ruta_reportes)

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["ruta"].format(ruta_reportes=ruta_reportes)
        )
        return ruta_reportes

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def _obtener_info_archivos(self, ruta_archivos: str) -> List[Dict[str, Any]]:
        """Permite obtener la información de cada uno de los archivos generados asociados al ciclo

        :param ruta_archivos: ruta del ciclo
        :type ruta_archivos: str
        :return: lista con la información de cada ciclo
        :rtype: List[Dict[str, Any]]
        """
        datos: List[Dict[str, Any]] = []
        for archivo in self.listar_archivos(ruta_archivos):
            if archivo.endswith(self.__app.constante.LOG):
                with open(os.path.join(ruta_archivos, archivo), "r") as leer_archivo:
                    contenido = yaml.safe_load(leer_archivo)
                    datos.append(contenido)
        return datos

    # DOCDEV: PAG#6, REPORTE: Análisis de eventos | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def _generar_analisis_eventos(
        self,
        datos: List[Dict[str, Any]],
        ruta_reporte: str,
        ciclo: str,
        reporte: str
    ) -> None:
        """Generación del reporte de analisis de eventos

        :param datos: datos consolidados para calcular el reporte
        :type df: List[Dict[str, Any]]
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        """
        resultados: Dict[str, Any] = {}

        # para generar el reporte usando solo diccionarios, me parecio mas apropiado crear
        # genrarquias para agrupar datos, o mirandolo de otro modo, como excel
        for dato in datos:
            clave_mision = dato['mission']
            clave_dispositivo = dato['device_type']
            clave_estado = dato['device_status']
            conteo = 1

            if clave_mision not in resultados:
                resultados[clave_mision] = {}

            if clave_dispositivo not in resultados[clave_mision]:
                resultados[clave_mision][clave_dispositivo] = {}

            if clave_estado not in resultados[clave_mision][clave_dispositivo]:
                resultados[clave_mision][clave_dispositivo][clave_estado] = 0

            resultados[clave_mision][clave_dispositivo][clave_estado] += conteo

        # guardar reporte
        diccionario_ordenado = dict(sorted(resultados.items()))
        with open(ruta_reporte, 'w') as reporte:
            reporte.write(self.__app.config.encabezados_rep_1 + '\n')

            # itero sobre el diccionario ordenado y escribir cada entrada en el archivo
            for mision, dispositivos in diccionario_ordenado.items():
                for dispositivo, estados in dispositivos.items():
                    for estado, conteo in estados.items():
                        reporte.write(f'{mision},{dispositivo},{estado},{conteo}\n')

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["reporte_generado"].format(
                json.dumps(diccionario_ordenado, indent=4),
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )

    # DOCDEV: PAG#6, REPORTE: Gestión de desconexiones | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def _generar_desconexiones(self, datos: List[Dict[str, Any]], ruta_reporte: str, ciclo: str, reporte: str) -> None:
        """Generación del reporte de dispositivos de desconexiones

        :param datos: datos consolidados para calcular el reporte
        :type datos:  List[Dict[str, Any]]
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        """
        # filtrar datos para quitar unknown
        datos_filtrados: List[Dict[str, Any]] = [
            elemento for elemento in datos
            if elemento["mission"] == self.__app.constante.UNKN
        ]
        resultados: Dict[str, Any] = {}

        # para generar el reporte usando solo diccionarios, me parecio mas apropiado crear
        # genrarquias para agrupar datos, o mirandolo de otro modo, como excel
        for resultado in datos_filtrados:
            mision = resultado['mission']
            dispositivo = resultado['device_type']
            conteo = 1

            if mision not in resultados:
                resultados[mision] = {}

            if dispositivo not in resultados[mision]:
                resultados[mision][dispositivo] = 0

            resultados[mision][dispositivo] += conteo

        # guardar reporte
        with open(ruta_reporte, 'w') as reporte:
            reporte.write(self.__app.config.encabezados_rep_1 + '\n')

            # itero sobre el diccionario ordenado y escribir cada entrada en el archivo
            for mision, dispositivos in resultados.items():
                for dispositivo, estados in dispositivos.items():
                    reporte.write(f'{mision},{dispositivo},{self.__app.constante.UNKNOWN},{estados}\n')

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["reporte_generado"].format(
                json.dumps(resultados, indent=4),
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )

    # DOCDEV: PAG#6, REPORTE: Consolidación de misiones | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def _generar_dispositivos_inoperables(
        self,
        datos: List[Dict[str, Any]],
        ruta_reporte: str,
        ciclo: str,
        reporte: str
    ) -> None:
        """Generación del reporte de dispositivos inoperables

        :param datos: datos consolidados para calcular el reporte
        :type datos: List[Dict[str, Any]]
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        """
        resultados: Dict[str, Any] = {}
        # filtrado de datos
        datos_filtrados: List[Dict[str, Any]] = [
            dato for dato in datos
            if dato["mission"] != self.__app.constante.UNKN and dato['device_status'] == self.__app.constante.KILLED]

        # para generar el reporte usando solo diccionarios, me parecio mas apropiado crear
        # genrarquias para agrupar datos, o mirandolo de otro modo, como excel
        for resultado in datos_filtrados:
            mision = resultado['mission']
            dispositivo = resultado['device_type']
            conteo = 1

            if mision not in resultados:
                resultados[mision] = {}

            if dispositivo not in resultados[mision]:
                resultados[mision][dispositivo] = 0

            resultados[mision][dispositivo] += conteo

        # Generar el archivo CSV actualizado sin csv.writer
        with open(ruta_reporte, 'w') as reporte:
            # Escribir la cabecera del CSV
            reporte.write(self.__app.config.encabezados_rep_1 + '\n')

            # Iterar sobre el diccionario ordenado y escribir cada entrada en el archivo
            for mision, dispositivos in resultados.items():
                for dispositivo, estados in dispositivos.items():
                    reporte.write(f'{mision},{dispositivo},{self.__app.constante.KILLED},{estados}\n')

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["reporte_generado"].format(
                json.dumps(resultados, indent=4),
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )

    # DOCDEV: PAG#6, REPORTE: Cálculo de porcentajes | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def _calcular_porcentajes(
        self,
        datos: List[Dict[str, Any]],
        ruta_reporte: str,
        ciclo: str, reporte: str
    ) -> List[Dict[str, Any]]:
        """Generación del reporte de porcentajes de datos por dispositivos

        :param datos: datos consolidados para calcular el reporte
        :type datos: List[Dict[str, Any]]
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        :return: datos de porcentajes calculados para generar el dashboard
        :rtype: List[Dict[str, Any]]
        """
        resultados: Dict[str, Any] = {}

        # para generar el reporte usando solo diccionarios, me parecio mas apropiado crear
        # genrarquias para agrupar datos, o mirandolo de otro modo, como excel
        for dato in datos:
            mission = dato['mission']
            device_type = dato['device_type']

            if mission not in resultados:
                resultados[mission] = {}

            if device_type not in resultados[mission]:
                resultados[mission][device_type] = 0

            resultados[mission][device_type] += 1

        # calcular los porcentajes
        total_registros = len(datos)
        resutaldos_finales: List[Dict[str, Any]] = []

        for mission, dispositivos in resultados.items():
            for device_type, count in dispositivos.items():
                porcentaje = (count / total_registros) * 100
                resutaldos_finales.append(
                    {
                        'mission': mission,
                        'device_type': device_type,
                        'count': count,
                        'percentage': round(porcentaje, 2)
                    }
                )

        # guardar reporte
        with open(ruta_reporte, 'w') as dashboard:
            dashboard.write(self.__app.config.encabezados_rep_2 + '\n')

            # escribir datos calculados
            for fila in resutaldos_finales:
                dashboard.write(f"{fila['mission']},{fila['device_type']},{fila['count']},{fila['percentage']}\n")

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["reporte_generado"].format(
                json.dumps(resutaldos_finales, indent=4),
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )
        return resutaldos_finales

    # DOCDEV: PAG#6, REPORTE: Generación de tablero de control | seccion 4.4
    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    def _generar_dashboard(self, datos: List[Dict[str, Any]], ruta_reporte: str, ciclo: str, reporte: str) -> None:
        """Generación del dashboard

        :param datos: datos consolidados para generar el dashboard
        :type datos: List[Dict[str, Any]]
        :param ruta_reporte: ruta donde se almacenara el reporte
        :type ruta_reporte: str
        :param ciclo: ciclo del archivo generado
        :type ciclo: str
        :param reporte: nombre del reporte para genera
        :type reporte: str
        """
        with open(ruta_reporte, 'w') as reporte:
            with open(os.path.join(__basedir__, "nasa", "config", "logotipos", self.__app.config.logotipo)) as logo:
                reporte.write("\n" + self.__app.utilitarios.obtener_encabezado(logo.read(), "dashboard") + "\n")
                # calcular header con format
                header = "| {:<9} | {:<20} | {:>7} | {:>12} |".format('mission', 'device_type', 'count', 'percentage')
                reporte.write("+-----------+----------------------+---------+--------------+" + "\n")
                reporte.write(header + "\n")
                reporte.write("+-----------+----------------------+---------+--------------+" + "\n")

                # imprimir filas
                datos = sorted(datos, key=lambda x: x['mission'])
                for dato in datos:
                    dato_texto: str = "| {:<9} | {:<20} | {:>7} | {:>12.2f} |\n".format(
                        dato['mission'],
                        dato['device_type'],
                        dato['count'],
                        dato['percentage']
                    )
                    reporte.write(dato_texto)
                reporte.write("+-----------+----------------------+---------+--------------+\n")
                reporte.write("\n" + __copyright__ + "\n")

        # TECDEV: SEC#1, ID#2, MANEJO DE LOGGIN
        self.__app.utilitarios.LOGGER.info(
            self.__app.mensajes.reportes["dashboard"].format(
                ciclo=ciclo,
                reporte=reporte,
                ruta_reporte=ruta_reporte
            )
        )

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
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
        return os.path.join(
            ruta_reporte,
            self.__app.config.nombre_reportes.format(
                reporte=nombre_reporte,
                formato_fecha_archivo=formato_fecha
            )
        )

    # TECDEV: SEC#2, ID#5, ENCAPSULAMIENTO
    # TECDEV: SEC#2, ID#14, DECORADORES
    @App.tiempo_ejecucion(mostrar_reporte=True)
    def generar_reportes(self) -> None:
        lista_carpetas: List[str] = [
            carpeta for carpeta
            in self.listar_archivos(self.__app.ruta_archivos) if self.__app.constante.NOREPORT in carpeta
        ]

        for carpeta in lista_carpetas:
            # calcular variables basada sobre cada carpeta
            carpeta = os.path.join(self.__app.ruta_archivos, carpeta)
            fecha_reporte: str = datetime.now().strftime(self.__app.config.formato_fecha_archivo)
            ruta_reporte: str = self._preparar_nombre_carpeta(carpeta)
            ciclo: str = carpeta.split(os.sep)[-1].replace(self.__app.constante.NOREPORT, "")

            # diccionario con los datos leidos
            datos: List[Dict[str, Any]] = self._obtener_info_archivos(carpeta)

            # se deben generar 5 reportes, para esto use Enums
            for reporte in CodigoReportes:
                match reporte:
                    # sección para generar preporte análisis de reporte
                    case CodigoReportes.REP_ANALISIS_EVENTOS:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_ANALISIS_EVENTOS.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        self._generar_analisis_eventos(
                            datos,
                            ruta_reporte_tmp,
                            ciclo,
                            CodigoReportes.REP_ANALISIS_EVENTOS.name
                        )
                    # sección para generar preporte de desconexiones
                    case CodigoReportes.REP_GEST_DESCONEXIONES:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_GEST_DESCONEXIONES.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        self._generar_desconexiones(
                            datos,
                            ruta_reporte_tmp,
                            ciclo,
                            CodigoReportes.REP_GEST_DESCONEXIONES.name
                        )
                    # sección para generar dispositivos inoperables
                    case CodigoReportes.REP_CONS_MIS_INOP:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_CONS_MIS_INOP.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        self._generar_dispositivos_inoperables(
                            datos,
                            ruta_reporte_tmp,
                            ciclo,
                            CodigoReportes.REP_CONS_MIS_INOP.name
                        )
                    # sección para generar distribución de dispositivos
                    case CodigoReportes.REP_CALC_PORCENTAJES:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_CALC_PORCENTAJES.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        porcentajes: List[Dict[str, Any]] = self._calcular_porcentajes(
                            datos,
                            ruta_reporte_tmp,
                            ciclo,
                            CodigoReportes.REP_CALC_PORCENTAJES.name
                        )
                    # sección para generar tablero de control
                    case CodigoReportes.REP_TABLERO_CONTROL:
                        ruta_reporte_tmp: str = self._preparar_nombre_reporte(
                            nombre_reporte=CodigoReportes.REP_TABLERO_CONTROL.name,
                            ruta_reporte=ruta_reporte,
                            formato_fecha=fecha_reporte
                        )
                        self._generar_dashboard(
                            porcentajes,
                            ruta_reporte_tmp,
                            ciclo, CodigoReportes.REP_TABLERO_CONTROL.name
                        )

            # DOCDEV: PAG#6, REPORTE: Limpieza de archivos | seccion 4.4
            # mover archivos en este punto
            self.mover_carpeta(
                carpeta,
                os.path.join(
                    self.__app.ruta_respaldo,
                    carpeta.split(os.sep)[-1].replace(self.__app.constante.NOREPORT, self.__app.config.segmento_ok)
                )
            )
