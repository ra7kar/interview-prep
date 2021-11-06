# LinkedList


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return "({})".format(self.data)

    def print(self) -> str:
        # Recursive
        if self.next:
            connected = self.next.print()
        else:
            connected = "None"

        return "{}->{}".format(self, connected)

        # Iterative
        # cur = self
        # out = ""
        # while cur:
        #     out += str(cur) + "->"
        #     cur = cur.next
        # out += "None"
        # return out


class LinkedList:
    def __init__(self, pylist=[]) -> None:
        self.head = None
        self.tail = None
        self.len = 0
        for i in pylist:
            self.append(i)

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.len += 1

    def __len__(self):
        return self.len

    def __str__(self) -> str:
        return ", ".join(str(i.data) for i in self)

    def __iter__(self):
        cur_node = self.head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next
