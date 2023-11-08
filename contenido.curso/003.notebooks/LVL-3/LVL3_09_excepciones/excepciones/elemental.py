
class BootCampNivel1(Exception):
    """cuando se quieran crear excepciones personalizadas
        la clase siempre debe heredar de Exception

    :param Exception: _description_
    :type Exception: _type_
    """
    pass


class BootCampNivel2(Exception):
    codigo_error: int = -1
    mensaje: str = "NO_DEFINIDA"

    def __init__(self, codigo_error: int, mensaje: str) -> None:
        self.codigo_error = codigo_error
        self.mensaje: str = mensaje


class BootCampNivel3(Exception):

    def __init__(self, codigo_error: int, mensaje: str, nivel: str) -> None:
        self.__codigo_error = codigo_error
        self.__mensaje: str = mensaje
        self.__nivel: str = nivel
        self.__error: str = None
        self.__helper()
        
    def __helper(self):
        self._error: dict = {
            "COD_ERROR": self.__codigo_error,
            "MESSAGE_ERROR": self.__mensaje,
            "ERROR_LEVEL": self.__nivel,
            "ERROR_FORMAT": f"""
            el código del error que se presentó es:
            
            COD: {self.__codigo_error}
            LVL: {self.__codigo_error}
            MSM: {self.__mensaje}
            """
        }
    
    def __str__(self):
        return  self._error["ERROR_FORMAT"]
