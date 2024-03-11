import logging
from logging.handlers import SysLogHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="basic.log",
    filemode="w",
)


def configure_logger(logger_name: str, logger_host: str, logger_port: int) -> None:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(logger_host, logger_port))
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
