# Graph with Breadth first search iterative approach.
# Breadth first search uses a queue.

from collections import deque


class Graph:
    def __init__(self, graph, source_node) -> None:
        self.graph = graph
        self.source_node = source_node

    def breadth_first_search(self):
        # create a queue and initialize it with source node
        queue = deque(self.source_node)
        result = []

        while len(queue) != 0:
            current_node = queue.pop()
            result.append(current_node)

            # add neighbors to the queue.
            for node in self.graph[current_node]:
                queue.appendleft(node)

        return result


def main():

    graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
    source_node = "a"
    g = Graph(graph, source_node)
    result = g.breadth_first_search()

    print(result)


if __name__ == "__main__":
    main()
