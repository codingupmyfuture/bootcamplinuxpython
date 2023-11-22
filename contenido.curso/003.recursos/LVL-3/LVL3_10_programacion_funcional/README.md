
## ASSERTS 

El assert es una instrucción de Python que te permite definir 
condiciones que deben cumplirse siempre. En caso de que la expresión 
booleana sea True assert no hace nada y en caso de False dispara una excepción

funciona a partir de logica booleana


* pruebas unitarias
* optimización de código

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


## PROGRAMACIÓN FUNCIONAL 

Es programación a partir de funciones.

ejemplo:
   cambiar los 138 correos de mayuscula a minuscula.

```python
lista_correos: list = ["CORREO1", "correO ...138"]

nuevos_correos: list = []

for correo in lista_correos:
  nuevos_correos.append(correo.lower())
```

lambda
en la programación funcional, el desarrollador solo se tiene que encargar de dos cosas:

1. función para transformar los datos `declaradas: def` `anonimas: lambda`

2. el tipo de acción

  * `map` = misma cantidad, misma salida
  * `filter` = solo devuelve lo que sea verdaro
  * `reduce` = tener algo general a particula, eje: contador de palabras
