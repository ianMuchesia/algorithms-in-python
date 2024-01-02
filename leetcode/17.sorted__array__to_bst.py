from typing import List, Optional

class TreeNode:
    def __init__(self,val,left=None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums)-1
        
        
        def helper(nums,start, end):
            
            if start > end:
                return None
            
            mid = (start + end)//2
            
            node = TreeNode(nums[mid])
            print(node.val)
            
            node.left  = helper( nums,start , mid-1)
            node.right = helper( nums,mid+1,end)
            
            return node
            
      
        
        return helper(nums,start, end)
            
            
            
    
    
sol = Solution()
sol.sortedArrayToBST([-10,-3,0,5,9]
)