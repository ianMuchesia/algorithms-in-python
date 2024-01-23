from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        
        if root.left.val != root.right.val:
            return False
        
        return self.isSymmetric(root.left) and self.isSymmetric(root.right)
        
        
        
        
        
        
        
# Create nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)

# Connect nodes to form the tree
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


sol = Solution()
print(sol.isSymmetric(node1))