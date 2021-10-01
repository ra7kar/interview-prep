# remove duplicate valuse from a linked sorted list.

from typing import Counter
from linked_list import LinkedList

def remove_duplicates(llist):
    # return if llist is empty

    #start with head
    cur_node = llist.head
   
    if cur_node is None:
        return None
 
    if cur_node.next is None:
        return llist
    
    next_node = cur_node.next
    
    # loop through the llist
    while cur_node is not None :
      
        next_node = cur_node.next

        if next_node is not None and cur_node.data == next_node.data:
            cur_node.next = next_node.next
            next_node.next = None
        else:
            cur_node = cur_node.next
        
    return llist

llist = LinkedList([1,1,1,1,1,2,2,3,4,5,5,5])
print("------------------")
print(llist)
print("__________ Result _______")
ll = remove_duplicates(llist)
print(llist)


