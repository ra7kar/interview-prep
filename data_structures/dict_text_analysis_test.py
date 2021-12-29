# test cases dictionary example to count words in a file.


import pytest
from dict_text_analysis import text_analysis


@pytest.mark.parametrize(
    "file_name, result",
    [
        ("test1.txt", {"#": 1, "test": 2}),
        ("test2.txt", {"#": 1, "test": 2, "check": 1, "this": 1, "out": 1}),
    ],
)
def test_dict_text_analysis(file_name, result):
    count = text_analysis(file_name)
    assert count == result
