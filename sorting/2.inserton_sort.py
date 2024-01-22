from typing import List
def insertion_sort(nums:List[int]):
    
    for i in range(1, len(nums)):
        number_to_insert = nums[i]
        sorted_element = i-1
        
        while sorted_element >= 0 and number_to_insert < nums[sorted_element]:
            nums[sorted_element +1] = nums[sorted_element]
            sorted_element -=1
        nums[sorted_element +1] = number_to_insert
        
            
        
        print(nums[sorted_element])

            
    return nums


print(insertion_sort([8,20,-2,4,-6])) 