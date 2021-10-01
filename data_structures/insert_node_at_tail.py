# insertNodeAtTail

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "({})".format(self.data)
        

def insertNodeAtTail(head, data):
    if head == None:
        head = Node(data)
        data = None
        return head
    else:
        cur_node = head
        if cur_node.next == None:
            cur_node.next = Node(data)
            data = None
            return head
        while cur_node.next != None or data != None:
            if cur_node.next == None:
                cur_node.next = Node(data)
                data = None
            cur_node = cur_node.next
        
        return head
        
    
   
ll = None
ll = insertNodeAtTail( ll, "10")
ll = insertNodeAtTail( ll, "12")
ll = insertNodeAtTail( ll, "14")
ll = insertNodeAtTail( ll, "16")

print(ll)
    






