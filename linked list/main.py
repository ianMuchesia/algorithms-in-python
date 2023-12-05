class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    #check if it is empty
    def isEmpty(self):
        return self.head == None
    
    #append to the end of the list
    def append(self, val):
        node = Node(val)
        if self.isEmpty():
            self.head = node
        else:
            current = self.head
            
            while current.next:
                current = current.next
            
            current.next = node
    
    #print the list
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
    
    #prepend to the beginning of the list
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
        
    #delete node by value
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
        
    #delete node by position
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
    
    #delete the entire list
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
                    
        
    #swap nodes 
    def swap_nodes(self, key_1,key_2):
        
        if key_1 == key_2:
            return
        prev_1=None
        current_1 = self.head
        
      
        while current_1:
            if current_1.data == key_1:
                break
            prev_1 = current_1
            current_1 = current_1.next
       
        prev_2 = None
        current_2 = self.head
        
        while current_2:
            if current_2.data == key_2:
                break
            prev_2 = current_2
            current_2 = current_2.next
          

        if not current_2 or not current_1:
            return None
        if prev_1:
            prev_1.next = current_2
        else:
            self.head = current_2
        if prev_2:
            prev_2.next = current_1
        else:
            self.head = current_1
            
        current_1.next, current_2.next = current_2.next , current_1.next
    
    #reverse a linked list
    def reverse_list(self):
        if self.isEmpty():
            return
        prev = None
        current = self.head
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        
    def recursive_reverse(self):
        if self.isEmpty():
            return
        
        def recursiveImplementation(prev,current):
            if not current:
                return prev
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            return recursiveImplementation(prev,current)
        
        self.head = recursiveImplementation(None, self.head)
            
            
        
        
        
        

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
node_list.swap_nodes(7,3)
node_list.recursive_reverse()
node_list.reverse_list()
node_list.print_list()

        
        
            
            
        
        