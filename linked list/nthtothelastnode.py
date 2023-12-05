from main import Node


def nth_to_last_node(node,n):
    p = node
    q = node
    count = 0
    
    while p:
        if count >= int(n):
            q = q.next
        p = p.next
        count+=1
        
    return q.data


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

print(nth_to_last_node(node1,2))
    


