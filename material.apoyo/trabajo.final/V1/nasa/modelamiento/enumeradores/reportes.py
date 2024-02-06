from enum import Enum


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# DOCDEV: PAG#5, nombre de reportes | seccion 4.4
class CodigoReportes(Enum):

    """
        Un enum (enumeración) es un tipo de dato en muchos lenguajes de programación que representa un conjunto de
        valores constantes y asigna nombres descriptivos a esos valores. La idea principal es proporcionar un
        conjunto claro y legible de opciones o estados posibles para una variable.

        los atributos .name y .value se utilizan para acceder al nombre y al valor asociados a cada miembro de
        la enumeración. ejemplo:

        CodigoReportes.REP_ANALISIS_EVENTOS.value obtendras 1
        CodigoReportes.REP_ANALISIS_EVENTOS.name obtendras REP_ANALISIS_EVENTOS

        Otra de las ventajas que ofrece es que los enums son iterables, es decir, se pueden recorrer dinámicamente los
        elementos del enumerador y acceder a cada atributo. Esto facilita la programación más dinámica, especialmente
        si en el futuro se requiere agregar más elementos.
    """

    # cantidad de eventos por estado para cada misión y dispositivo
    REP_ANALISIS_EVENTOS: int = 1

    # identificar los dispositivos que presentan un mayor número de desconexiones
    REP_GEST_DESCONEXIONES: int = 2

    # consolidación de todas las misiones para determinar cuántos dispositivos son inoperables
    REP_CONS_MIS_INOP: int = 3

    # porcentajes de datos generados para cada dispositivo y misión con respecto a la cantidad total de datos
    REP_CALC_PORCENTAJES: int = 4

    # simulación de un tablero de control
    REP_TABLERO_CONTROL: int = 5
