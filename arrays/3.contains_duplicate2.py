from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                if (i-hashmap[nums[i]]) <= k:
                    return True
                else:
                    hashmap[nums[i]] = i
        return False
            
    
    
    
sol = Solution()
print(sol.containsNearbyDuplicate([1,0,1,1],1))

