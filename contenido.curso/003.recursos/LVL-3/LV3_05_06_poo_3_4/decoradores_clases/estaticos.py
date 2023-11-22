class Demo:
    
    def saludar(self, nombre: str) -> None:
        """método al que se accede por instancia para saludar

        :param nombre: nombre de la persona a saludar
        :type nombre: str
        """
        print(f"saludo a: {nombre}")
        
    @staticmethod
    def saludar_estaticamente(nombre: str) -> None:
        """método al que se accede por instancia para saludar

        :param nombre: nombre de la persona a saludar
        :type nombre: str
        """
        print(f"saludo a: {nombre}")