class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()
        
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
    
    
    
class Queue_using_stack:
    def __init__(self) -> None:
        self.stack_1 = []
        self.stack_1 = []
        self.count = 0
        self.size = 5
        self.top_1 = -1
        self.top_2 = -1
        
    
    def push_1(self,data:int):
        if self.top_1 == self.size -1:
            print("overflow")
        else:
            self.top_1 += 1
            self.stack_1[self.top_1] = data
            
    
    def push_2(self,data:int):
        if self.top_2 == self.size -1:
            print("overflow")
        else:
            self.top_2 += 1
            self.stack_2[self.top_2] = data
           
    def enqueue(self, x:int):
        self.push_1(x)
        self.count += 1
        

    
    def dequeue(self):
        if self.top_1 == -1 and self.top_2 == -1:
            print("queue is empty")
        else:
            for i in range(self.count):
                a = self.pop_1()
                self.push_2(a)
            return self.pop_2()
                
        
        
    