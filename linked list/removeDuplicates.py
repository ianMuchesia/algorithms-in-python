from main import Node
from mergeTwoSorted import print_list



def removeDuplicates(node):
    hashMap = {}
    
    p = node
    q = None
    head = p
    while p:
        if p.data in hashMap:
            q.next = p.next
            p = None
        else:
            hashMap[p.data] = p.data
            q = p
        p = q.next
    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(5)
node5 = Node(5)
node6 = Node(8)
node7 = Node(3)
node8 = Node(8)
node9 = Node(7)
node10 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

print(removeDuplicates(node1))
print_list(removeDuplicates(node1))