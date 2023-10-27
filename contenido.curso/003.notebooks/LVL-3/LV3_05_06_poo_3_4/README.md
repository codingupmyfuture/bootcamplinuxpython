# NOTAS

## DOCUMENTACIÓN
* recuerden que para librerias, paquetes y módulos, no debe llevar tildes
* los comandos de import tambien funcionan con atributos

## DOCUMENTACIÓN

documentación para funciones & metodos `docsStrings`

### -reST
```python
"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""
```

### GOOGLE
```python
"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""
```

### NUNPYDOC
```python
"""
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""
```
## PYTEST

1. Para mirar la ayuda
`pydoc -h`

2. Para generar la documentación de un módulo especifico
`pydoc mymodule `

ejemplo proyecto

`pydoc documentacion.docs`

solo usuarios linux, redireccionamiento
`pydoc documentacion.docs > docs/clase.docs.txt`

para generar un servidor local
`pydoc -p 8080`

`pydoc -w mymodule`

ejemplo proyecto

`pydoc documentacion.docs`