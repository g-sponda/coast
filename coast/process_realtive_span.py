from coast.database.models import select


def find_max_relative_span():
    query = """
    WITH span AS (
        SELECT year, iso_week, MAX(close) AS max_close, MIN(close) AS min_close
        FROM `DAILY_DIGITAL_CURRENCY` 
        GROUP BY year, iso_week
    )
    SELECT year, iso_week, max_close, min_close, MAX((max_close - min_close)/min_close) AS max_span 
    FROM span;"""
    result = select(query)

    return result.first()
