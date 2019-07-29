from coast.database.models import select
from coast.settings import get_logger
import json


LOGGER = get_logger()


def find_max_relative_span():
    """
    Method to collect the max relative span
    @return: dict with keys 'year', 'iso_week', 'max_span'
    """
    # Query to get the max_span

    query = """
    WITH span AS (
        SELECT year, iso_week, MAX(close) AS max_close, MIN(close) AS min_close
        FROM `DAILY_DIGITAL_CURRENCY` 
        GROUP BY year, iso_week
    )
    SELECT year, iso_week, MAX((max_close - min_close)/min_close) AS max_span 
    FROM span;"""
    result = select(query).first()
    LOGGER.info("Result of the query: {}".format(result))
    return result


def jsonify_max_span(max_span):
    """
    Method to transform the max relative span result query to json
    @return: json formatted string
    """
    json_max_span = {
        "year_week": "{year}-W{iso_week}".format(year=max_span[0], iso_week=max_span[1])
    }

    return json.dumps(json_max_span)
