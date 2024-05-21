from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr:
            return True
        hashmap = dict()
        
        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                
        hashtable = dict()
        for key,value in hashmap.items():
            if value in hashtable:
                return False
            else:
                hashtable[value] = 1
                
        return True
            
     
        
        
        
sol = Solution()
print(sol.uniqueOccurrences([-4,3,3]))