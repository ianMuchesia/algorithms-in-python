from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            
            def helper(root:Optional[TreeNode]):
                if root:
                    print(root.val)
                    helper(root.left)
                    helper(root.right)
                    
                    
            return helper(root)
                    
                    
                
                
                
            
            
                
            
    

sol = Solution()
node1 = TreeNode(1)
node1.left = TreeNode(0)
node1.left.left = TreeNode(0)
node1.left.right = TreeNode(1)
node1.right = TreeNode(1)
node1.right.left = TreeNode(1)
node1.right.right = TreeNode(1)
print(sol.sumRootToLeaf(node1))