import logging
import os
from logging.handlers import SysLogHandler

def configure_logger(logger_name: str, logger_host: str, logger_port: int) -> None:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(logger_host, logger_port))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
