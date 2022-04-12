
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

# need N extra space
def palindrmoe1(head):
    temp_deque = deque()
    temp_head = head
    while temp_head:
        temp_deque.append(temp_head)
        temp_head = temp_head.next
    
    while head:
        if head.val != temp_deque.pop().val:
            return False
        head = head.next
    
    return True

# print(palindrmoe1(node1))
   
    
# need N/2 extra space
def palindrmoe2(head):
    slow_pointer = head.next
    fast_pointer = head
    
    while fast_pointer.next and fast_pointer.next.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        
    temp_deque = deque()
    while slow_pointer :
        temp_deque.append(slow_pointer)
        slow_pointer = slow_pointer.next
        
    while len(temp_deque)>0:
        if head.val != temp_deque.pop().val:
            return False
        head = head.next
    
    return True
    
# print(palindrmoe2(node1))


# need N/2 extra space
def palindrmoe3(head):
    if head is None or head.next is None:
        return True
    
    temp_node_1 = head
    temp_node_2 = head
    temp_node_3 = None
    # fast and slow pointer
    while temp_node_2.next and temp_node_2.next.next:
        temp_node_1 = temp_node_1.next
        temp_node_2 = temp_node_2.next.next

    # reverse right part 
    temp_node_2 = temp_node_1.next
    temp_node_1.next = None
    while temp_node_2:
        temp_node_3 = temp_node_2.next
        temp_node_2.next = temp_node_1
        temp_node_1 = temp_node_2
        temp_node_2 = temp_node_3
    
    # comparing
    temp_node_3 = temp_node_1
    temp_node_2 = head
    res = True
    while temp_node_1 and temp_node_2:
        if temp_node_1.val != temp_node_2.val:
            res = False
            break
        else:
            temp_node_1 = temp_node_1.next
            temp_node_2 = temp_node_2.next
    
    # right part recover
    temp_node_1 = temp_node_3.next
    temp_node_3.next = None
    while temp_node_1:
        temp_node_2 = temp_node_1.next
        temp_node_1.next = temp_node_3
        temp_node_3 = temp_node_1
        temp_node_1 = temp_node_2
    
    return res

print(palindrmoe3(node1))