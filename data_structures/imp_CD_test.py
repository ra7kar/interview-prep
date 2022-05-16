# pytest script for simulate cd command.

import pytest
from imp_CD import imp_cd


@pytest.mark.parametrize(
    "cur_path, commands, result",
    [
        ("/Users/rct/src/interview-prep/data_structures", ["../.."], "/Users/rct/src/"),
        (
            "/Users/rct/src/interview-prep/data_structures",
            ["../..", "data_structure"],
            "/Users/rct/src/data_structure/",
        ),
        (
            "/Users/rct/src/interview-prep/data_structures",
            ["../..", "data_structure", "/User/rct", "..", "/", "test", "abc"],
            "/test/abc/",
        ),
    ],
)
def test_imp_cd(cur_path, commands, result):
    assert imp_cd(cur_path, commands) == result
