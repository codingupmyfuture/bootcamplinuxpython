class Demo2:
    
    def saludar(self, nombre: str) -> None:
        """método al que se accede por instancia para saludar

        :param nombre: nombre de la persona a saludar
        :type nombre: str
        """
        print(f"saludo a: {nombre}")
        
    @classmethod
    def saludar_metodo_clase(cls, nombre: str) -> None:
        """Los metodos de clase están vinculados a la clase y no a la instancia de
        la clase.
        
        Como resultado, se pueden llamar en la propia clase o en cualquier instancia de la clase

        :param nombre: nombre de la persona a saludar
        :type nombre: str
        """
        print(id(cls))
        print(f"saludo a: {nombre}")