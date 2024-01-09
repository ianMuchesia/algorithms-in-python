from typing import List
import collections


def find_max_sliding_window(nums:List[int], w:int):
    
    deque = []
    output = []
    
    largest = nums[0]
    for num in nums[:w]:
        
        if num > largest:
            
            while len(deque) >= 1:
                deque.pop()
           
            deque.append(num)
            largest = num
        else:
            deque.append(num)
            
    output.append(deque[0])
    
    start = 1
    end = w
    
    while end <= len(nums) -1:
        if nums[end] > deque[-1]:
            while  len(deque) and nums[end] > deque[-1]:
                deque.pop()
            deque.append(nums[end])
        else:
            deque.append(nums[end])
        
        output.append(deque[0])
            
        start+=1
        end+=1
            
            
    
        
        
        
        
    
    
    return output






#correct implementation


def maxSlidingWindow(nums:List[int],k:int)->List[int]:
    output = []
    q = collections.deque() #index
    left = 0
    right = 0
    
    while right > len(nums):
        while q and nums[q[-1]] < nums[right]:
            q.pop()
        q.append(right)
        
        #left value remove from window if it is out of bounds
        if left > q[0]:
            q.popleft()
            
        if right + left >= k:
            output.append(nums[q[0]])
            l+=1
            
        right+=1
            
    return output
        
        


def final_max_window_implementation(nums:List[int], w:int):
    deque = []
    output = []
    
    largest = nums[0]
    
    for i in range(0,w):    
        while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
           
        deque.append(i)
        
            
    output.append(nums[deque[0]])
    
    print(deque)
    start = 1
    end = w
    
    while end <= len(nums) -1:
       
        if deque and  start > deque[0]:
            deque.pop(0)
            
      
        while  len(deque) and nums[end] > nums[deque[-1]]:
                deque.pop()
        deque.append(end)
        
        
        
        output.append(nums[deque[0]])
            
        end+=1
        start+=1
    
    
    
    
    return output
    
        
        
print(final_max_window_implementation([1,3,-1,-3,5,3,6,7] , 3
))
