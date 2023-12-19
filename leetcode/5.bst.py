from typing import Optional,List
from math import ceil
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        midpoint = ceil(len(nums)/2)-1
        
        tree = TreeNode(val=nums[midpoint])
        
        
        return tree and self.insertionNode(tree,nums)
        
        
    def insertionNode(self, tree:TreeNode,nums):
        
        if len(nums)!=0:
            num = nums[-1]
            
            if num == tree.val:
                nums.pop()
                num = nums[-1]
            if num > tree.val:
                if not tree.right:
                    tree.right = TreeNode(val=nums.pop())
                else:
                    self.insertionNode(tree.right,nums)
            else:
                if not tree.left:
                    tree.left =TreeNode(val=nums.pop())
                else:
                    self.insertionNode(tree.left,nums)
                    
        
    def inOrder(self, root:TreeNode):
        if root:
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)
            
            
        
        
        
        
        
        
        
        
        
        
solution = Solution()
print(solution.sortedArrayToBST([-10,-3,0,5,9]))
# solution.inOrder()