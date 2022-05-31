# pytest script for Graph depth first search recursively.

import pytest
from graph_dfs_recursive import Graph


@pytest.mark.parametrize(
    "graph, source_node, result",
    [
        (
            {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []},
            "a",
            ["a", "c", "e", "b", "d", "f"],
        ),
        (
            {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []},
            "a",
            ["a", "b", "d", "f", "c", "e"],
        ),
    ],
)
def test_dfs_recur(graph, source_node, result):
    g = Graph(graph, source_node)
    g.dfs_recursive(source_node) == result
