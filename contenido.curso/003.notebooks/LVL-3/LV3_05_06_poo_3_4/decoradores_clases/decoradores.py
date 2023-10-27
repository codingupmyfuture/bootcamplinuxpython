class MalaPractica:
    """
        los famosos getters and setters
        getter: obtener un atributo de la clase
        setter: asignación
        
        cuando se usa esto, cuando quiero de manera pública signar un valor a un atrinuto pridados
    """
    def __init__(self):
        self.__nombre: str = None
        
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre
        
    def get_nombre(self) -> str:
        return self.__nombre
    
class BuenaPractica:
    """ pasos
    
        1. el getter y el setter se llaman igual
        2. al getter se le pone  @property
        3. al setter se le llama getter.setter
        
    """
    
    def __init__(self):
        self.__nombre: str = None

    @property # este es el getter o MalaPractica.get_nombre
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter # este es el setter o MalaPractica.set_nombre
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre

