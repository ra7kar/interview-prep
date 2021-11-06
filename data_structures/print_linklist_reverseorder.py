# Print linklist in revers order


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
        for i in pylist:
            self.add(i)

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self._add(self.head, data)

    def _add(self, sub_node, data):
        cur_node = sub_node

        while cur_node is not None:
            if cur_node.next is None:
                cur_node.next = Node(data)
                return
            cur_node = cur_node.next

    def __str__(self) -> str:
        return ", ".join(str(i.data) for i in self)

    def __iter__(self):
        cur_node = self.head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def print_reverse(self):
        cur_node = self.head
        out = []
        while cur_node is not None:
            out.append(cur_node.data)
            cur_node = cur_node.next

        return [ele for ele in reversed(out)]

    def reverse_linked_list(self):
        if self.head is None:
            return

        # Move first node to new list
        new_l_head = self.head
        old_l_head = self.head.next
        new_l_head.next = None  # Remove connection to old list
        old_l_head.print()
        while old_l_head:
            # Caputre the next of old list
            temp = old_l_head.next

            # Move current head to new list
            old_l_head.next = new_l_head
            new_l_head = old_l_head

            # Assign the next of old list as current head
            old_l_head = temp

        self.head = new_l_head


def compare_lists(llist1, llist2):

    cur_node_l1 = llist1.head
    cur_node_l2 = llist2.head
    while cur_node_l1 and cur_node_l2:
        if cur_node_l1.data != cur_node_l2.data:
            return 0
        cur_node_l1 = cur_node_l1.next
        cur_node_l2 = cur_node_l2.next

    if cur_node_l1 or cur_node_l2:
        return 0

    return 1


def list_count(llist):
    count = 0
    cur_node = llist.head

    while cur_node:
        count += 1
        cur_node = cur_node.next

    return count


ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
llist = LinkedList(ll)
print(llist)
lrev = llist.print_reverse()
print(lrev)

llist.reverse_linked_list()
print(llist)

l1 = [1, 2]
l2 = [1]

llist1 = LinkedList(l1)
llist2 = LinkedList(l2)

ret = compare_lists(llist1, llist2)
print(ret)
