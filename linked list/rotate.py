from main import Node
from removeDuplicates import print_list

def rotateList(node,n):
    p = node
    q=None
    count = 0
    head = node
    start = None
    
    while p:
        if count-1 == n:
            q = p
            start = p.next
        p = p.next
    
 
    q.next = None
    p.next = head
    
    return start


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_list(rotateList(node1,3))