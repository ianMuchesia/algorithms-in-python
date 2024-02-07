from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        res = []
    
        def traverse_root1(node:Optional[TreeNode]):
            
            if not node:
                return 
            if not node.left and not node.right:
                res.append(node.val)
                return
            traverse_root1(node.left)
            traverse_root1(node.right)    
            
        traverse_root1(root1)
        
        stack = [root2]
        
        while stack:
            node = stack.pop()
            
            if not node.left and not node.right:
                if node.val != res.pop(): return False
                
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return True
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isIdentical(node1:Optional[TreeNode],node2:Optional[TreeNode]):
            if not node2 and not node1:
                return True
            if not node2 or not node1:
                return False
            
            return node1.val == node2.val and isIdentical(node1.left,node2.left) and isIdentical(node1.right,node2.right)
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.val == subRoot.val:
                if isIdentical(node,subRoot):
                    return True
            if not node.left and not node.right:
                continue
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
                
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        unique = set()
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            unique.add(node.val)
            
            if len(unique)>1:
                return False
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
        return True            
            
        
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # unique = set()
        
        # def helper(root:Optional[TreeNode]):
        #     if root:
        #         unique.add(root.val)
        #         helper(root.left)
        #         helper(root.right)
        
        # helper(root)
        
        # return len(unique) == 1
        # unique = set()
        # stack = [root]
        
        # while stack:
        #     node = stack.pop()
            
        #     unique.add(node.val)
            
        #     if len(unique)>1:
        #         return False
            
        #     if node.right:
        #         stack.append(node.right)
                
        #     if node.left:
        #         stack.append(node.left)
        # return True              
        def helper(node: Optional[TreeNode], target: int) -> bool:
            if not node:
                return True
            return node.val == target and helper(node.left, target) and helper(node.right, target)

        if not root:
            return True
        return helper(root, root.val)   

               
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def helper(root:Optional[TreeNode],v,count=0):
            if not root:
                return count
              
            if root.left == v or root.right == v:
                return count + 1
            
            left = helper(root.left,v,count+1)
            right = helper(root.right,v,count+1) 
            
            return max(left,right)
        
            
                 
            
    
sol = Solution()
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)


node2 = TreeNode(1)
node2.left = TreeNode(3)
node2.right = TreeNode(2)
print(sol.leafSimilar(node1,node2))
