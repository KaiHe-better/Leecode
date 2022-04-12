
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(2)
node5 = Node(1)

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



from collections import deque
def palindrmoe(head):
    if head is None or head.next is None:
        return True
    
    fast = head
    slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    
    fast = slow.next
    slow.next = None
    temp_node = None
    while fast:
        temp = fast.next
        fast.next = temp_node
        temp_node = fast
        fast = temp
    
    res = True
    fast = head
    while temp_node.next and fast.next:
        if temp_node.val != fast.val:
            res = False
            break
        else:
            temp_node = temp_node.next 
            fast = fast.next 
        
    
    return res

print(palindrmoe(node1))  