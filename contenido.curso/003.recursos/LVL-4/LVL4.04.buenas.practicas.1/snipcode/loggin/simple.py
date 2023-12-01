import logging

# configurar el nivel
logging.basicConfig(level=logging.ERROR)

# ejemplos de registro de mensajes
logging.debug('este es un mensaje de debug')         # 10 logging.INFO
logging.info('esto es un mensaje de información')    # 20
logging.warning('¡euidado! Esto es una advertencia') # 30 logging.WARNING
logging.error('ha ocurrido un error')                # 40 logging.ERROR
logging.critical('este es un error crítico')         # 50


for index in range(1,1500):
    logging.info(f'mensaje # {index}')