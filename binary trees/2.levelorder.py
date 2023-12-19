from bt import Node

class LevelOrder:
    def __init__(self) -> None:
        self.root = None
        
    def level_order_print(self, root: Node):
        if not root:
            return
        traversal = ""
        queue = []
        queue.append(root)  # Enqueue the root node

        while len(queue) > 0:
            current = queue.pop(0)  # Dequeue the front element
            traversal += str(current.value) + " "

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        print(traversal.strip())
    
    
    def levelorder_reversal(self,root:Node):
        if not root:
            return
        
        traversal =  ""
        
        stack = []
        queue = []
        
        queue.append(root)
        
        while len(queue)>0:
            
            curr = queue.pop(0)
            stack.append(curr)
            
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
        
        while len(stack) >  0:
            curr = stack.pop()
            traversal += str(curr.value) + " "
        print(traversal)
            
        
    def height(self,root:Node):
        
        if not root:
            return -1
        
        left_height = self.height(root.left)
        
        right_height = self.height(root.right)
        
        return 1 + max(left_height, right_height)
    
    def myHeightImplementation(self, root:Node,counter = 0):
        
        if not root:
            return counter-1
        
   
        total1 = self.myHeightImplementation(root.left, counter+1)
        total2 = self.myHeightImplementation(root.right, counter+1)
        
        return max(total1, total2)
    
    
    def size_of_tree(self, root:Node):
        
        if root is None:
            return
        
        
        stack = []
        stack.append(root)
        count = 1
        while len(stack)>0:
            
            curr = stack.pop()
            if curr.left:
                count+=1
                stack.append(curr.left)
            if curr.right:
                count+=1
                stack.append(curr.right)
                
           
                
        print(count)
    
    def size_of_tree_recursion(self, root:Node):
        if not root:
            return 0


        left = self.size_of_tree_recursion(root.left)
        right = self.size_of_tree_recursion(root.right)

        print("left:", left, "right:", right)
        return left + right +1
            
            
            
        
            
        
        
    
    
    
    

# Example usage:
node = Node(1)
node.left = Node(3)
node.left.left = Node(5)
node.left.right = Node(7)
node.right = Node(15)

bst = LevelOrder()
bst.level_order_print(node)

bst.levelorder_reversal(node)
print(bst.myHeightImplementation(node))
print(bst.height(node))
print(bst.size_of_tree_recursion(node))
bst.size_of_tree(node)