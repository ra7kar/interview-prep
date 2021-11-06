# get node value from the tail position, tail is at 0, parent is 1 and so on.

from linked_list import LinkedList


def get_node_value(llist, position):

    cur_node = llist.head
    llist_data = []

    while cur_node:
        llist_data.append(cur_node.data)
        cur_node = cur_node.next

    return llist_data[-position - 1]


position = 3
llist = LinkedList([10, 20, 40, 60])
print(llist)
print(get_node_value(llist, position))
