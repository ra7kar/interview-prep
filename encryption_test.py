# pytest script for encryption, hacker rank problem.

import pytest
from encryption import encryption


@pytest.mark.parametrize(
    "string, result",
    [
        (
            "if man was meant to stay on the ground god would have given us roots",
            "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau",
        ),
        ("have a nice day", "hae and via ecy"),
    ],
)
def test_encryption(string, result):
    assert encryption(string) == result
