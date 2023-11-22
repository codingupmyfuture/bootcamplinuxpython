class Calculadora:
    
    def __init__(self, numero_1, numero_2) -> None:
        self.__numero_1 = numero_1
        self.__numero_2 = numero_2

    def suma(self):
        return self.__numero_1 + self.__numero_2