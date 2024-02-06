from nasa.comunes.decoradores import App


def test_tiempo_ejecucion_reporte(capsys):
    """función para validar el decorador encendido aplicado a una función dummy

    :param capsys: es una fixture en pytest que proporciona la capacidad de capturar la salida estándar (stdout) y la
    salida de error (stderr) generadas durante la ejecución de una prueba
    :type capsys: capsys
    """
    @App.tiempo_ejecucion(mostrar_reporte=True, ruta_logs="/tmp")
    def funcion_mock():
        return "bootcamp"

    with capsys.disabled():
        resultado: str = funcion_mock()

    # se verifica la saluda
    assert resultado == "bootcamp"


def test_tiempo_ejecucion_sin_reporte(capsys):
    """función para validar el decorador apagado aplicado a una función dummy

    :param capsys: es una fixture en pytest que proporciona la capacidad de capturar la salida estándar (stdout) y la
    salida de error (stderr) generadas durante la ejecución de una prueba
    :type capsys: capsys
    """
    @App.tiempo_ejecucion(mostrar_reporte=False, ruta_logs="/tmp")
    def funcion_mock():
        return "bootcamp"

    with capsys.disabled():
        resultado: str = funcion_mock()

    # se verifica la salida
    assert resultado == "bootcamp"
