from nasa.comunes.constantes import ValoresConstantesNoHarcodeados


def test_constantes():
    """función para validar el objeto constantes
    """
    valoresConstantesNoHarcodeados: ValoresConstantesNoHarcodeados = ValoresConstantesNoHarcodeados()
    assert valoresConstantesNoHarcodeados.UNKN == "UNKN"
    assert valoresConstantesNoHarcodeados.UNKNOWN == "unknown"
    assert valoresConstantesNoHarcodeados.NOREPORT == "_noreporte"
    assert valoresConstantesNoHarcodeados.LOG == ".log"
    assert valoresConstantesNoHarcodeados.KILLED == "killed"
    assert valoresConstantesNoHarcodeados.GENERADOR == "generador"
    assert valoresConstantesNoHarcodeados.REPORTES == "reporteador"
    assert valoresConstantesNoHarcodeados.CONFIGAPP == "app.yaml"
    assert valoresConstantesNoHarcodeados.CONFMSG == "mensajes.yaml"
    assert valoresConstantesNoHarcodeados.PANADAS == "pandas"
    assert valoresConstantesNoHarcodeados.PYTHON == "python"
