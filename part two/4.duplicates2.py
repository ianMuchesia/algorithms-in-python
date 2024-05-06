from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        q = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[k]:
               k = k+1
               nums[k] = nums[i]
               q = 0
            else: 
                q = q + 1
                if(q<2):
                    k = k+1
                    
                    nums[k] = nums[i]
                
        
        print(nums)
               
                    
                
        
        
sol = Solution()

sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])