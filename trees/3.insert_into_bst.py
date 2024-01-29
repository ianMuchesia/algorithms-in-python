from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            root = new_node
        
        def helper(root:Optional[TreeNode]):
            if val > root.val:
                if not root.right:
                    root.right = new_node
                else:
                    helper(root.right)
            else:
                if not root.left:
                    root.left = new_node
                else:
                    helper(root.left)
               
            
        
        helper(root)
        return root
                
            
    

sol = Solution()
node1 = TreeNode(4)
node1.left = TreeNode(2)
node1.left.left = TreeNode(1)
node1.left.right = TreeNode(3)
node1.right = TreeNode(7)
print(sol.searchBST(node1))