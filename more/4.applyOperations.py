from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        fast = 1
        slow = 0
        
        while(fast < len(nums)):
            if nums[fast] == nums[slow]:
                nums[slow] = nums[slow] * 2
                nums[fast] = 0
                
            fast += 1
            slow += 1
            
        fast = 0
        slow = 0
      
        while(fast < len(nums)):
          
            if nums[fast] != 0:
                if nums[slow] == 0:
                    nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
                
            fast += 1
            
            
        return nums
    
    


sol = Solution()

print(sol.applyOperations([1,2,2,1,1,0]))