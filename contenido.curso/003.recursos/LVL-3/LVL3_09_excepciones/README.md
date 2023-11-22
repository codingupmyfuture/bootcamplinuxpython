# EXCEPCIONES

una interrupción brusca a la ejecución de mi programa (profundizar). Estas excepciones, en un proyecto grande, pueden generar la pérdida de:

* Información
* Dinero
* De su empleo
* De cliente
* ETC.

## GENERALES 
Cómo se manejan las excepciones en Python:

```python
#estructura de excepciones

try: # obligatorio
  
  #1/0
  print("1. Bloque principal de código a evaluar")
except: # obligatorio
  print("-1. Bloque de captura de excepción. Nota: permite múltiple except")
else: # opcionales
  print("2. Bloque después de terminado el bloque 1")
finally: # opcionales
  print("3. Bloque que siempre se ejecuta")

```
## ASSERTS 

El assert es una instrucción de Python que te permite definir 
condiciones que deben cumplirse siempre. En caso de que la expresión 
booleana sea True assert no hace nada y en caso de False dispara una excepción


```python
# sin mensaje
x = 1
assert x == 2
```

```python
# con mensjae
x = 1
assert x == 2, "el valor no es igual a 1"
```