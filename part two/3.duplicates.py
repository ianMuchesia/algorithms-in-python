from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        
        
        for i in range(1,len(nums)):
            if nums[i] > nums[p]:
                p += 1
                nums[p] = nums[i]
                
        print(p)
        return p
            
            
            
            
            
                
            
            
    
    
sol = Solution()

sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])