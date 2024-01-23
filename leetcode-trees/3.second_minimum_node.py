from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        left_side = root.left.left if root.left.left else -1
        right_side = root.right.right if root.right.right else -1
        
        if left_side == -1:
            return root.right.val if right_side != -1 else -1
        
        if right_side == -1:
            return root.left.val if right_side != -1 else -1
        
        if left_side >= 0 and right_side>=0:
            return min(root.right.val, root.left.val)
            
            
        
        
        return 1
        
    

node1 = TreeNode(2)
node1.left = TreeNode(2)
node1.right = TreeNode(2)
# node1.right.left = TreeNode(5)
# node1.right.right =TreeNode(7)
        
sol = Solution()

print(sol.findSecondMinimumValue(node1))