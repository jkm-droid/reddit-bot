import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def log(message, level):
    if level == "info":
        logger.info(message)
    elif level == "error":
        logger.error(message)
