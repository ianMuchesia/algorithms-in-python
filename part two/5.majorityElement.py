from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                
        
        print(hashmap)
        k = 0
        maxVal = 0
        
        for key,value in hashmap.items():
            print(value)
            if value > maxVal:
                k = key
                maxVal = value
          
        print(k)  
        
        
    def boyerMooreVoting(self, nums:List[int])->int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        print(candidate)
        count = 0
        
        for num in nums:
            if num == candidate:
                count += 1
                
    
        if count > len(nums)//2:
            return candidate
        else :
            return -1
            
        
            
    
    
sol = Solution()
sol.majorityElement([2,2,1,1,1,2,2])
sol.boyerMooreVoting([2,2,1,1,1,2,2])