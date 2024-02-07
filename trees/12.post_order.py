from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursive_traversal(root:Optional[TreeNode]):
            if root:
                recursive_traversal(root.left)
                recursive_traversal(root.right)
                print(root.val)
                
        recursive_traversal(root)
        res = []
        def iterative_traversal(root:Optional[TreeNode]):
            stack = [root]
            
            
            
            while stack:
                node = stack.pop()
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            
                    
        iterative_traversal(root)
        print(res[::-1])
        
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(root:Optional[TreeNode]):
            if root:
                inorder_traversal(root.left)
                print(root.val)
                inorder_traversal(root.right)
            
            
        inorder_traversal(root)
                    
        def inorder_iterative(root:Optional[TreeNode]):
            stack = [root]
            
            res = []
            current = root
            
            while stack:
                if current.left:
                    res.append(current.left)
                    current = current.left
                elif stack:
                    node = stack.pop()
                    res.append(node.val)
                    
                if current.right:
                    res.append(current.right)
                    current = current.right
                        
                    

            


sol = Solution()
node1 = TreeNode(4)
node1.left = TreeNode(2)
node1.left.left = TreeNode(3)
node1.left.right = TreeNode(1)
node1.right = TreeNode(15)
node1.right.left = TreeNode(7)
node1.right.right = TreeNode(20)

sol.inorderTraversal(node1)