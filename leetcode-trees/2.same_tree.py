from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        
        
    
    


node1 = TreeNode(10)
node1.right=TreeNode(15)
node1.left=TreeNode(5)
node1.left.right = TreeNode(7)
node1.left.left = TreeNode(3)


node2 = TreeNode(10)
node2.right=TreeNode(15)
node2.left=TreeNode(5)
node2.left.right = TreeNode(7)
node2.left.left = TreeNode(3)

sol = Solution()
print(sol.isSameTree(node1,node2))