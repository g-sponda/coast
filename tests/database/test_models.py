import pytest
from datetime import datetime
from coast.database.models import (
    DailyDigitalCurrency,
    create_tables,
    drop_tables,
    insert,
    select,
    get_latest_date,
)


def test_creation_DailyDigitalCurrency():
    dict_values = {
        "close": "479.02343370",
        "date": datetime.strptime("2014-04-01", "%Y-%m-%d"),
        "high": "491.26727280",
        "low": "468.48010552",
        "market_cap": "30128027.04467774",
        "open": "468.48010552",
        "volume": "62894.68306786",
    }
    daily_digital_currency = DailyDigitalCurrency(dict_values)
    assert daily_digital_currency.close == dict_values["close"]
    assert daily_digital_currency.date == dict_values["date"]
    assert daily_digital_currency.high == dict_values["high"]
    assert daily_digital_currency.low == dict_values["low"]
    assert daily_digital_currency.market_cap == dict_values["market_cap"]
    assert daily_digital_currency.open == dict_values["open"]
    assert daily_digital_currency.volume == dict_values["volume"]


def test_creation_exception_DailyDigitalCurrency():
    dict_values = {
        "close": "479.02343370",
        "date": datetime.strptime("2014-04-01", "%Y-%m-%d"),
        "low": "468.48010552",
        "market_cap": "30128027.04467774",
        "open": "468.48010552",
        "volume": "62894.68306786",
    }
    with pytest.raises(KeyError):
        assert DailyDigitalCurrency(dict_values)
