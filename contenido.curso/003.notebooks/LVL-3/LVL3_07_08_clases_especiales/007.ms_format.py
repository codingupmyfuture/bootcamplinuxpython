# cadena.format()
# help(format)
from especiales.me_format import MiNumero

print("\n ------------ \n")
print("[LVL1] normal lo que conocemos")
print("modo elemental de formato {}".format("str.format(..)"))


print("\n ------------ \n")
print("[LVL2] usando el __format__")
print("[LVL2] __format__ ventaja: usa funciones nativas del lenguaje")
numero = MiNumero(5)

resultado_binario = format(numero, 'bin')
resultado_hexadecimal = format(numero, 'hex')
resultado_default = format(numero, 'default')

print( f'bin     --> {resultado_binario}')
print( f'hex     --> {resultado_hexadecimal}')
print( f'default --> {resultado_default}')


print("\n ------------ \n")
print("[LVL 1.5] usando el metodos normales")


resultado_binario = numero.formato('hex')
resultado_hexadecimal = numero.formato ('hex')
resultado_default = numero.formato('default')

print( f'bin     --> {resultado_binario}')
print( f'hex     --> {resultado_hexadecimal}')
print( f'default --> {resultado_default}')