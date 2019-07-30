from coast.process_relative_span import jsonify_max_span


def test_jsonify_max_span():
    result_query = (2017, 52, 14.923775252053172)
    expected = '{"year_week": "2017-W52"}'

    assert jsonify_max_span(result_query) == expected
