import requests
from coast.settings import *


LOGGER = get_logger()
url = URL.format(
    api_function=API_FUNCTION, symbol=SYMBOL, market=MARKET, api_key=API_KEY
)


def collect_json_api_data():
    try:
        response = requests.get(url)
        response_json = response.json()
    except Exception:
        LOGGER.error("Error to collect the data from API")
        raise

    return response_json
