import logging
import os
import sys
from datetime import datetime
from logging import handlers

def get_logger(
    app_name: str,
    log_location: str ="/tmp/logs",
    log_format: str ="%Y%m%d%H%M%S",

    logger_level: int = logging.DEBUG
):
    """
        custom logger to use in the app
        :param app_name     : name of the application or floe that is running
        :param logger_level : logger level - CRITICAL=50, ERROR=40, WARNING=30,
            INFO=20, DEBUG=10, NOTSET=0
    """

    log_save = os.path.join(
        log_location,
        (app_name or "UnknowNameLog") + "_{}.log".format(datetime.now().strftime(log_format))
    )
    logger = None
    try:
        logger = logging.getLogger(app_name or "UnknowApp")
        logger.setLevel(logger_level)
        format = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - [%(name)s] : %(message)s", "%d/%m/%Y %H:%M:%S")
        loginStreamHandler = logging.StreamHandler(sys.stdout)
        loginStreamHandler.setFormatter(format)
        logger.addHandler(loginStreamHandler)

        fileHandler = handlers.RotatingFileHandler(
            log_save, maxBytes=(1048576 * 5), backupCount=7)
        fileHandler.setFormatter(format)
        logger.addHandler(fileHandler)
    except Exception as ex:
        logger = None
    return logger

