from typing import Optional,List
 
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode],q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        
        
        return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root:Optional[TreeNode]):
            if root:
        
                root.left, root.right = root.right,root.left
                helper(root.left)
                helper(root.right)
        helper(root)
        return root
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(p:Optional[TreeNode],q:Optional[TreeNode]):
            if not p and not q: return True
            if not p or not q: return False
            
            if p.val != q.val:
                return False
            return (helper(p.left,q.right) and helper(p.right,q.left))
            
        return helper(root.left,root.right)
    
    def maxDepth(self, root: Optional[TreeNode], count = 0) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left,count=count+1)
        right = self.maxDepth(root.right,count=count+1)
        
        return 1 + max(right,left)
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: 
        
        node = TreeNode
        def helper(root:Optional[TreeNode],nums:List[int]): 
            if len(nums) < 1:
                return None
        
            midpoint = len(nums)//2
            
            node = TreeNode(nums[midpoint])
            
            node.left = helper(nums[:midpoint])
            node.right = helper(nums[midpoint:]) 
            
            
            return node
            
            
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def helper(root:Optional[TreeNode],isLeft:bool=False,total=0):
            if not root.left and not root.right:
                return root.val if isLeft else 0
            
            
            
            left =  helper(root.left,True) if root.left else 0
            right = helper(root.right,False) if root.right else 0
            
            return left + right
           
            
        return helper(root)
    
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []
        def helper(root:Optional[TreeNode],string:str):
              
                if not root.right and not root.left:
                    arr.append(string + str(root.val))
                    return string + str(root.val)
                
                left = helper(root.left, string=string+f"{root.val}->") if root.left else ""
                right = helper(root.right, string=string+f"{root.val}->") if root.right else "" 
                return f"{left}, {right}"
                    
            
            
                   
        helper(root,"")
        return arr
    
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        string = "abcdefghijklmnopqrstuvwsyz"
        res=""
        def helper(root:Optional[TreeNode],stringHelper:str="",count=0,minNumber=float('inf')):
            nonlocal res
            if not root:
                return
            
            if not root.right and not root.left:
               
                count = count + root.val
                stringHelper +=str(root.val)
                print(minNumber)
                if count < minNumber:
                    
                    res = ""
                    for s in stringHelper:
                   
                        res += string[int(s)]
                    
                    minNumber = count
                                                  
                return 
            
            helper(root.left,stringHelper=stringHelper+f"{root.val}",count=count+root.val,minNumber=min(minNumber, count))
            helper(root.right,stringHelper=stringHelper+f"{root.val}",count =count+root.val,minNumber=min(minNumber, count))
            
        helper(root)
        return res

       


        

 
                
        
        

    
    

        


        
sol = Solution()
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.left.left = TreeNode(4)
node1.left.right = TreeNode(5)
node1.right = TreeNode(3)
node1.right.left = TreeNode(10)

print(sol.sumOfLeftLeaves(node1))

treenode = TreeNode(1)
treenode.left = TreeNode(2)
treenode.left.right = TreeNode(5)
treenode.right = TreeNode(3)



print(sol.binaryTreePaths(treenode))

small = TreeNode(0)
small.left = TreeNode(1)
small.left.left = TreeNode(3)
small.left.right = TreeNode(4)
small.right = TreeNode(2)
small.right.left = TreeNode(3)
small.right.right = TreeNode(4)

print(sol.smallestFromLeaf(small))