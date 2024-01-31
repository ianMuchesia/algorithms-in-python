from typing import Optional,List
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root:Optional[TreeNode]):
            if root:
                helper(root.left)
                print(root.val)
                helper(root.right)
        
        stack = []
        res = []
        current = root
      
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                curr = stack.pop()
                res.append(curr.val)
                current = curr.right
            else:
                print(res)
                return res
                
                
        
        
                
            
                       
        return []
                
                

sol = Solution()
node1 = TreeNode(3)
node1.left = TreeNode(2)
node1.left.left = TreeNode(1)
node1.left.right = TreeNode(5)
node1.right = TreeNode(15)
sol.inorderTraversal(node1)
