from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashmap = {}
        res = []
        def helper(root:Optional[TreeNode]):
            if root:
                if root.val in hashmap:
                    hashmap[root.val] += 1
                   
                else:
                    hashmap[root.val] = 1
                helper(root.left)
                helper(root.right)
        helper(root)
        print(hashmap)
        maxNum = 0
        for key,value in hashmap.items():
            maxNum = max(maxNum,value)
        
        for key,value in hashmap.items():
            if value == maxNum:
                res.append(key)
        return res
    
    
    
    
sol = Solution()
# Example 1:
node1 = TreeNode(1)
node1.right = TreeNode(2)
node1.left = TreeNode(2)
sol.findMode(node1)