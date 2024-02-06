# TECDEV: SEC#1, ID#1, MANEJO DE TYPING | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, MANEJO DE DOCSTRINGS | TODO EL ARCHIVO
# TECDEV: SEC#1, ID#4, NO VALORES HARCODEADOS
# TECDEV: SEC#2, ID#10, PROPERTIES
class ValoresConstantesNoHarcodeados:
    """MANEJO DE CONSTANTES

    Manejar constantes en una aplicación es una buena práctica cuando se tienen valores que no deben cambiar durante la
    ejecución del programa. Las constantes proporcionan un nombre descriptivo a valores específicos y facilitan el
    mantenimiento del código.
    """

    @property
    def UNKN(self) -> str:
        """UNKN

        :return: bandera lógica para controlar el projecto unknown
        :rtype: str
        """
        return "UNKN"

    @property
    def UNKNOWN(self) -> str:
        """UNKNOWN

        :return: bandera lógica para controlar el estado unknown
        :rtype: str
        """
        return "unknown"

    @property
    def NOREPORT(self) -> str:
        """NOREPORT
        permite parámetrizar la marca que tendran todas las carpetas para poder saber si se les genero reporte o no.
        Esto se hace ya que el proceso no es secuencial, y es una forma simple de saber que se proceso o no.

        :return: marca para agregar a los ciclos generados
        :rtype: str
        """
        return "_noreporte"

    @property
    def LOG(self) -> str:
        """LOG

        :return: permite manejar la extensión que se estará usando para el programa
        :rtype: str
        """
        return ".log"

    @property
    def KILLED(self) -> str:
        """KILLED

        :return: bandera lógica para controlar el estado killed
        :rtype: str
        """
        return "killed"

    @property
    def GENERADOR(self) -> str:
        """GENERADOR

        :return: nombre del módulo para generar archivos aleatorios
        :rtype: str
        """
        return "generador"

    @property
    def REPORTES(self) -> str:
        """REPORTES

        :return: nombre del módulo para reportes
        :rtype: str
        """
        return "reporteador"

    @property
    def CONFIGAPP(self) -> str:
        """CONFIGAPP

        :return: nombre del archivo de configuración
        :rtype: str
        """
        return "app.yaml"

    @property
    def CONFMSG(self) -> str:
        """REPORTES

        :return: nombre del módulo para reportes
        :rtype: str
        """
        return "mensajes.yaml"

    @property
    def PANADAS(self) -> str:
        """PANADAS

        :return: metodo para generar los reportes usando pandas
        :rtype: str
        """
        return "pandas"

    @property
    def PYTHON(self) -> str:
        """PYTHON

        :return: metodo para generar los reportes usando python
        :rtype: str
        """
        return "python"
