from calidad.calidad.utilitarios.texto import TextoUtil


def test_probar_modulo_texto(app):
    assert 1 == 1
    caso_1 = TextoUtil.invertir_cadena_texto("AEIOU")
    caso_2 = app.texto_util.invertir_cadena_texto({})

    # caso_2 = app.texto_util.invertir_cadena_texto({})
    print(caso_1)
    assert caso_1[0] == "UOIEA"
    assert caso_1[1] == 5, "la longitud no concuerda"
    assert caso_2[0] == None
    assert caso_2[1] == -1, "la longitud no concuerda"
    
def test_invertir_cadena_texto(app):
    caso_2 = app.texto_util.invertir_cadena_texto({})
    assert caso_2[0] == None
    assert caso_2[1] == -1, "la longitud no concuerda"