# import es la primera palabra, es sinónimo de todo
import operaciones_matematicas.elementales

# as: 1. se usa para agregar alias a las importaciones
import operaciones_matematicas.elementales as op

# tomar parte de algo
from operaciones_matematicas.elementales import suma

# tomar parte de algo más el alias
from operaciones_matematicas.elementales import suma as sm

# importación total o parcial
from operaciones_matematicas.elementales import (
    suma as lf,
    resta as vv
)

import operaciones_matematicas.elementales_objetos as objetos

# importación de clases
from operaciones_matematicas.elementales_objetos import Elementales

elementales_1 = objetos.Elementales()
elementales_2 = Elementales()

print(f"la suma es largo           : {operaciones_matematicas.elementales.suma(1,2)}")
print(f"la suma es corto           : {op.suma(5,5)}")
print(f"la suma es from            : {suma(10,10)}")
print(f"la suma es from + alias    : {sm(100,100)}")
print(f"la suma es from + alias 2  : {lf(200,200)}")
print(f"la resta es from + alias 2 : {vv(10, 5)}")
print(f"la suma es objetos         : {elementales_1.suma(10, 5)}")
print(f"la suma es objetos         : {elementales_2.suma(10, 5)}")