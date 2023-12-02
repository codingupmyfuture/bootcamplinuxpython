import sys
import logging


"""
que pasa si recibo un valor que es una letra, o un valor diferente a 
0
20
30
40
50
"""

nivel_loggin: int = 20 # INFO
print(f"argumentos generales ==> {sys.argv}")
print(f"nombre script       ==> {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"usando index         ==> {sys.argv[1]}")
    print(f"usando slices        ==> {sys.argv[1:]}")   
    nivel_loggin = int(sys.argv[2])


logging.basicConfig(level=nivel_loggin)

# ejemplos de registro de mensajes
logging.debug('este es un mensaje de debug')         # 10 logging.INFO
logging.info('esto es un mensaje de información')    # 20
logging.warning('¡cuidado! Esto es una advertencia') # 30 logging.WARNING
logging.error('ha ocurrido un error')                # 40 logging.ERROR
logging.critical('este es un error crítico')         # 50
