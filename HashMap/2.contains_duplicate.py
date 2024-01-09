from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        start = 0
        end = k-1
        
        hashMap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashMap:
                diff = abs(hashMap[nums[i]] - i)
                if diff <= k:
                    return True
                else:
                    hashMap[nums[i]] = i
            else:
                hashMap[nums[i]] = i
        
        return False
    
    
    
    
sol = Solution()

print(sol.containsNearbyDuplicate([1,2,3,1], k=3))