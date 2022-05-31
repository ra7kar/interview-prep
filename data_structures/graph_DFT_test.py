# pytest for Depth first search of a graph.

import pytest

from graph_depth_first_search import Graph


@pytest.mark.parametrize(
    "graph, source_node, result",
    [
        (
            {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []},
            "a",
            ["a", "c", "e", "b", "d", "f"],
        ),
        (
            {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []},
            "a",
            ["a", "b", "d", "f", "c", "e"],
        ),
    ],
)
def test_graph_DPF(graph, source_node, result):
    g = Graph(graph, source_node)
    assert g.depth_first_search() == result
