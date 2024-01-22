from typing import Optional 
 
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
       
        node: TreeNode = root
        def helper(node:Optional[TreeNode]):
            if not node:
                return None
            node.left, node.right = node.right, node.left

            # Recursively invert the left and right subtrees
            print(node.val)
            helper(node.left)
            helper(node.right)

            return node

        # Start the inversion from the root
        return helper(root)
    def preOrder(self,root:TreeNode):
        #check if the current node is empty or null
        if root:
            
            print(root.val,"hey")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
                
    
    

node1 = TreeNode(val=4)
node2 = TreeNode(val=2)
node3 = TreeNode(val=1)
node4 = TreeNode(val=3)
node5 = TreeNode(val=7)
node6 = TreeNode(val=6)
node7 = TreeNode(val=9)


node1.left = node2
node2.left = node3
node2.right = node4
# node3.right = node5
node1.right = node5
node5.left = node6
node5.right = node7

sol = Solution()
print(sol.invertTree(node1))
sol.preOrder(sol.invertTree(node1))