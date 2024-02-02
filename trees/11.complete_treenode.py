from typing import Optional,List
 
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        def countNodes(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            arr = []
            
            def helper(root:Optional[TreeNode]):
                if not root:
                    return 0
              
                
                left = helper(root.left)
                right = helper(root.right)
                
                print("left ",left," right: ",right," total",left + right)
                return 1 + left + right
            return helper(root)
        
        def minDepth(self, root: Optional[TreeNode],count:int=0) -> int:
            if not root:
                return 0
            
            def helper(root:Optional[TreeNode]):
               
                
                left = helper(root.left) if root.left else 0
                right = helper(root.right) if root.right else 0
                
                if left == 0:
                    return right
                if right == 0:
                    return left
                return 1 + min(left,right)
            return helper(root)
        
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            
            queue:[TreeNode] = [root]
            res = [[root.val]]
            while queue:
                node = queue.pop(0)
                print(node.val)
                stack = []
                if node.left and node.right:
                    stack.append(node.left.val)
                    stack.append(node.right.val)
                    queue.append(node.left)
                    queue.append(node.right)

                elif node.left:
                    queue.append(node.left)
                    stack.append(node.left.val)
                elif node.right:
                    queue.append(node.right)
                    stack.append(node.right.val)
                res.append(stack)

            print(res)
                    
                          
            


        
        
sol = Solution()
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.left.left = TreeNode(4)
node1.left.right = TreeNode(5)
node1.right = TreeNode(3)
node1.right.left = TreeNode(6)
# print(sol.countNodes(node1))
sol.levelOrder(node1)