from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode], count:int = 0) -> bool:
        def height_of_tree(root):
            if root is None:
                return 0
            else:
                left_height = height_of_tree(root.left)
                right_height = height_of_tree(root.right)

        # Choose the maximum height between left and right subtrees
            return max(left_height, right_height) + 1
        
        return height_of_tree(root.right)
       
    
    def minDepth(self, root: Optional[TreeNode],count:int=0) -> int:
        
        def height_helper(root,func, count = 0):
            if not root:
               
                return count

            leftdepth = height_helper(root.left,func, count+1)
            rightdepth = height_helper(root.right,func, count+1)

            return func(leftdepth, rightdepth)
        
        
        minimum =  height_helper(root,min)
        maximum = height_helper(root,max)
         
        print(minimum,maximum)
        if minimum == 1:
            return maximum
        else:
            return minimum
            
         
        


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)

root.left.left.left = TreeNode(4)
root.right.right = TreeNode(3)

root.right.right.right = TreeNode(4)

sol =Solution()

print(sol.isBalanced(root))


