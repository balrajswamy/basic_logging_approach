import logging
from time import asctime


def log():
    logging.basicConfig(
                        filename="logs/test.log",
                        level=logging.INFO,
                        format='%(asctime)s-%(levelname)s-%(message)s',
                        datefmt ='%Y-%m-%d %I:%M:%S %p'
                        )
    return logging.getLogger()

logger = log()
logger.info("Hello world!")
