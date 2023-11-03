from generico.calculadora import Calculadora
from especiales.me_call import (
    Calculadora as CalculadoraCall,
    MiDecoradorElemental,
    MiDecoradorArgumentos,
    MiDecoradorArgumentosYMetodos
)
print("\n ------------ \n")
calculadora = Calculadora(1, 1)
print("proceso normal (hasta ahora) ", calculadora.suma())

print("\n ------------ \n")
calculadora = CalculadoraCall()
print("proceso call (type) ", type(calculadora))
resultado = calculadora(1,2)
print("proceso call (valor 1)", resultado)
print("proceso call (valor 2)", calculadora(1,2))

print("\n ------------ \n")
# llamando decoradores

@MiDecoradorElemental
def mi_func_sin_args():
    print("mi primer decorador de clase sin retorno")
    

@MiDecoradorElemental
def mi_func_con_args():
    return "*" * 30
print("\n ------------ \n")
print("[LVL1] probando decorador de clase")
print("[LVL1]probando mi_func_sin_args ------")
mi_func_sin_args()

print("\n ------------ \n")
print("[LVL1]probando mi_func_con_args ------")
mi_func_con_args()




print("\n ------------ \n")
print("[LVL2] probando decorador con argumentos")

@MiDecoradorArgumentos("auxilio")
def sesion_08():
    return "me quiero morir la clase de hoy"

sesion_08()

print("\n ------------ \n")
print("[LVL2] probando decorador con argumentos y delimitador")

@MiDecoradorArgumentos("auxilio", delimitador="|")
def sesion_08_02():
    return "me quiero morir la clase de hoy"

valor_retornado = sesion_08_02()
print("utilizando el retorno despues del decorador y la ehjecución de la función")
print(valor_retornado)

print("\n ------------ \n")
print("[LVL3] probando decorador con argumentos y metodos")


@MiDecoradorArgumentosYMetodos.pela_para_elena(cuantas_veces_pao_pao=10)
def pao_pao_para_01(nombre: str):
    return nombre

pao_pao_para_01("elena")

print("\n ------------ \n")
print("[LVL3] probando decorador con instancia")
app = MiDecoradorArgumentosYMetodos("me quiero morir parte 3")

@app.pela_para_elena(cuantas_veces_pao_pao=20)
def pao_pao_para_02(nombre: str):
    return nombre

pao_pao_para_02("elena")

print("\n ------------ \n")
print("[LVL4] multiples decoradores")


@MiDecoradorArgumentos("ahora si me morí, que hago en este curso!!!")
@MiDecoradorArgumentosYMetodos.pela_para_elena(cuantas_veces_pao_pao=25)
def pao_pao_para_03(nombre: str):
        return nombre

pao_pao_para_03("elena")