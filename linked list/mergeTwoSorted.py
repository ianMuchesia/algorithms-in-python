from main import Node,LinkedList


def mergeTwoSortedLists(node_1,node_2):
    if not node_1 or not node_2:
        return
    p = node_1
    q = node_2
    s = None
    
    if p.data > q.data:
        s = q
        q = q.next
    elif q.data > p.data:
        s=p
        p = p.next
    else:
        s=p
        p=p.next
        q=q.next
        
    return_list = s

    while p and q:
        if p.data > q.data:
            s.next = q
            q = q.next
        elif q.data > p.data:
            s.next=p
            p = p.next
        else:
            s.next=p
            p=p.next
            q=q.next
        s = s.next
            
    if not p:
      s.next = q 
    if not q:
      s.next = p
            
        
    return return_list


def print_list(node):
        if not node:
            print("list is empty")
            return
        else:
            value = ''
            current = node
            
            while(current):
                value += str(current.data) + ' '
                current = current.next
            print(value)

node1 = Node(1)
node2 = Node(5)
node3 = Node(6)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

# Creating List 2
nodeA = Node(2)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(7)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
print_list(mergeTwoSortedLists(node1, nodeA))