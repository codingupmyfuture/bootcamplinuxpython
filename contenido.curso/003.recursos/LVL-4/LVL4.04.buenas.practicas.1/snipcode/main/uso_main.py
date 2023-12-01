
import sys

print("0 ----- compila todo")

def funcion_principal():
    print("2 ----- Función principal ejecutada")

if __name__ == "__main__":
    print("1 ----- Este es el script principal")
    print(f"argumentos generales ==> {sys.argv}")
    print(f"nombre escript       ==> {sys.argv[0]}")
    funcion_principal()