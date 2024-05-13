from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        
        slow  = 0
        
        fast = 0
    
        
        while fast < len(nums):
            
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                
            fast += 1
            
        print(slow)
        while slow< len(nums):
            nums[slow] = 0
            slow +=1
        return nums
            
    
    
sol = Solution()
print(sol.moveZeroes( [0,1,0,3,12]))