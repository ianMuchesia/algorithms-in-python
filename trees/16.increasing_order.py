from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        stack = []
        curr = root
        
        trav = TreeNode(curr.val)
        res = trav
        
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                node = stack.pop()
                print(node.val)
                trav.right = TreeNode(node.val)
                trav = trav.right
                curr =node.right
               
            else:
                break
            
        return res.right
                
                
                
                




sol = Solution()
node1 = TreeNode(5)
node1.left = TreeNode(3)
node1.left.left = TreeNode(2)
node1.left.right = TreeNode(4)
node1.left.left.left = TreeNode(1)
node1.right = TreeNode(6)
node1.right.right = TreeNode(8)
node1.right.right.left = TreeNode(7)
node1.right.right.right = TreeNode(9)
sol.increasingBST(node1)