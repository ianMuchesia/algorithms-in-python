# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth,right_depth)
    
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode], count = 0) -> int:
        if not root:
            return count
    
        left_depth = self.maxDepth(root.left, count + 1)
        right_depth = self.maxDepth(root.right, count + 1)

        return max(left_depth, right_depth)
    
    


sol = Solution()