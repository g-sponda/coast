import requests
from coast.settings import *


LOGGER = get_logger()
url = URL.format(
    api_function=API_FUNCTION, symbol=SYMBOL, market=MARKET, api_key=API_KEY
)


def collect_json_api_data():
    """
    Method to get data from alphavantage API

    @return: json response
    """
    try:
        LOGGER.debug("Request the alphavantage API")
        response = requests.get(url)
        response_json = response.json()
    except Exception:
        LOGGER.error("Error to collect the data from API")
        raise

    return response_json


def transform_data_daily_digital_currency(json_data):
    """
    @param json_data: the json response from alphavantage API
    @return: list of objects from `Time Series (Digital Currency Daily)`. Example:
    [{'close': '479.02343370',
    'date': '2014-04-01',
    'high': '491.26727280',
    'low': '468.48010552',
    'market_cap': '30128027.04467774',
    'open': '468.48010552',
    'volume': '62894.68306786'},]
    """
    LOGGER.debug('Get data of "Time Series (Digital Currency Daily)" object')
    digital_currency_daily_data = json_data["Time Series (Digital Currency Daily)"]

    formatted_data = []
    LOGGER.debug("Start collecting the values that we need")
    for k, v in digital_currency_daily_data.items():
        date = k
        # Here we collect just from `a` subindex, because the `b` is USD too and has the same values
        formatted_data.append(
            {
                "open": v["1a. open (USD)"],
                "high": v["2a. high (USD)"],
                "low": v["3a. low (USD)"],
                "close": v["4a. close (USD)"],
                "volume": v["5. volume"],
                "market_cap": v["6. market cap (USD)"],
                "date": date,
            }
        )

    return formatted_data
