import sys
from os import getenv
import time
import threading
from coast.external.alphavantage import (
    collect_json_api_data,
    transform_data_daily_digital_currency,
)
from coast.database.helper import save_list
from coast.database.models import drop_tables, create_tables
from coast.process_relative_span import find_max_relative_span, jsonify_max_span
from coast.settings import get_logger
import schedule
from flask import Flask


LOGGER = get_logger()
app = Flask(__name__)

has_collected = False


@app.route("/maxspan", methods=["GET"])
def max_span():
    result = find_max_relative_span()
    return jsonify_max_span(result)


def __collect_api_data():
    json_response = collect_json_api_data()
    data = transform_data_daily_digital_currency(json_response)
    save_list(data)


def schedule_collect_api_data():
    global has_collected
    if has_collected is False:
        __collect_api_data()
        has_collected = True
    else:
        schedule.every().day.at("00:01").do(__collect_api_data)
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    if getenv("RUN_MIGRATIONS", "no") == "yes":
        drop_tables()
        create_tables()
    try:
        threading.Thread(target=schedule_collect_api_data, args=()).start()
        app.run(host="0.0.0.0", debug=True)
    except:
        LOGGER.error("Unexpected error:", sys.exc_info()[0])
        raise
