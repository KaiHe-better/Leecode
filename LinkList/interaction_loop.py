# 给定两个可能有环，也可能无环的单链表，头结点head1和head2 (head1和head2不同).
# 实现一个函数，如果两个链表相交，则返回相交的第一个节点。
# 如果不相交，返回None


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
node5.next = node3


node010 = Node(100) 
node020 = Node(20)
node030 = Node(30)
node040 = Node(40)
node050 = Node(500)

node010.next = node020
node020.next = node030
node030.next = node040
node040.next = node050



def get_loop_node():
    
    pass


