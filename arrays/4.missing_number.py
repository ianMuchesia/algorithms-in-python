from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if (i+1) not in nums:
              
        #         print(i+1)
        #         return i+1
            
        total = sum(nums)
        print(total)
        
        current_total = 0
        for i in range(1,len(nums)+1):
            current_total += i
        
        
        return abs(total - current_total)
            
    
sol = Solution()
sol.missingNumber([1,0,3])