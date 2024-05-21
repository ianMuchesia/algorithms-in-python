from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        right_sum = total_sum - nums[0]
        left_sum = 0
        
        for i in range(len(nums)):
            print(f"right sum: {right_sum} left_sum: {left_sum}")

            if right_sum == left_sum:
                return i
            right_sum -= nums[i+1] 
            left_sum += nums[i]
          
        return -1  
    
    
    
    
sol = Solution()
print(sol.pivotIndex([-1,-1,0,1,0,-1]))