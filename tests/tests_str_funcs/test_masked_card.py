from utils.str_funcs import get_masked_card_number


def test_empty_num():
    assert get_masked_card_number("") == ""


def test_num_card():
    assert get_masked_card_number("1111222233334444") == "111122******4444"
