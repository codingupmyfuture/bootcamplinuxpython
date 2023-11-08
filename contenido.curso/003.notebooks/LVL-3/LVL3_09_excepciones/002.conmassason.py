from excepciones.elemental import BootCampNivel2


try:
    print("probando nuestra excepción")
    raise BootCampNivel2(100, "manejando mi excepción lvl 2", )
except BootCampNivel2 as ex:
    print(f"el error que genero fue: --> {ex}")
    print(f"el codigo  es : {ex.codigo_error}")
    print(f"el mensaje es : {ex.mensaje}")