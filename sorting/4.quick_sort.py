from typing import List

def quick_sort(nums:List[int])->List[int]:
    if len(nums) < 2:
        return nums
    pivot = nums[-1]
    
 
    
    left = [ num for num in nums[:-1] if num < pivot]
    right = [num for num in nums[:-1] if num > pivot]
    
    return [*quick_sort(left),pivot,*quick_sort(right)]


print(quick_sort([-6,8,4,20,-2]))