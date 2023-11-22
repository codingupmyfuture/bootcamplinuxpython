# lo veremos en nivel para referenciar los tipos de datos
from typing import Any


class Calculadora:
    """
    CALLABLES

        Se puede hacer que cualquier objeto emule un invocable implementando un 
        método __call__  de clase
        
        en otras palabras
        instancia e inmediatemente ejecuta algo
    """ 
    # def __call__(self, *args: Any, **kwds: Any) -> Any: lo adecúa para decoradores
    def __call__(self, numero_1, numero_2):
        return numero_1 + numero_2
    
    
    
class MiDecoradorElemental:
    
    # para crear decoradores que sean clases, tengo que usar constructor
    # function es el nombre que se le dio (le puedes poner cualquiera) y ese argumento
    # lo envía Python, no usted
    def __init__(self, function) -> None:
        self.func = function
        
    # definir call
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f"ejecutando el decorador, función original {self.func.__name__}")
        resultado = self.func(*args, **kwds)
        if resultado is None:
            print("nada que mostrar en el retorno")
        else:
            print(f"sí hay para mostrar y es: {resultado}")
        print("finalizó el decorador")
        return resultado
    
    
class MiDecoradorArgumentos:
    
    # para crear decoradores que sean clases y con arguments, tengo que usar constructor
    # para recibir los argumentos del decorador
    def __init__(self, mensaje: str, delimitador: str = "*") -> None:
        self.mensaje = mensaje
        self.delimitador = delimitador
        
    # definir call
    def __call__(self, function) -> Any:
        # function es el nombre que se le dio (le puedes poner cualquiera) y ese argumento
        # lo envía Python, no usted
        def decorador(*args: Any, **kwds: Any):
            print("ejecutando decorador con argumentos")
            print(f"delimitador : {self.delimitador}")
            print(f"mensaje : {self.mensaje}")
            print(f"decorador con argumentos: {function.__name__}")
            print(self.delimitador * 40)
            print(self.delimitador * 20)
            print(self.delimitador * 10)
            print("entró a ejecutar")
            resultado = function(*args, **kwds)
            print(f"salió de ejecutar, valor retornado ---> {resultado}")
            print(self.delimitador * 10)
            print(self.delimitador * 20)
            print(self.delimitador * 40)
            print("se ejecutó la función decorada")
            print("finalizó el decorador")
            return resultado
        return decorador
    

class MiDecoradorArgumentosYMetodos:
    
    # para crear decoradores que sean clases y con arguments, tengo que usar constructor
    # para recibir los argumentos del decorador
    def __init__(self, mensaje: str, delimitador: str = "*") -> None:
        self.mensaje = mensaje
        self.delimitador = delimitador
        
    # definir call - par argumentos de clase del decorador
    def __call__(self, function) -> Any:
        # function es el nombre que se le dio (le puedes poner cualquiera) y ese argumento
        # lo envía Python, no usted
        def decorador(*args: Any, **kwds: Any):
            print("ejecutando decorador con argumentos")
            print(f"delimitador : {self.delimitador}")
            print(f"mensaje : {self.mensaje}")
            print(f"decorador con argumentos: {function.__name__}")
            print(self.delimitador * 40)
            print(self.delimitador * 20)
            print(self.delimitador * 10)
            print("entró a ejecutar")
            resultado = function(*args, **kwds)
            print(f"salió de ejecutar, valor retornado ---> {resultado}")
            print(self.delimitador * 10)
            print(self.delimitador * 20)
            print(self.delimitador * 40)
            print("se ejecutó la función decorada")
            print("finalizó el decorador")
            return resultado
        return decorador

    @classmethod
    def pela_para_elena(cls, cuantas_veces_pao_pao: int):
        def decorador(function):
            def decorada(*args, **kwds):
                print("entrando a pao pao")
                quien_se_gano_pao_pao = function(*args, **kwds)
                mensaje: str = f" la persona {quien_se_gano_pao_pao} se ganó {cuantas_veces_pao_pao} de pao pao!"
                print(mensaje)
                print("")
                print("clap!" *  cuantas_veces_pao_pao)
                print("")
                print("saliendo de pao pao")
                return quien_se_gano_pao_pao
            return decorada
        return decorador