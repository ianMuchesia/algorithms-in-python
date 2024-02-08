from typing import Optional,List
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]
        queue = [root]
        
        res = []
        
        while queue:
            temp = []
            total = 0
            for num in queue:
                total += num
                
            node = queue.pop(0)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return k == 0
        stack = [root]
        
        hashMap = {}
        
        while stack:
            node = stack.pop()
            
            if node.val in hashMap:
                return True
            else:
                hashMap[k - node.val] = node.val
                
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left) 
            
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        def helper(root,direction,prev=0):
            if root.direction:
                prev = root.val
                
            
        
                
                
                
            
sol = Solution()
node1 = TreeNode(3)
node1.left= TreeNode(9)
node1.right = TreeNode(20)
node1.right.left = TreeNode(15)
node1.right.right = TreeNode(7)


sol.averageOfLevels(node1)