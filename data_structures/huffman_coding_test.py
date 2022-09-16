# pytest for Huffman coding problem.

import pytest
from huffman_coding import HuffmanCoding


@pytest.mark.parametrize(
    "text, result", [("abac", "0 10 0 11"), ("adbcacc", "10 110 111 0 10 0 0")]
)
def text_huffman_coding(text, result):
    hc = HuffmanCoding(text)
    assert hc.compress() == result
