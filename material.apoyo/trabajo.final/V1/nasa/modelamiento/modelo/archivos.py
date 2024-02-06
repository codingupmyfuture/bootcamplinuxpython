from pydantic import BaseModel


# TECDEV: SEC#3, ID#17, MANEJO DE PAQUETES Y MÓDULOS
# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#2, ID#9, DATACLASSES O PYDENTIC
# DOCDEV: PAG#5, formato para cada | seccion 4.2
class ContenidoArchivo(BaseModel):
    """Permite capturar los atributos de las misiones y realizar validaciones.

    :param BaseModel: BaseModel
    :type BaseModel: BaseModel
    """
    date: str
    mission: str
    device_type: str
    device_status: str
    hash: str = ""
