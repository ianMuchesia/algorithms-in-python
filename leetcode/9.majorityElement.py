
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        
        for i in nums:
            if i in hashmap:
                hashmap[i] = hashmap[i]+1
            else:
                hashmap[i] = 1
        print(hashmap) 
        
        max_key = None
        max_value = float('-inf')
        
        for key , value in hashmap.items():
            print(key)
            if value>max_value:
                max_key = key
                max_value = value
        print(max_key)
        return max_key
    
    
        
    
    
sol = Solution()
sol.majorityElement([1,2,1])