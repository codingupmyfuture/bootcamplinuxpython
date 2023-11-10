
from typing import List

lista_numeros: List[int] = [1,2,3,4,5,6,7,8,9,10]

# [NIVEL1] forma de clarada
def pares(numero: int) -> int:
    return numero % 2 == 0

nueva_lista = list(filter(pares, lista_numeros))
# nueva_lista el tipo de dato es mapobject, castear a lista para tener
# un dato conocido

# [NIVEL2] forma anonima
nueva_anonima = list(filter(lambda x: x % 2 == 0, lista_numeros))



print(f"[NIVEL1] lista con funcion declarada --> {nueva_lista}")
print(f"[NIVEL2] lista con funcion anonima   --> {nueva_anonima}")
