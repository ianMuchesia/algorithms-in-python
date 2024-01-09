from typing import List
arr = [ 1,6,5,4,3,2,1]


def find_bitonic_peak(nums:List[int]):
    
    left = 0
    
    right = len(nums)
    
    while right >= left:
        mid = (left + right)//2
      
        
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid -1]:
            return nums[mid]
        elif nums[mid] > nums[mid + 1]:
            right = mid -1
        else:
            left = mid + 1
    
    return None

print(find_bitonic_peak([5, 4, 3, 2, 1]))
        
        