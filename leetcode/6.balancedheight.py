from typing import Optional,List
from math import ceil
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        
        left_side = self.isBalanced(root.left)
        right_side = self.isBalanced(root.right)
        
        return (right_side+1) == (left_side+1) or abs((right_side+1)-(left_side+1)) <= 1
        
        
        
        
solution = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(solution.isBalanced(root))