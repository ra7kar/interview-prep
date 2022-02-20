# pytest script for day_of_programmer program.

import pytest
from day_of_programmer import day_of_programmer


@pytest.mark.parametrize(
    "year, result",
    [
        (1800, "12.09.1800"),
        (2017, "13.09.2017"),
        (2016, "12.09.2016"),
    ],
)
def test_day_of_programmer(year, result):
    assert day_of_programmer(year) == result
