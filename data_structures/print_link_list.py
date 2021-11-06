# print link list

# Node class


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "({})".format(self)


class Linklist:
    def __init__(self, pylist=None):
        if pylist is None:
            return "List is empty"

        self.root = None
        for i in pylist:
            self.add(i)

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add_helper(self.root, data)

    def _add_helper(self, sub_node, data):
        if sub_node.next is None:
            sub_node.next = Node(data)
        else:
            self._add_helper(sub_node.next, data)

    def __str__(self):
        return "\n".join(str(i.data) for i in self)

    def __iter__(self):
        cur_node = self.root
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next


ll = [2, 4, 6, 8, 9]
linklist = Linklist(ll)
print(linklist)
