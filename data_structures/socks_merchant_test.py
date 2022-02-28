# pytest script for Socks_merchant program

import pytest
from socks_merchant import sock_merchant


@pytest.mark.parametrize(
    "n, arr, result",
    [
        (3, [1, 2, 1], 1),
        (10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3], 4),
    ],
)
def test_socks_merchant(n, arr, result):
    assert sock_merchant(n, arr) == result
