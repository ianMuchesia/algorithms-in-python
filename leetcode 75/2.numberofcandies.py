from typing import List

class Solution:
  
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_in_candies = max(candies)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_in_candies:
                candies[i] = True
            else:
                candies[i] = False
        
        return candies
    
    
    
    
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_in_candies = max(candies)
        
        canHaveMaxCandies = list(map(lambda x: x + extraCandies >= max_in_candies, candies))
        
        return [candy + extraCandies >= max_in_candies for candy in candies]
        
        