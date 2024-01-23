from typing import List


def merge_sort(nums:List[int])->List[int]:
    if len(nums)<2:return nums
    
    mid = len(nums)//2
    
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    
    return merge(merge_sort(left_arr),merge_sort(right_arr))
    
def merge(left_arr:List[int],right_arr:List[int]):
    sorted_arr = []
    while len(left_arr) and len(right_arr):
        if left_arr[0] <= right_arr[0]:
            sorted_arr.append(left_arr.pop(0))
        else:
            sorted_arr.append(right_arr.pop(0))
            
    return [*sorted_arr,*left_arr,*right_arr]


print(merge_sort([8,20,-2,4,6]))