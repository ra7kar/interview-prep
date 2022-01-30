# breaking record pytest script
# hacker rank problem

import pytest
from breaking_record import breaking_record


@pytest.mark.parametrize(
    "py_list, result",
    [
        ([12, 24, 10, 24], [1, 1]),
        ([10, 5, 20, 20, 4, 5, 2, 25, 1], [2, 4]),
        ([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], [4, 0]),
    ],
)
def test_breaking_record(py_list, result):

    assert breaking_record(py_list) == result
