from typing import List

def max_sub_array(nums:List[int]):
    maxSub = nums[0]
    
    current = 0
    
    for i in range(1, len(nums)):
        if current < 0:
            current = 0
            
        current += nums[i]
        
        if current > maxSub:
            maxSub = current
            
        
    return maxSub
print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))