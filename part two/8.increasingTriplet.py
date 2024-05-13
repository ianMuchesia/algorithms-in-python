from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    
    
    
    

sol = Solution()
print(sol.increasingTriplet([20,100,10,12,5]))