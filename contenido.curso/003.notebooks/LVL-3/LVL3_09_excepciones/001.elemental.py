from excepciones.elemental import BootCampNivel1


try:
    print("probando nuestra excepción")
    raise BootCampNivel1("1ra excepción personalizada")
except BootCampNivel1 as ex:
    print(f"el error que generó fue: --> {ex}")