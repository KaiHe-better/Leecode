class Node:
    def __init__(self, val, next_node=None, before_node=None):
        self.val = val
        self.next = next_node
        self.before = next_node
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.before = None
node1.next = node2

node2.before = node1
node2.next = node3

node3.before = node2
node3.next = node4

node4.before = node3
node4.next = node5

node5.before = node4
node5.next = None


def print_double_linked_list(head):
    while head:
        head_val = head.val if head is not None else None
        head_before_val = head.before.val if head.before is not None else None
        head_next_val = head.next.val if head.next is not None else None
        print("val: {}, before: {}, next: {}".format(head_val, head_before_val, head_next_val))
        head = head.next
        
print_double_linked_list(node1)
print("====================================")


def reverse_double_linked_list(head):
    temp_head = None 
    while head:
        temp_next = head.next
        head.next = temp_head
        head.before = temp_next
        temp_head = head
        head = temp_next
    return temp_head



print_double_linked_list(reverse_double_linked_list(node1))