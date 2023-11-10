
from typing import List

lista_numeros: List[int] = [1,2,3,4,5,6,7,8,9,10]
lista_correos: List[str] = [
    "MeQuierOmorir@gmail.com",
    "PaoPao.ParaElena@gmail.com",
    "cristian.mOntys34Gmail.com"
]

# [NIVEL1] forma declarada
def al_cuadrado(numero: int) -> int:
    return numero ** 2

nueva_lista = list(map(al_cuadrado, lista_numeros))
# nueva_lista el tipo de dato es mapobject, castear a lista para tener
# un dato conocido

# [NIVEL2] forma anónima
nueva_anonima = list(map(lambda x: x ** 2, lista_numeros))

# [NIVEL3] forma anónima
# nuevos_emails = list(map(lambda x: x.lower(), lista_numeros))
nuevos_emails = list(map(str.lower, lista_correos))


print(f"[NIVEL1] lista con función declarada --> {nueva_lista}")
print(f"[NIVEL2] lista con función anónima   --> {nueva_anonima}")
print(f"[NIVEL3] lista con función anónima   --> {nuevos_emails}")