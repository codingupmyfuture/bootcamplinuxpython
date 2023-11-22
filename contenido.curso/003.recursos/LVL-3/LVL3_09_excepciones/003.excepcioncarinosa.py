from excepciones.elemental import BootCampNivel3


try:
    print("probando nuestra excepción")
    raise BootCampNivel3(
        codigo_error=100,
        mensaje="manejando mi excepción lvl 2",
        nivel="NO_BLOQUEAN"
    )
except BootCampNivel3 as lucho_error:
    print(f"el error que generó fue : --> {lucho_error}")
    print(f"el tipo de dato lucho_error: --> {type(lucho_error)}")
    print(f'errores como diccionario: --> {lucho_error._error["COD_ERROR"]}')
