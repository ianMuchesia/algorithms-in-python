from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        def helper(root:Optional[TreeNode]):
            if not root:
                return None
            if val == root.val:
                return root
            if val > root.val:
                return helper(root.right)
            else:
                return helper(root.left)
        return helper(root)
                
            
    

sol = Solution()
node1 = TreeNode(4)
node1.left = TreeNode(2)
node1.left.left = TreeNode(1)
node1.left.right = TreeNode(3)
node1.right = TreeNode(7)
print(sol.searchBST(node1))