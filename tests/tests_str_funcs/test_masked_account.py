from utils.str_funcs import get_masked_account_number


def test_empty_num():
    assert get_masked_account_number("") == ""


def test_num_card():
    assert get_masked_account_number("1111222233334444") == "**4444"
