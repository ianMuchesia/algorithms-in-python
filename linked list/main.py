class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def append(self, val):
        node = Node(val)
        if self.isEmpty():
            self.head = node
        else:
            current = self.head
            
            while current.next:
                current = current.next
            
            current.next = node
    
    def print_list(self):
        if self.isEmpty():
            print("list is empty")
            return
        else:
            value = ''
            current = self.head
            
            while(current):
                value += str(current.data) + ' '
                current = current.next
            print(value)
    
    def prepend(self,val):
        node = Node(val)
        if self.isEmpty():
            self.head = node
        else:
            temp = self.head
            node.next = temp
            self.head = node
    def insert_after_node(self,prevNode,val):
        if not prevNode:
            print("previous node does not exist")
            return
        node = Node(val)
        
        node.next = prevNode.next
        prevNode.next = node
        
    def delete_node(self,key):
        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current:
            if(current.data ==key):
                break
            prev = current
            current = current.next
        
        prev.next = current.next
        current= None
        
    def delete_by_position(self,pos):
        if not self.isEmpty():
            current = self.head
            if pos == 0:
                self.head = current.next
                current = None
                return
            prev = None
            counter = 0
            while current:
                if counter == pos:
                    break
                prev = current
                current = current.next
                counter += 1
            
            #is keyword is used to check if two variables refer to the same object in memory
            if current is None:
                return
            prev.next = current.next
            current = None
    
    def list_length(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count
    
    def list_length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.list_length_recursive(node.next)
                    
        
        
        
        
        

node_list = LinkedList()
node_list.append(1)
node_list.append(2)
node_list.append(3)
node_list.append(4)
node_list.append(5)
node_list.prepend(7)
print(node_list.list_length_recursive(node_list.head))
node_list.delete_node(4)
node_list.delete_by_position(1)
print(node_list.list_length())
node_list.print_list()

        
        
            
            
        
        