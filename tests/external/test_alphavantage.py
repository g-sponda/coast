from unittest.mock import Mock, patch
import datetime
from coast.external.alphavantage import (
    collect_json_api_data,
    transform_data_daily_digital_currency,
)

resp = {
    "Meta Data": {
        "1. Information": "Daily Prices and Volumes for Digital Currency",
        "2. Digital Currency Code": "BTC",
        "3. Digital Currency Name": "Bitcoin",
        "4. Market Code": "USD",
        "5. Market Name": "United States Dollar",
        "6. Last Refreshed": "2019-07-28 (end of day)",
        "7. Time Zone": "UTC",
    },
    "Time Series (Digital Currency Daily)": {
        "2019-07-28": {
            "1a. open (USD)": "9488.50408833",
            "1b. open (USD)": "9488.50408833",
            "2a. high (USD)": "9569.95971173",
            "2b. high (USD)": "9569.95971173",
            "3a. low (USD)": "9200.99536095",
            "3b. low (USD)": "9200.99536095",
            "4a. close (USD)": "9538.97653615",
            "4b. close (USD)": "9538.97653615",
            "5. volume": "42768.10768802",
            "6. market cap (USD)": "407963975.73158306",
        },
        "2019-07-27": {
            "1a. open (USD)": "9864.13785022",
            "1b. open (USD)": "9864.13785022",
            "2a. high (USD)": "10166.72248707",
            "2b. high (USD)": "10166.72248707",
            "3a. low (USD)": "9408.97913481",
            "3b. low (USD)": "9408.97913481",
            "4a. close (USD)": "9460.70116492",
            "4b. close (USD)": "9460.70116492",
            "5. volume": "68399.00314447",
            "6. market cap (USD)": "647102528.72846913",
        },
        "2019-07-26": {
            "1a. open (USD)": "9908.05440211",
            "1b. open (USD)": "9908.05440211",
            "2a. high (USD)": "9908.05440211",
            "2b. high (USD)": "9908.05440211",
            "3a. low (USD)": "9726.15907976",
            "3b. low (USD)": "9726.15907976",
            "4a. close (USD)": "9869.51696924",
            "4b. close (USD)": "9869.51696924",
            "5. volume": "41990.93000446",
            "6. market cap (USD)": "414430196.23310685",
        },
    },
}


@patch("coast.external.alphavantage.requests.get")
def test_collect_json_api_data_with_response(mock_get):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = resp

    response = collect_json_api_data()

    assert response == resp


@patch("coast.external.alphavantage.requests.get")
def test_collect_json_api_data_with_response_none(mock_get):
    mock_get.return_value.ok = False

    uncompleted_todos = collect_json_api_data()

    assert mock_get.called == True
    assert uncompleted_todos == None


def test_transform_data_daily_digital_currency():
    expected = [
        {
            "open": "9488.50408833",
            "high": "9569.95971173",
            "low": "9200.99536095",
            "close": "9538.97653615",
            "volume": "42768.10768802",
            "market_cap": "407963975.73158306",
            "date": datetime.datetime(2019, 7, 28, 0, 0),
        },
        {
            "open": "9864.13785022",
            "high": "10166.72248707",
            "low": "9408.97913481",
            "close": "9460.70116492",
            "volume": "68399.00314447",
            "market_cap": "647102528.72846913",
            "date": datetime.datetime(2019, 7, 27, 0, 0),
        },
        {
            "open": "9908.05440211",
            "high": "9908.05440211",
            "low": "9726.15907976",
            "close": "9869.51696924",
            "volume": "41990.93000446",
            "market_cap": "414430196.23310685",
            "date": datetime.datetime(2019, 7, 26, 0, 0),
        },
    ]

    assert transform_data_daily_digital_currency(resp) == expected
