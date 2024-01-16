
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 1:
            return [str(nums[0])]
        start = 0
        end = 0 
        output = []
      

        for i in range(1,len(nums)):
           
            if nums[i] - nums[end] > 1:
                print(nums[i])
                if end == start:
                    output.append(str(nums[end]))
                else:
                    new_string = f"{str(nums[start])}->{str(nums[end])}"
                
                    output.append(new_string)
                
                start=i
                
                
            
              
                 
            end += 1
             
             
        if end == start:
            output.append(str(nums[end]))
        else:
            new_string = f"{str(nums[start])}->{str(nums[end])}"
                
            output.append(new_string)       
        
        
                
        return output
        

sol = Solution()

print(sol.summaryRanges([0,2,3,4,6,8,9]))