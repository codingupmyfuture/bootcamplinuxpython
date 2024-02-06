import sys
import traceback
from nasa.comunes.excepcion import NasaAppException


def test_excepcion_personalizada():
    """función para validar la excepción modificada
    """
    try:
        1 / 0
    except Exception as ex:

        nasaAppException: NasaAppException = NasaAppException(
            codigo_error=100,
            mensaje=str(ex) + "\n" + traceback.format_exc(),
            sys_info=sys.exc_info()
        )

        assert nasaAppException._error is not None
        assert len(str(nasaAppException)) > 100
