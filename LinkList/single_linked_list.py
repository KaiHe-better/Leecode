from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# iterating linklist
def printList(node):
    while node:
        print(node.val)
        node = node.next  
     
print("raw linkedList :")   
printList(node1)



# reverse linklist
def reverse_list(head: Optional[Node]) -> Optional[Node]:
    new_sub_list = None
    while head:
        temp = head.next   
         
        head.next = new_sub_list
        new_sub_list = head
        
        head = temp
    return new_sub_list


print("reversed linkedList :")  
printList(reverse_list(node1))
