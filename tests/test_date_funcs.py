from utils.date_funcs import get_formatted_isodatetime


def test_isodate():
    assert get_formatted_isodatetime("2019-07-03T18:35:29.512364") == "03.07.2019"
