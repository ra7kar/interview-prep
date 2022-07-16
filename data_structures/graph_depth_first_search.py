# From a graph print node with a depth first search.
# input is a graph with a adjacent list of dictionary.
# A stack is used for a Depth first search.

from collections import deque


class Graph:
    def __init__(self, graph, source_node) -> None:
        self.graph = graph
        self.stack = deque(source_node)

    def depth_first_search(self):
        result = []
        while len(self.stack) > 0:
            current_node = self.stack.pop()
            result.append(current_node)
            for node in self.graph[current_node]:
                self.stack.extend(node)

        return result


def main():

    graph = {"a": ["c", "b"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

    source_node = "a"

    g = Graph(graph, source_node)
    result = g.depth_first_search()

    print("")
    print("-" * 5 + " Depth first search Order " + "-" * 10)
    print("")
    for i in result:
        print("{}{}".format(i, ", "), end="")

    print("")
    print("-" * 25)

    print(result)


if __name__ == "__main__":
    main()
