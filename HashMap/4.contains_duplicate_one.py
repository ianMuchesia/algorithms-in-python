from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #hashmap is more efficient
        return len(set(nums)) != len(nums)
    
    
        