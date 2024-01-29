from typing import List
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) :
        # Create a defaultdict with default value as an empty list
        hash_map = defaultdict(list)

        
        
        # It returns pairs of index and value.
        for index,num in enumerate(nums):
            hash_map[num].append(index)
            
        degree = max([len(x) for x in hash_map.values()])
        
        result = len(nums)
        
        for indices in hash_map.values():
            if len(indices) == degree:
                result = min(result, indices[-1] - indices[0])
        
        return result + 1
        
    
    
sol = Solution()

print(sol.findShortestSubArray([1,2,2,3,1]))