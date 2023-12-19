
from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        print(p.left)
        
        stack = [ p, q]
        
        while len(stack)>0:
            q1 = stack.pop()
            p1 = stack.pop()
            
            
         
            if (not q1 and p1) or (q1 and not p1):
                return False

            # Check values
            if q1 and p1 and q1.val != p1.val:
                return False
            
            if q1.left and p1.left:
                stack.append(p1.left)
                stack.append(q1.left)
            if q1.right and p1.right:
                stack.append(p1.right)
                stack.append(q1.right)
            
        
        return True
                
            
        
    def isSameTreeRecursive(self, p: Optional[TreeNode], q: Optional[TreeNode])->bool:
        
        
       
        if not p and not q:
            return True
        if not p or not q:
            return False
        print(p.val ,q.val)
        if p.val != q.val:
            return False
        
        return  self.isSameTreeRecursive(p.left,q.left) and  self.isSameTreeRecursive(p.right,q.right)
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        p = root.left
        q = root.right
        
        def innerfunc(p,q):
        
            if not p and not q:
                return True
            if not p or not q:
                return False
            print(p.val ,q.val)
            if p.val != q.val:
                return False
        
            return innerfunc(p.left,q.right) and innerfunc(p.right,q.left)
        
        return innerfunc(p,q)
        

            
    
        
        
        
solution = Solution()
node = TreeNode(1)
# node.left = TreeNode(None)
# node.right = TreeNode(3)

node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(solution.isSameTreeRecursive(node,node1))
print(solution.isSymmetric(root))