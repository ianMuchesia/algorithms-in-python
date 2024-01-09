from typing import List
A1 = [1,2,4,5,6,6,8,9]
A2 = [2,5,6,7,8,8,9]

def find_closest_num(A, target):
    min_diff = min_diff_left = min_diff_right = float("inf")
    
    low = 0
    
    high = len(A) -1
    
    closest_num = None
    
    #edge cases for empty list of list
    #with only one element
    
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    
    while low <= high:
        
        mid = (low + high) //2
        
        #to ensure we don not read beyond the bounds
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid+1] - target)
            
        if mid > 0:
            min_diff_left = abs(A[mid-1] - target)
            
            
        #check if the absolute values between left 
        #and right elements are smaller than any
        #seen prior
        
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
            
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid+1]
            
            
        #move the midpoint appropriately as it is done
        #via binary search
        if A[mid] < target:
            low = mid +1
        elif A[mid] > target:
            high = mid -1
            if high < 0:
                return A[mid]
        else:
            return A[mid]
    return closest_num


print(find_closest_num(A1, 11))
print(find_closest_num(A2, 4))



def my_closest_num(nums:List[int],target):
    left = 0
    right = len(nums)-1
    
    
    if len(nums) == 0:
        return None
    
    if len(nums) == 1:
        return nums[0]
    
    while right >= left:
        midpoint = (right + left) // 2
        left_min_diff = abs(nums[midpoint - 1] - target)
        right_min_diff = abs(nums[midpoint + 1] - target)
        
        
        if left_min_diff > right_min_diff:
            left = midpoint + 1
        else:
            right = midpoint -1

        
                
        
        
    
    