from typing import List
arr = [ 3,5,6,7,8,11,13,14,15,17,18,20 ]


def binary_search(nums:List[int], target):
    right = len(nums) -1
    left = 0
    
    
    while right >= left:
        midpoint = (right + left) // 2
    
        
        if nums[midpoint] == target:
            return True
        elif nums[midpoint] > target:
            right = midpoint-1
        else:
            left = midpoint +1
       
    return False

def binary_revursive_search(nums:List[int], target):
    return recursive_search(nums,target,0,len(nums)-1)

def recursive_search(nums:List[int],target, left, right):
    if right < left:
        return False
    
    
    midpoint = (left+right)//2
    
    if nums[midpoint] == target:
        return True
    elif nums[midpoint] > target:
        return recursive_search(nums,target,left, midpoint -1)
    else:
        return recursive_search(nums,target,midpoint + 1,right)


print(binary_search(arr,20))
print(binary_revursive_search(arr,20))
