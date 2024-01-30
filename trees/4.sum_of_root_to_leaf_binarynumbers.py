from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            
            def helper(root:Optional[TreeNode],s:str,total=0):
                if not root:
                    print(s)
                    return int(s,2)
                
                
                s += str(root.val)
                
                if not root.left and not root.right:
                    return int(s,2)
                
                
               
                left = helper(root.left,s,total)
                right = helper(root.right,s,total)
                
       
                return left + right
                
                
                
                
              
              
                    
                    
            return helper(root,"")
                    
                    
                
                
                
            
            
                
            
    

sol = Solution()
node1 = TreeNode(1)
node1.left = TreeNode(0)
node1.left.left = TreeNode(0)
node1.left.right = TreeNode(1)
node1.right = TreeNode(1)
node1.right.left = TreeNode(0)
node1.right.right = TreeNode(1)
print(sol.sumRootToLeaf(node1))