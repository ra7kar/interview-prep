# pytest for design pdf viewer , hacker rank problem

import pytest
from design_pdf_viewer import design_pdf_viewer


@pytest.mark.parametrize(
    "h, word, result",
    [
        (
            [
                1,
                3,
                5,
                3,
                5,
                7,
                8,
                6,
                4,
                3,
                3,
                2,
                4,
                2,
                3,
                6,
                7,
                5,
                9,
                2,
                3,
                4,
                6,
                3,
                6,
                8,
            ],
            "acbdef",
            42,
        ),
        (
            [
                1,
                3,
                5,
                3,
                5,
                7,
                8,
                6,
                4,
                3,
                3,
                2,
                4,
                2,
                3,
                6,
                7,
                5,
                9,
                2,
                3,
                4,
                6,
                3,
                6,
                8,
            ],
            "bdef",
            28,
        ),
    ],
)
def test_designer_pdf_viewer(h, word, result):
    assert design_pdf_viewer(h, word) == result
