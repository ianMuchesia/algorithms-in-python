from typing import List

def bubble_sort(nums:List[int]):
    
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
    
    return nums


print(bubble_sort([-6,20,8,-2,4]))