import logging
from snipcode.loggin.uso_loggin_avanzado import get_logger


my_log = get_logger("evelyn", logger_level = logging.DEBUG, log_location="logs")

# ejemplos de registro de mensajes
my_log.debug('este es un mensaje de debug')
my_log.info('esto es un mensaje de información')
my_log.warning('¡cuidado! Esto es una advertencia')
my_log.error('ha ocurrido un error')
my_log.critical('este es un error crítico')
