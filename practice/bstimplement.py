class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.right = None
        self.left = None
        

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def is_empty(self):
        return self.root == None
        
    def insertNode(self,val):
        node = Node(val)
        
        if self.is_empty():
            self.root = node
        else:
            self.insertion_point(val, self.root)
            
            
    def insertion_point(self,val,root:Node):
        if root:
            if val <= root.value:
                if not root.left:
                    root.left = Node(val)
                else:
                    self.insertion_point(val,root.left)
            else:
                if not root.right:
                    root.right = Node(val)
                else:
                    self.insertion_point(val, root.right)
                    
    def pre_order(self, root:Node):
        if root:
            print(root.value)
            self.pre_order(root.left)
            self.pre_order(root.right)
                
        
        
bst = BinarySearchTree()


bst.insertNode(3)
bst.insertNode(2)
bst.insertNode(5)
bst.insertNode(7)


bst.pre_order(bst.root)
        
        
        
        
        
        