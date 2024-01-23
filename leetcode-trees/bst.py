from typing import Optional
class Node:
    def __init__(self,val:int, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left
        
        
class BinarySearchTree:
    def __init__(self) -> None:
        self.root:Node = None
        
    def insertNode(self,val:int):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            return self.insert(self.root,node)
        
    def insert(self,root:Optional[Node],node:Optional[Node]):
      
        
        if node.val > root.val:
            if not root.right:
                root.right = node
            else:
                self.insert(root.right, node)
            
        else:
            if not root.left:
                root.left = node
            else:
                self.insert(root.left,node)
                
                
    def search(self, root:Optional[Node],val:int):
        if not root:
            return None
        if root.val == val:
            return True
        
        if root.val > val:
            return self.search(root.left, val)
        else:
            return self.search(root.right,val)
        
    def search_results(self,val:int):
        if not self.root: return False
        return self.search(self.root,val) == True
    
    
    def pre_order(self, root:Optional[Node]):
        if root:
            print(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)
            
    def inorder(self, root:Optional[Node]):
        if root:
            self.pre_order(root.left)
            print(root.val)
            self.pre_order(root.right)
            
            
    def post_order(self,root:Optional[Node]):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.val)
            
    
    
tree = BinarySearchTree()
tree.insertNode(10)
tree.insertNode(15)
tree.insertNode(5)
tree.pre_order(tree.root)
print(tree.search_results(1))
            
        
        
            
        