
from typing import Tuple


class TextoUtil:

    @staticmethod
    def invertir_cadena_texto(cadena: str) -> Tuple[str, int]:
        """metodo estatatico para revertir una cadena

        :param cadena: cadena de caracteres para validar
        :type cadena: str
        :return: Tuple(str, int)
        :rtype: primer valor de la tupla es la cadena invertida, segundo valor
        es la longitud de la cadena.

        Notas: en caso de que la variable cadena no sea str, los
        valores que retornara
        seran (None, -1)
        """
        if isinstance(cadena, str):
            texto_invertido: str = cadena[::-1]
            longitud: int = len(cadena)
            return (texto_invertido, longitud)
            #  return (cadena[::-1], len(cadena))
        else:
            return (None, -1)
