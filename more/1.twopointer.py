from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            curr_diff = target - nums[i]
            
            if(curr_diff in hashmap):
                return [hashmap[curr_diff], i]
            else:
                hashmap[nums[i]] = i
    
    
sol = Solution()
print(sol.twoSum([3, 2, 4, 3, 7, 1, 5], 8))
            
        
