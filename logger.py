import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def log(message, level):
    if level == "info":
        logger.info(message)
    elif level == "error":
        logger.error(message)


handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
for logger_name in ("praw", "prawcore"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
