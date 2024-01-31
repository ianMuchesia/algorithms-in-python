from typing import Optional,List
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        res = []
        
        current = root
        
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = current.right
                
        
        
                
        
        
                
            
   
                
                

sol = Solution()
node1 = TreeNode(3)
node1.left = TreeNode(2)
node1.left.left = TreeNode(1)
node1.left.right = TreeNode(5)
node1.right = TreeNode(15)
sol.postorderTraversal(node1)
