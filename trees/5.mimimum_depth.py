from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
       def minDepth(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            def helper(root:Optional[TreeNode],count=0):
                if not root:
                    return 0
                left = helper(root.left)
                right = helper(root.right)
                
                if left == 0:
                    return right + 1
                if right == 0:
                    return left + 1
                return min(left,right) + 1
            
            return helper(root)
                
            
            

sol = Solution()
node1 = TreeNode(3)
node1.right = TreeNode(9)
node1.right.right = TreeNode(20)
node1.right.right.right = TreeNode(15)
node1.right.right.right.right = TreeNode(7)
print(sol.minDepth(node1))