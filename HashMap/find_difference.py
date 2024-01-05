from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashMap_1, hashMap_2 = set(nums1), set(nums2)
        list_1, list_2 = set(),set()
        
        
        
        for num in nums1:
            if num not in hashMap_2:
                list_1.add(num)
                
        for num in nums2:
            if num not in hashMap_1:
                list_2.add(num)
        
        
      
      
        return [list(list_1),list(list_2)]
                
    
    
sol = Solution()
print(sol.findDifference([1,2,3,3],[1,1,2,2]))