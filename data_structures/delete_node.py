# deleteNode


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return "({})".format(self.data)


class LinkList:
    def __init__(self, pylist=[]) -> None:
        self.head = None
        for i in pylist:
            self.add(i)

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node

    def __str__(self):
        return ",".join(str(i.data) for i in self)

    def __iter__(self):
        cur_node = self.head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def delete_node(self, position):
        cur_node = self.head
        counter = 1
        if counter == position:
            next_node = cur_node.next
            cur_node = None
            self.head = next_node
            return

        while counter < (position - 1):
            cur_node = cur_node.next
            counter += 1

        next_node = cur_node.next
        cur_node.next = next_node.next
        next_node.next = None


position = 1
llist = [1, 2, 3, 4, 5, 6, 7, 8]
ll = LinkList(llist)
print(ll)
print("Delete location : " + str(position))
ll.delete_node(position)
print(ll)
