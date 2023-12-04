class Stack:
    def __init__(self):
        self.items = []
        self.length = 0
        
    def is_empty(self):
        return self.length == 0
        

    def push(self, items):
        self.items.append(items)
        self.length += 1
    def pop(self):
        if  self.is_empty():
            return "stack is empty"
            
        self.length -= 1   
        return self.items.pop()
    def print_stack(self):
        if self.is_empty():
            print("stack is empty")
            return
        for item in self.items:
            print(item, end=" ")
            
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return
        return self.items[-1]



stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")

stack.print_stack()