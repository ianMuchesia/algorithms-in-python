from typing import List


def insertion_sort(nums:List[int])->List[int]:
    
    for i in range(1, len(nums)):
        num_to_insert = nums[i]
        
        sorted_element_index = i-1
        
        while(sorted_element_index >= 0 and nums[sorted_element_index]>num_to_insert):
            
            nums[sorted_element_index +1] = nums[sorted_element_index]
            sorted_element_index -= 1
        print(nums)
        nums[sorted_element_index +1] = num_to_insert
    return nums



print(insertion_sort([1,8,-2,-6,4,]))