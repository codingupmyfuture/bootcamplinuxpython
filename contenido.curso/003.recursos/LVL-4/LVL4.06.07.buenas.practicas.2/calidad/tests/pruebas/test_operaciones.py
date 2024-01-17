

def test_suma(app):
    
    assert app.funcion_suma(5, 5) == 10
    
def test_resta(app):
    assert app.funcion_resta(5, 5) == 0