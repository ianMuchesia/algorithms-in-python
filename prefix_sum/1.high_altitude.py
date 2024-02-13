from typing import List
def largestAltitude(self, gain: List[int]) -> int:
    largest = float("-inf")
    
    current_total = 0
    
    
    for i in range(len(gain)):
        current_total += gain[i]
        largest = max(largest,current_total)
        
        
    return largest

def pivotIndex( nums: List[int]) -> int:
    
    current_sum = 0
    
    total = sum(nums)
    
    for i in range(1,len(nums)-1):
        current_sum +=[i-1]
        
        current_sub = total - nums[i] - current_sum
        
        if current_sub == current_sum:
            return i
        
    return -1
def minStartValue(nums: List[int]) -> int:
    
    total = 0
    res = []    
    for i in range(len(nums)):
        total += nums[i]
        res.append(total)
        
    print(res)
    print(min(res))
    print(1-min(res))
    return 1


minStartValue([2,3,5,-5,-1])
