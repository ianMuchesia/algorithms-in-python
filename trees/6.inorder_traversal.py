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
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned:
            return None
        if cloned.val == target.val:
            return cloned
        
        return self.getTargetCopy(original,cloned.left,target) or self.getTargetCopy(original,cloned.right,target)
        
        
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root1,root2,new_root):
            
            if not root1 and not root2:
                return None
            
            if not root1:
                new_root = TreeNode(root2.val)
            elif not root2:
                new_root = TreeNode(root1.val)
            else:
                new_root = TreeNode(root1.val + root2.val)
            print(new_root.val)
         
            new_root.left = helper(root1.left,root2.left,new_root.left)

           
            new_root.right = helper(root1.right,root2.right,new_root.right)
            
            return new_root

        return helper(root1,root2,None)
            
            
            

          
                
        
        
                
            
    
                

sol = Solution()
node1 = TreeNode(1)
node1.left = TreeNode(3)
node1.left.left = TreeNode(5)
# node1.left.right = TreeNode(5)
node1.right = TreeNode(2)


node2 = TreeNode(2)
node2.left = TreeNode(1)

node2.left.right = TreeNode(4)
node2.right = TreeNode(3)
node2.right.right = TreeNode(7)

sol.mergeTrees(node1,node2)
