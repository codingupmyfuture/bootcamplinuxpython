from generico.poo import MyClass as Demo
from especiales.me_repr_str import Persona

demo = Demo()
print("normal (instancia) --> ", demo)
print("normal (id)        --> ", id(demo))


persona = Persona("hijo", 6)
print("normal (instancia)    --> ", persona)
print("normal (llamando rep) --> ", persona.__repr__)
print("normal (rep str)      --> ", str(persona))
