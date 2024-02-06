from nasa.modelamiento.enumeradores.reportes import CodigoReportes


def test_enum_valores() -> None:
    """Validación de enumeradores por valor
    """
    assert CodigoReportes.REP_ANALISIS_EVENTOS.value == 1
    assert CodigoReportes.REP_GEST_DESCONEXIONES.value == 2
    assert CodigoReportes.REP_CONS_MIS_INOP.value == 3
    assert CodigoReportes.REP_CALC_PORCENTAJES.value == 4
    assert CodigoReportes.REP_TABLERO_CONTROL.value == 5


def test_enum_nombres() -> None:
    """Validación de enumeradores por nombre
    """
    assert CodigoReportes.REP_ANALISIS_EVENTOS.name == "REP_ANALISIS_EVENTOS"
    assert CodigoReportes.REP_GEST_DESCONEXIONES.name == "REP_GEST_DESCONEXIONES"
    assert CodigoReportes.REP_CONS_MIS_INOP.name == "REP_CONS_MIS_INOP"
    assert CodigoReportes.REP_CALC_PORCENTAJES.name == "REP_CALC_PORCENTAJES"
    assert CodigoReportes.REP_TABLERO_CONTROL.name == "REP_TABLERO_CONTROL"
