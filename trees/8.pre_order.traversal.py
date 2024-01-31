from typing import Optional,List
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(res)        
        return res
       
                
        
        
                
            
   
                
                

sol = Solution()
node1 = TreeNode(3)
node1.left = TreeNode(2)
node1.left.left = TreeNode(1)
node1.left.right = TreeNode(5)
node1.right = TreeNode(15)
sol.postorderTraversal(node1)
