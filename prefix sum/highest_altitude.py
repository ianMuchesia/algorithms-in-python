from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        alt = [0]
        largest = 0
        current_sum = 0
        for i in range(len(gain)):
            current_sum += gain[i]
            
            if current_sum > largest:
                largest = current_sum
            
        return largest
            
            
            
      
    
sol = Solution()
print(sol.largestAltitude([-5,1,5,0,-7]))