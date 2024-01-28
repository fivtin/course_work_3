from utils.str_funcs import split_by_4


def test_empty():
    assert split_by_4('') == ''


def test_16num():
    assert split_by_4("1111222233334444") == "1111 2222 3333 4444"
