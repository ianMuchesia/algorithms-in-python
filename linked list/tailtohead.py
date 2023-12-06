from main import Node
from removeDuplicates import print_list


def move_tail_to_head(node):
    
    p = node
    q = None
    start = node
    
    while p.next:
        temp = p
        q = temp
        p = p.next

    q.next = None   
    p.next = start
    
    return p
    
    
    
    
    
    
    
    
    
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print_list(move_tail_to_head(node1))