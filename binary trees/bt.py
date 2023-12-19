class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def insert(self, value):
        node = Node(value)
        if self.isEmpty():
            self.root = node
        else:
            self.insertNode(self.root, node)
        
    def insertNode(self, root:Node,node:Node):
        if node.value < root.value:
            if root.left == None:
                root.left = node
            else:
                self.insertNode(root.left , node)
        else:
            if root.right == None:  
                root.right = node
            else:
                self.insertNode(root.right, node)
                
    def search(self, root:Node, value):
        if not root:
            return False
        else:
            if root.value == value:
                return True
            elif value < root.value:
                return self.search(root.left, value)
            else:
                return self.search(root.right, value)
    
    def preOrder(self,root:Node):
        #check if the current node is empty or null
        if root:
            
            print(root.value)
            self.preOrder(root.left)
            self.preOrder(root.right)
            
    def inOrder(self, root:Node):
        if root:
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)
    def postOrder(self, root:Node):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value)
    def levelOrderBFS(self):
        #use the optimized queue implementation
        queue:[Node] =[]
        queue.append(self.root)
        
        while len(queue):
            curr = queue.pop(0)
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)   
    
bst = BinarySearchTree()
print(bst.isEmpty())


bst.insert(10)
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(15)

print(bst.search(bst.root,15))
print(bst.search(bst.root,7))
# bst.preOrder(bst.root)
bst.inOrder(bst.root)
bst.levelOrderBFS()