# 给定两个可能有环，也可能无环的单链表，头结点head1和head2 (head1和head2不同).
# 实现一个函数，如果两个链表相交，则返回相交的第一个节点。
# 如果不相交，返回None


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_example_link():
    # loop linked list 1
    node0_1 = Node(1)
    node0_2 = Node(2)
    node0_3 = Node(3)
    node0_4 = Node(4)
    node0_5 = Node(5)

    node0_1.next = node0_2
    node0_2.next = node0_3
    node0_3.next = node0_4
    node0_4.next = node0_5
    node0_5.next = node0_3
    
    # loop linked list 2
    node1_1 = Node(11)
    node1_2 = Node(12)
    node1_3 = Node(13)
    node1_4 = Node(14)
    node1_5 = Node(15)

    node1_1.next = node1_2
    node1_2.next = node1_3
    node1_3.next = node1_4
    node1_4.next = node1_5
    node1_5.next = node1_2
    

    # no loop list 1
    node2_1 = Node(21) 
    node2_2 = Node(22)
    node2_3 = Node(23)
    node2_4 = Node(24)
    node2_5 = Node(25)

    node2_1.next = node2_2
    node2_2.next = node2_3
    node2_3.next = node2_4
    node2_4.next = node2_5
    
    
    # no loop list 2
    node3_1 = Node(31) 
    node3_2 = Node(32)
    node3_3 = Node(33)
    node3_4 = Node(34)
    node3_5 = Node(35)

    node3_1.next = node3_2
    node3_2.next = node3_3
    node3_3.next = node3_4
    node3_4.next = node3_5
    
    return node0_1, node1_1, node2_1, node3_1



def get_loop_node(head1, head2):
    if head1 ==None and head2==None:
        return None
    
    loop1 = get_loop(head1)
    loop2 = get_loop(head2)
    
    if loop1==None and loop2==None:
        return no_loop_find(head, head2)
    
    if loop1 is not None and loop2 is not None:
        return both_loop_find(head1, head2)
    
    return None


def get_loop(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    
    slow_p = head.next
    faster_p = head.next.next
    count = 0
    while head:
        if slow_p.val != faster_p.val:
            if slow_p.next is None or faster_p.next is None or faster_p.next.next is None:
                return None
            else:
                slow_p = slow_p.next
                faster_p = faster_p.next.next
                
        else:
            faster_p = head
            count +=1

        if count ==2:
            break
        
    return faster_p

def no_loop_find(head1, head2):
    find_head = ""
    return find_head


def both_loop_find(head1, head2):
    find_head = ""
    return find_head

def printList(node):
    while node:
        print(node.val)
        node = node.next  
    print("==============")


node0_1, node1_1, node2_1, node3_1 = get_example_link()
# find_node = get_loop_node(node0_1, node2_1)
# print(find_node)


find_node = get_loop(node1_1)
a = find_node.val if find_node is not  None  else find_node
print(a)