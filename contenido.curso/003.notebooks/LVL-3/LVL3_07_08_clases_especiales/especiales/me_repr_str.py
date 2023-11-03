class Persona:

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        print("se ejecuto __str__")
        return f"__str__ ||| {Persona.__name__}(NOMBRE= {self.nombre},EDAD={self.edad})"

    def __repr__(self) -> str:
        print("se ejecuto __repr__")
        return f"MiPersonaFavorita || NOMBRE = {self.nombre}, EDAD = {self.edad}"