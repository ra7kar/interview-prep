# pytest script for tree class.

import pytest
from tree import build_tree


@pytest.mark.parametrize(
    "tree, result",
    [
        (
            {
                "Electronics": ["Laptops", "TVs", "Cellphones"],
                "Laptops": ["Lenovo", "HP", "Dell"],
                "TVs": ["Samsung", "LG"],
                "Cellphones": ["Apple", "Samsung"],
            },
            [
                "Electronics",
                "Laptops",
                "Lenovo",
                "HP",
                "Dell",
                "TVs",
                "Samsung",
                "LG",
                "Cellphones",
                "Apple",
                "Samsung",
            ],
        ),
        (
            {
                "Electronics": ["Laptops", "TVs", "Cellphones"],
                "Laptops": ["Lenovo", "HP"],
                "TVs": ["Samsung", "LG"],
                "Cellphones": ["Apple"],
            },
            [
                "Electronics",
                "Laptops",
                "Lenovo",
                "HP",
                "TVs",
                "Samsung",
                "LG",
                "Cellphones",
                "Apple",
            ],
        ),
    ],
)
def test_tree(tree, result):
    ret_list = []
    root = build_tree(tree)
    root.tree_list(ret_list) == result
