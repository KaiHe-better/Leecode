
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
node9 = Node(9)
node1 = Node(1)
node2 = Node(2)
node5 = Node(5)
node3 = Node(3)

node9.next = node1
node1.next = node2
node2.next = node5
node5.next = node3
node3.next = None

def partition_link_list(head, pivot):
    sh, st = None, None
    eh, et = None, None
    bh, bt = None, None
    save_head = None
    while head:
        
        save_head = head.next
        head.next = None
        
        if head.val < pivot:
            if sh is None:
                sh = head
                st = head
            else:
                st.next = head
                st = head
                
        elif head.val == pivot:
            if eh is None:
                eh = head
                et = head
            else:
                et.next = head
                et = head
        else:
            if bh is None:
                bh = head
                bt = head
            else:
                bt.next = head
                bt = head
                
        head = save_head
    
    # 如果有小于区域， 小于区域和等于区域连接
    if st:
        st.next = eh
        et = st if et is None else et # 谁连接大于区域的头，谁就是et
        
    if et: # 只要不是小于区域和等与区域都为空
        et.next = bh
        
    res = sh if sh is not None else (eh if eh is not None else mh )
    return res 
    
            
def printList(node):
    while node:
        print(node.val)
        node = node.next  
     
print("raw linkedList :")   
printList(node9)

print("partition_link_list :") 
printList(partition_link_list(node9, 3))
