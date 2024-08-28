from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast = 0
        slow = 0
        
        while(fast < len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
              
          
             
                
            fast += 1
                
        print(nums)
        return nums
            
           
                
                    
                
            
      
      

sol = Solution()
sol.moveZeroes([4,2,4,0,0,3,0,5,1,0])
            
        