# Add two numbers : Input two link lists , output one link list sum of two link lists

# create link list


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return "({})".format(self.data)


class LinkedList:
    def __init__(self, py_list=[]):
        self.head = None
        for i in py_list:
            self.append(i)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self._append_helper(self.head, data)

    def _append_helper(self, sub_node, data):

        if sub_node.next is None:
            sub_node.next = Node(data)
        else:
            self._append_helper(sub_node.next, data)

    def __str__(self):
        return "->".join(str(i.data) for i in self)

    def __iter__(self) -> str:
        cur_node = self.head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def __add__(self, ll2):
        ll3 = LinkedList()
        total = 0
        carry = 0

        cur_node1 = self.head
        cur_node2 = ll2.head
        while cur_node1 or cur_node2:
            total = carry
            if cur_node1:
                total += cur_node1.data
                cur_node1 = cur_node1.next

            if cur_node2:
                total += cur_node2.data
                cur_node2 = cur_node2.next

            carry = 1 if total > 9 else 0

            ll3.append(total % 10)

        if carry > 0:
            ll3.append(carry)

        return ll3

    def __repr__(self):
        return "LinkedList({})".format([n.data for n in self])

    def __mul__(self, ll2):
        pass


ll1 = LinkedList([9, 9, 10, 10])
ll2 = LinkedList([1, 2])
ll3 = ll1 + ll2
print("LinkList1: " + str(ll1))
print(ll2)
print(ll3)
print(repr(ll1))
print(eval(repr(ll1)))
ll4 = ll1 * ll3
