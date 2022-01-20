# students grade pytest script

import pytest
from students_grade import students_grades


@pytest.mark.parametrize(
    "py_list, result",
    [
        ([39, 40, 81, 82, 83, 84, 85], [40, 40, 81, 82, 85, 85, 85]),
        (
            [37, 38, 39, 40, 81, 82, 83, 84, 85, 100],
            [37, 40, 40, 40, 81, 82, 85, 85, 85, 100],
        ),
    ],
)
def test_students_grade(py_list, result):
    ret_val = students_grades(py_list)

    assert ret_val == result
