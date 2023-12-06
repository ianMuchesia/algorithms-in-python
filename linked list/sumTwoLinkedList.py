from main import Node
from removeDuplicates import print_list


def sum_two_linked_list(nodeA , nodeB):
    p = nodeA
    q = nodeB
    new_node = Node(None)
    
    carrier = 0
    total = 0
    head = new_node
    while p and q:
        total = p.data + q.data + carrier
        
        if total> 9:
            total = total -10
            carrier = 1
        else:
            carrier = 0
        #print(total)
        if new_node.data:
            tempNode = Node(total)
            print(tempNode.data)
            new_node.next = tempNode 
            new_node = new_node.next
        else:
            new_node.data = total
            
        p = p.next
        q = q.next
        
    if p:
            new_node.next = p
            p = p.next
        
    if q:
            new_node.next = q
            q = p.next
    if carrier:
        tempNode = Node(total)
        print(tempNode.data)
        new_node.next = tempNode 
               
    return head
    
    
    
# Creating nodes for the first linked list (nodeA)
nodeA1 = Node(5)
nodeA2 = Node(6)
nodeA3 = Node(3)

# Connecting nodes for the first linked list
nodeA1.next = nodeA2
nodeA2.next = nodeA3

# Creating nodes for the second linked list (nodeB)
nodeB1 = Node(8)
nodeB2 = Node(4)
nodeB3 = Node(2)

# Connecting nodes for the second linked list
nodeB1.next = nodeB2
nodeB2.next = nodeB3
        
        
        
print_list(sum_two_linked_list(nodeA1, nodeB1))