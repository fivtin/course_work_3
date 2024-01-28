import os

from utils.file_funcs import load_from_file


def test_load_file():
    assert isinstance(load_from_file(), list)
