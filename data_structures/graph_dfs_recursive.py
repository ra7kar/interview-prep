# Graph, depth first search by recursive method.


class Graph:
    def __init__(self, graph, source_node) -> None:
        self.graph = graph
        self.source_node = source_node
        self.result = []

    def dfs_recursive(self, current_node):

        self.result.append(current_node)

        for node in self.graph[current_node]:
            self.dfs_recursive(node)

        return self.result


def main():

    graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
    source_node = "a"

    g = Graph(graph, source_node)
    result = g.dfs_recursive(source_node)

    print(result)


if __name__ == "__main__":
    main()
