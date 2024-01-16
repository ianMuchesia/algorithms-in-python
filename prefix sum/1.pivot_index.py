from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
       
     
        current_total = sum(nums)
       
         
        if current_total == 0:return 0
            
        print(current_total)
        left_sum = 0
        right_sum = current_total    
        for i in range(len(nums)-1):
            if i == 0:
                left_sum = 0
            else:
                left_sum += nums[i-1]
            right_sum =current_total - (left_sum + nums[i])
            
            if left_sum == right_sum:
                return i
            
        return -1
            
            

            
       
        
    
 
 
 
   
sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))