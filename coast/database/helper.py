from coast.database.models import DailyDigitalCurrency, insert, get_latest_date
from coast.settings import get_logger
from datetime import datetime

LOGGER = get_logger()


def save_list(dict_data):
    """
    Method to save dict_data in Database
    @param dict_data: list of objects from `Time Series (Digital Currency Daily)`. Example:
    [{'close': '479.02343370',
    'date': '2014-04-01',
    'high': '491.26727280',
    'low': '468.48010552',
    'market_cap': '30128027.04467774',
    'open': '468.48010552',
    'volume': '62894.68306786'},]
    @return: True if success
    """
    latest_date = get_latest_date()
    # In case we don't have any data in database
    if latest_date is None:
        latest_date = datetime.min
        order_dict_data = sorted(dict_data, key=lambda data: data["date"])
        dict_data = order_dict_data

    for data in dict_data:
        if data["date"] <= latest_date:
            LOGGER.info(
                "The data from date {} is already in Database".format(data["date"])
            )
            break
        try:
            LOGGER.debug(data)
            daily_digital_currency = DailyDigitalCurrency(data)
            insert(daily_digital_currency)
        except Exception as e:
            LOGGER.error("Error while inserting data")
            raise

    LOGGER.debug("Finish inserts in database")
    return True
