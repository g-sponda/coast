import logging
from pythonjsonlogger import jsonlogger
from configparser import ConfigParser
from os import path, getenv


URL = "https://www.alphavantage.co/query?function={api_function}&symbol={symbol}&market={market}&apikey={api_key}"
API_FUNCTION = "DIGITAL_CURRENCY_DAILY"
SYMBOL = "BTC"
MARKET = "USD"
API_KEY = get_configurations().get("api", "token")


def get_logger():
    logger = logging.getLogger()
    configurations = get_configurations()

    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(logHandler)
    logger.setLevel(getattr(logging, configurations.get("logging", "level")))
    return logger


def get_configurations():
    configuration = ConfigParser()
    APPLICATION_ROOT_PATH = path.abspath(path.join(path.dirname(__file__), ".."))

    configuration.read(path.join(APPLICATION_ROOT_PATH, "config", "default.toml"))
    return configuration
