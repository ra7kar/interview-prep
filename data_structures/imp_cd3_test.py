# pytest script to test simulate cd command.

import pytest
from imp_cd3 import cd


@pytest.mark.parametrize(
    "cur_path, commands, result",
    [
        (
            "/Users/rct/src/interview-prep/data_structures",
            ["..", "../..", "test", "../", "test2"],
            "Users/rct/test2",
        ),
        (
            "/Users/rct/src/interview-prep/data_structures",
            ["..", "../..", "test", "../"],
            "Users/rct",
        ),
    ],
)
def test_cd(cur_path, commands, result):
    assert cd(cur_path, commands) == result
