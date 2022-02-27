# pytest script for Bill division program.

import pytest
from bill_division import bon_appetit


@pytest.mark.parametrize(
    "bill, k, b, result",
    [
        ([10, 20, 30, 40], 1, 40, "Bon Appetit"),
        ([10, 20, 30, 40], 1, 50, 10),
    ],
)
def test_bon_appetit(bill, k, b, result):
    assert bon_appetit(bill, k, b) == result
