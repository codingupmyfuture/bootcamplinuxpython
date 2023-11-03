class Persona:
    """
        __str__
            utilizado para crear una representación de cadena de un objeto

            se utiliza para las funciones repr() y str()
            normalmente se utiliza para mostrar propósitos al usuario final, lógica, etc.
            si __str__ no está implementado, Python buscará __repr__ en su lugar
    """
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        print("se ejecutó __str__")
        return f"__str__ ||| {Persona.__name__}(NOMBRE= {self.nombre},EDAD={self.edad})"