from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not len(nums1) or not len(nums2):
            return []
        hashmap = dict()
        res = list()
        
        
        for i in nums1:
            if i not in hashmap:
                hashmap[i] = 1
                
        for i in nums2:
            if i in hashmap:
                if hashmap[i] == 1:
                    res.append(i)
                    hashmap[i] = 0
              
                    
        
        return res
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            if not len(nums1) or not len(nums2):
                return []
            
            res = list()
            hashmap = dict()
            
            for num in nums1:
                if num in hashmap:
                    hashmap[num] += 1
                else:
                    hashmap[num] =1
                    
            for num in nums2:
                if num in hashmap:
                    if hashmap[num] > 0:
                        res.append(num)
                        hashmap[num] -=1
                        
            return res
        
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        sortedArr1 = nums1.sort()
        sortedArr2 = nums2.sort()
        
        i = 0
        
        j= 0
        
        res1 = []
        
        res2 = []
        
        
        return sortedArr2
        # while i < len(sortedArr1) and j< len(sortedArr2):
            
        #     if sortedArr1[i] > sortedArr2[j]:
        #         res1.append(sortedArr1[i])
        #         i+=1
        #     elif sortedArr1[i] < sortedArr2[j]:
        #         res2.append(sortedArr2[j])
        #         j+=1
        #     else:
        #         j+=1
        #         i+=1
                
        
        # while i < len(sortedArr1):
        #     res1.append(sortedArr1[i])
        #     i+=1
            
        # while j< len(sortedArr2):
        #     res2.append(sortedArr2[j])
        #     j+=1
            
        
        # return [res1,res2]

                
                
        
        
sol = Solution()
print(sol.findDifference([1,2,3],[2,4,6]))
        