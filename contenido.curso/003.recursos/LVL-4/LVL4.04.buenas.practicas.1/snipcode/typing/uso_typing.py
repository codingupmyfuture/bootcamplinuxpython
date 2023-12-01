from typing import List, Tuple, Dict, Optional, Callable, Any, Union
# NOTA: para datos complejos

# [1.variables]
texto: str = ""
mi_lista: List[int] = [1, 2, 3]
mi_lista: List[Any] = [1, True, 3.14]
mi_lista_2: List[Dict[str, Any]]
mi_tupla: Tuple[str, int, float] = ('Hola', 10, 3.14)
mi_diccionario: Dict[str, int] = {'Juan': 25, 'María': 30}


# [2.funciones]

# parámetros simples
def sumar_elementos(lista: List[int], edades: Dict[str, int], nombre: str, max_edad: int, promedio: float) -> int:
    pass

# parámetros funciones y retornos
def obtener_nombre(activo: bool, funcion: Callable[[str, int], bool], nombre: Optional[str] = None) -> List[str]:
    pass

# [3. ejemplos +1]

# union
genero: Union[Optional[str], int]

# any
datos: Dict[str, Dict[str, List[Any]]] = {
    "elemento": {
        "a": [1, False]
    }
}


datos = {
    "elemento": {
        "a": [1, False]
    }
}