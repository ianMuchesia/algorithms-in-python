class Node:
    def __init__(self, data):
      self.data = data
      self.next = None


class CircularLinkedList:
    def __init__(self):
      self.head = None 

    def prepend(self, data):
        new_node = Node(data)
        
        current = self.head
        new_node.next = self.head
        
        if not self.head:
            new_node.next = new_node
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node



    def print_list(self):
        current = self.head
        
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break
      
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
        
    def remove(self, key):
        if not self.head:
            return
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
               current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            current =self.head
            prev = None
            while current.next != self.head:
                prev  = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = current.next
        
    
  #The __len__ method has been defined with underscores before and after the len keyword so that it overrides the len method to operate on a circular linked list.  
    def len(self):
        if self.head:
            current = self.head
            count = 0
            
            while current:
                count+=1
                current=current.next
                if current == self.head:
                    break
            
            return count
                
                
cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()