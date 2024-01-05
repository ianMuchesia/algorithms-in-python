from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
      
        
        hashMap = {}

        count = 0
        for i in arr:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
                
            
        new = []
        
        for key, value in hashMap.items():
            new.append(value)
        
        return len(set(arr)) == len(set(new))
            
         
        
            
    
    
    
sol = Solution()
print(sol.uniqueOccurrences([1,2]))