from functools import reduce
import json


mensaje: str = """
Este es un mensaje de PRueBA con algunas PALABRAS en MAYÚSCULAS y
otras en minúsculas. El objetivo es generar un mensaje lo suficientemente
largo con al menos 100 palabras. Repetir palabras como prueba. Repetir
palabras como PRUEBA. Este es un mensaje de prueba con algunas PALABRAS en
MAYÚSCULAS y otras en minúsculas. Repetir palabras como prueba. Repetir
palabras como PRueBA. Este es un mensaje de prueba con algunas PALABRAS en
MAYÚSCULAS y otras en minúsculas. Repetir palabras como prueba. Repetir
palabras como PRUEBA. Este es un mensaje de prueba con algunas PALABRAS en
MAYÚSCULAS y otras en minúsculas. Repetir palabras como prueba. Repetir
palabras como PRUEBA. prueba Este es un mensaje de prueba con algunas PALABRAS
en MAYÚSCULAS y otras en minúsculas. Repetir palabras como prueba. Repetir
palabras como PRUEBA. Este es un mensaje de prueba con algunas PALABRAS en 
MAYÚSCULAS y otras en minúsculas. Repetir palabras como prueba. Repetir
palabras como PRUEBA. Este es un mensaje de prueba con algunas PALABRAS
en MAYÚSCULAS y otras en minúsculas. Repetir palabras como Prueba. 
Repetir palabras como PRUEBa.
"""

# PASO 1: definir función (en este caso es declarada)
def contador_palabras(acumulador: dict, palabra: str) -> dict:
    acumulador[palabra] = acumulador.get(palabra, 0) +1
    return acumulador


# PASO 2: estandarizar 
mensaje = mensaje.lower().replace("ú", "u").replace(".", "")

# PASO 3: partir/dividir las palabras | manejar palabras separadas en una lista
lista_palabras = mensaje.split()

# PASO 4: contador de palabras
documento: dict = reduce(contador_palabras, lista_palabras, {})


print(json.dumps(documento, indent=4))