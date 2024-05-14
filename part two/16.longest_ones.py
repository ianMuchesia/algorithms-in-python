
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        
        
        for right in range(len(nums)):
            #if we encounter a 0 then we decrement K
            if nums[right] == 0:
                k-=1
            
            #else do no changes to k
            
            #if k<0 then we need to move to the left part of the window
            #to try and remove extra zeros
            
            
            if k<0:
                #if left one was zero then we adjust k
                if nums[left] == 0:
                    k+=1
                left += 1
                    
            # regardless of whether we had a 1 or a 0 we can move left side by 1
           # if we keep seeing 1's the window still keeps moving as-is      
            
        return right - left + 1