from coast.database.models import DailyDigitalCurrency, insert, get_latest_date
from coast.settings import get_logger
from datetime import datetime

LOGGER = get_logger()


def save_list(json_data):
    latest_date = get_latest_date()
    # In case we don't have any data in database
    if latest_date is None:
        latest_date = datetime.min
        order_json_data = sorted(json_data, key=lambda data: data["date"])
        json_data = order_json_data

    for data in json_data:
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
