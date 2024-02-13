from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(root:Optional[TreeNode],val:int):
            if not root.left and not root.right:
                return root.val
            
          
            left = helper(root.left, root.val)
            
            right = helper(root.left,root.val)
            
            return left and right if root.val == 3 else left or right
        
        return helper(root,root.val)
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        def helper(root:Optional[TreeNode],string):
            if not root:
                res.append(string)
                return
            if not root.left and not root.right:
                total_str = string + str(root.val)
                res.append(total_str)
                return
            
            helper(root.left, string=string+str(root.val))
            helper(root.right, string=string+str(root.val))
        helper(root,"")
        
        total = 0
        for r in res:
            total += int(r,2)
        return total
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        
        def helper(root:Optional[TreeNode],low:int,high:int):
            nonlocal res
            if root:
                if root.val <= high and root.val >= low:
                    res += root.val
                
                if root.left: helper(root.left,low,high)
                if root.right: helper(root.righ,low,high)
                
        helper(root,low,high)
        return res
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        diff = float("inf")
        prev = float("-inf")
        def helper(root:Optional[TreeNode]):
            nonlocal diff,prev
            if root:                
                helper(root.left)
                
                if abs(root.val - prev) < diff:
                    diff = abs(root.val - prev)
                prev  = root.val
                helper(root.right)
                
        helper(root)
        return diff
    
    
         
                
                
                
                
                
            

                    

        
            
    
