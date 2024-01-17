
from calidad.calidad.pruebas.linting import diccionario, resultado

def test_diccionario(app):
    assert diccionario["a"] == 1
    assert diccionario["b"] == 2

def test_resultado(app):
    assert resultado == 8
