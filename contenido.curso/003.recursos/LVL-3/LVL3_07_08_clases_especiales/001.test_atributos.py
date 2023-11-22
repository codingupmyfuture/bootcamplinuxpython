from generico.procedural import suma as sm
from generico.poo import MyClass as Demo

"""
__name__: Este atributo proporciona el nombre de la función, 
clase o módulo en forma de cadena de caracteres
"""
print("__name__ | funcion -->", sm.__name__)
print("__name__ | clase   -->", Demo.__name__)

"""
__annotations__: Este atributo almacena las anotaciones de tipo (type hints) definidas en una función
"""
print("__annotations__ | funcion -->", sm.__annotations__)


"""
__doc__: Este atributo especial almacena la cadena de documentación (docstring) asociada a la clase o función, 
proporcionando información sobre su uso y funcionamiento
"""

print("__doc__ | funcion -->", sm.__doc__)
print("__doc__ | clase   -->", Demo.__doc__)

"""
__module__: Este atributo proporciona el nombre del módulo al que pertenece una función o clase. Es útil para obtener 
el nombre del módulo en el que se encuentra el objeto
"""
print("__module__ | funcion -->", sm.__module__)
print("__module__ | clase   -->", Demo.__module__)

"""
__dict__: Este atributo contiene un diccionario que almacena los atributos de una instancia de una clase. Puede ser útil para 
acceder y modificar atributos dinámicamente
"""
print("__dict__ | clase   -->", Demo.__dict__)


"""
__file__: Este atributo proporciona la ruta al archivo en el que se encuentra un módulo
"""
import pandas as pd
import generico as gen
print("__file__ | modulo", pd.__file__)
print("__file__ | modulo", gen.__file__)

"""
__class__: Este atributo proporciona la referencia de la clase (type)
"""
print("__class__ vs type  [1] -->", type(Demo))
print("__class__ | clase  [1] -->", Demo.__class__)

class Demo2:
    __class__: str = str

demo2 = Demo2()

print("__class__ vs type  [2] -->", type(demo2))
print("__class__ | clase  [2] -->", demo2.__class__)