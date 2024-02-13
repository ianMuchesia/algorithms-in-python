from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(root:Optional[TreeNode]):
            
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            
            return 1 + max(left,right)
        
    
        diameter = float("-inf")
        def traverse(root:Optional[TreeNode]):
            nonlocal diameter
            if root:
                if root.left or root.right:
                    currentMax = helper(root.left) + helper(root.right)
                
                    diameter = max(diameter,currentMax)
                
                traverse(root.left)
                traverse(root.right)
                
        
        return diameter
            