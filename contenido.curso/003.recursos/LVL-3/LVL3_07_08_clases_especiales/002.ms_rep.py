from generico.poo import MyClass as Demo
from especiales.me_repr import Persona

demo = Demo()
print("normal (instancia) --> ", demo)
print("normal (id)        --> ", id(demo))


persona = Persona("hijo", 6)
print("normal (instancia) --> ", persona)
