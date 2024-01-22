from typing import Optional 
 
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        if not root.right and not root.left:
            return root.val == targetSum
       
     
        def helper(root:Optional[TreeNode], targetSum, total=0):
            if not root.right and not root.left:
                return root.val + total == targetSum
            
            
            
            left_side = helper(root.left, targetSum, total=total + root.val) if root.left else False
            right_side = helper(root.right,targetSum, total=total + root.val) if root.right else False
          
            return right_side  or left_side 
        
        return helper(root, targetSum)
            
    
    
    
# node1 = TreeNode(val=5)
# node2 = TreeNode(val=4)
# node3 = TreeNode(val=11)
# node4 = TreeNode(val=7)
# node5 = TreeNode(val=2)
# node6 = TreeNode(val=8)
# node7 = TreeNode(val=4)
# node8 = TreeNode(val=13)
# node9 = TreeNode(val=1)

# node1.left = node2
# node2.left = node3
# node3.left = node4
# node3.right = node5
# node1.right = node6
# node6.left = node8
# node6.right = node7
# node7.right = node9

node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.left.left = TreeNode(3)
node1.left.left.left = TreeNode(4)
node1.left.left.left.left = TreeNode(5)



# node1.right = TreeNode(3)
sol = Solution()
print(sol.hasPathSum(node1, 6))
