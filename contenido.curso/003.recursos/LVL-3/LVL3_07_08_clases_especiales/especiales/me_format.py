class MiNumero:
    """__format__: se utiliza para personalizar la representación de 
    formato de un objeto cuando se utiliza la función format() o 
    cuando se formatea una cadena utilizando las literales de cadena f-strings 
    (disponibles en Python 3.6 y versiones posteriores).
    """
    def __init__(self, valor):
        self.valor = valor
 
    def __format__(self, formato):
        if formato == 'bin':
            return bin(self.valor)
        elif formato == 'hex':
            return hex(self.valor)
        else:
            return str(self.valor)

    def formato(self, formato):
        if formato == 'bin':
            return bin(self.valor)
        elif formato == 'hex':
            return hex(self.valor)
        else:
            return str(self.valor)