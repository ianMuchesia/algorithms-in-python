class TreeNode:
    def __init__(self,val=0,right=None,left=None) -> None:
        self.val = val
        self.right = right
        self.left = left
        
class BinaryTree:
    def __init__(self,root=None) -> None:
        self.root = root
        
        
    def breadthFirstSearch(self,root:TreeNode):
        queue = []
        
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    def minValueOfTree(self, root:TreeNode):
        if not root.left:
            return root.val
        else:
            return self.minValueOfTree(root.left)
        
    def maxValueOfTree(self,root:TreeNode):
        if not root.right:
            return root.val
        else:
            return self.maxValueOfTree(root.right)
        
    def deleteNodeFromTree(self,root:TreeNode,val):
        if not root:
            return root
        if val < root.val:
            root.left = self.deleteNodeFromTree(root.left,val)
        elif val > root.val:
            root.right = self.deleteNodeFromTree(root.right,val)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.value = self.minValueOfTree(root.right)
            root.right = self.deleteNodeFromTree(root.right,root.val)
        return root
            
            
            
        
    def deleteNode(self,val:int):
        self.root = self.deleteNodeFromTree(self.root,val)
                
        
        
        
        
        

node1 = TreeNode(10)
node1.left = TreeNode(5)
node1.left.left = TreeNode(3)
node1.left.right = TreeNode(7)
node1.right = TreeNode(15)

bst = BinaryTree()
# bst.breadthFirstSearch(node1)
# print(bst.minValueOfTree(node1))
bst.root = node1
bst.deleteNode(7)
bst.breadthFirstSearch(bst.root)

        