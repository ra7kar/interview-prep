# Test script for staircase program.

import pytest
from staircase import staircase


@pytest.mark.parametrize(
    "n, result",
    [
        (4, ["   #", "  ##", " ###", "####"]),
        (6, ["     #", "    ##", "   ###", "  ####", " #####", "######"]),
    ],
)
def test_staircase(n, result):
    ret_val = staircase(n)
    assert ret_val == result
