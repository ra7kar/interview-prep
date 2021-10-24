# Multiply two numbers, input two link lists, result return a link list.


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self):
        return "({})".format(self.data)

    def __repr__(self):
        return "Node({})".format(repr(self.data))

    def __eq__(self, other):
        return self.data == other.data


n = Node(4)
print(n)
print(repr(n))
y = Node(10)
print(repr(y))
#assert eval(repr(n)) == n