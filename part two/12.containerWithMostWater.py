from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p = 0 
        q = len(height) - 1
        width = q
        
        area = 0
        
        
        
        while p < q:
            width = q - p
            currentArea = width * min(height[p], height[q])
            
            area = max(currentArea, area)
            
            
            if height[p] > height[q]:
                q -= 1
                
            else: 
                p += 1
                
        return area
    
    
    
    

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
            