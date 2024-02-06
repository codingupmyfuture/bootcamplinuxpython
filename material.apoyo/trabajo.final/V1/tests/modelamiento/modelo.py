from nasa.modelamiento.modelo.archivos import ContenidoArchivo


def test_pydantic() -> None:
    """validación del modelo de pydantic
    """
    contenido = ContenidoArchivo(date="2022-01-30", mission="MSN1", device_type="DT", device_status="ST")
    assert contenido.date == "2022-01-30"
    assert contenido.mission == "MSN1"
    assert contenido.device_type == "DT"
    assert contenido.device_status == "ST"
    assert contenido.hash == ""
