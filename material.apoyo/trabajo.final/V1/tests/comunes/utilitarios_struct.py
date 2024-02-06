from nasa.comunes.utilitarios import Struct


def test_struct() -> None:
    """Función para probar la clase Struct
    """
    estructura: Struct = Struct(**{'version': '1.0', 'createdby': 'bootcamp'})
    assert estructura.version == "1.0"
    assert estructura.createdby == "bootcamp"
