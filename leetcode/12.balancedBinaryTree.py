from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode], count:int = 0) -> bool:
        
        
        def helper(func,root):
            
            if not root:
                return count
        
            left = helper(root.left, count +1)
            right = helper(root.right, count + 1)
        
        
            return  func(left,right)
        
        
        def helper_balance(root):
            if not root:
                return True
            
            left_height = helper(max,root.left)
            right_height = helper(max, root.right)
            
            
            return abs(left_height-right_height)<= 0 and helper_balance(root.left) and helper_balance(root.right)
        
        return helper_balance(root)
    
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
            
         
        


bst = TreeNode(1)
bst.left = TreeNode(2)
bst.left.left = TreeNode(4)
bst.right = TreeNode(3)
bst.right.right = TreeNode(5)

sol =Solution()

print(sol.minDepth(bst))


