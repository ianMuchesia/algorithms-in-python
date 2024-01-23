
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def helper(root:Optional[TreeNode]):
            res, stack = [], []
            curr = root
           
            while True:
                if curr != None:
                    stack.append(curr)
                    curr = curr.left
                elif stack:
                    curr = stack.pop()
                    res.append(curr.val)
                    curr = curr.right
                else:
                    break
            print(res)
            return res
        
        return helper(root)
               
           
           
                
                
                
                
                
                
    
    
node1 = TreeNode(10)
node1.right=TreeNode(15)
node1.left=TreeNode(5)
node1.left.right = TreeNode(7)
node1.left.left = TreeNode(3)

sol = Solution()
sol.inorderTraversal(node1)