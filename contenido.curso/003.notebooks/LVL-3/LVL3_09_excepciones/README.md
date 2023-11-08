# EXCEPCIONES

una interrupción bruzca a la ejecución de mi programa (profundizar). Estás excepciones, en un projecto grande, pueden generar la perdida de:

* Información
* dinero
* De su empleo
* De cliente
* ETC


Como se manejan las excepciones en python:

```python
#estructura de excepciones

try: # obligatorio
  
  #1/0
  print("1. bloque principal de codigo a evaluar")
except: # obligatorio
  print("-1. bloque de captura de excepción, nota : permite multiple except")
else: # opcionales
  print("2. bloque despues de terminado bloque 1")
finally: # opcionales
  print("3. bloque que siempre se ejecuta")

```