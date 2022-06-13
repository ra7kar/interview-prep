# pytest for Tries,

import pytest

from tries import Trie


@pytest.mark.parametrize(
    "search_w, result",
    [
        ("battt", False),
        ("apple", True),
    ],
)
def test_tries(search_w, result):
    trie = Trie()
    trie.add_word("apple")
    trie.add_word("at")
    trie.add_word("att")
    trie.add_word("btt")

    assert trie.search(search_w) == result
