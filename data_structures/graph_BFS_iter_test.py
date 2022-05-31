# pytest for Breadth iterative search of a graph.

import pytest

from graph_BFS_iterative import Graph


@pytest.mark.parametrize(
    "graph, source_node, result",
    [
        (
            {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []},
            "a",
            ["a", "c", "b", "e", "d", "f"],
        ),
        (
            {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []},
            "a",
            ["a", "b", "c", "d", "e", "f"],
        ),
    ],
)
def test_BFS_iterative(graph, source_node, result):
    g = Graph(graph, source_node)
    assert g.breadth_first_search() == result
