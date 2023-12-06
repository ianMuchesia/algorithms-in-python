from main import Node
from removeDuplicates import print_list

def rotateList(node,n):
    
    fast = node
    slow = None
    
    start = node
    
    count = 0
    
    while count < n:
        temp = fast
        fast = fast.next
        slow = temp
        count+=1
        
    new_start = slow.next
    slow.next = None
    
    while fast.next:
        fast = fast.next
    
    fast.next = start
    
    return new_start

 
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