from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        counter = 0
        for num in nums:
           
            complement = k  - num
          
            if complement in hashmap:
                del hashmap[complement]
                counter += 1
            
                
            else:
               
                hashmap[num] = 1
        return counter
          
          
          
          
    
    
sol = Solution()
print(sol.maxOperations([3,1,3,4,3],6))
            
            
            