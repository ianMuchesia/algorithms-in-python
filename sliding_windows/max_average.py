from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        start = 0
        end = k
        current_total = sum(nums[start:end ])
        largest = current_total
        for i in range(end,len(nums)):
           
            current_total = current_total + nums[i]-nums[start]
             
            if current_total > largest:
                largest = current_total
            
            start+=1
                
    
        return largest/k
    
sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(sol.findMaxAverage(nums, k))