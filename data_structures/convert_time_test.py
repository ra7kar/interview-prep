# pytest for convert_time program.

import pytest
from convert_time import convert_time


@pytest.mark.parametrize(
    "t, result",
    [("12:01:00 PM", "12:01:00"), ("12:01:00 AM", "00:01:00")],
)
def test_convert_time(t, result):
    ret_val = convert_time(t)

    assert ret_val == result
