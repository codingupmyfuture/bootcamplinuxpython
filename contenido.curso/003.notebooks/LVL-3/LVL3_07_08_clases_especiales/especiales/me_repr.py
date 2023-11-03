class Persona:
    """
        __repr__
            utilizado para crear una representación de cadena de un objeto
            es utilizado por desarrolladores
            hazlo lo más descriptivo posible
            llamado cuando la función repr()
    """
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        
    def __repr__(self) -> str:
        return f"MiPersonaFavorita || NOMBRE = {self.nombre}, EDAD = {self.edad}"