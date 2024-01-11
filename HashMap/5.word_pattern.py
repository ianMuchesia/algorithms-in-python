class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
      p = 0
      q = 0
      hashmap = {}
       
      s_arr = s.split(" ")
      
      while p < len(pattern) and q < len(s_arr):
         if pattern[p] not in hashmap:
            if s_arr[q] in hashmap.values():
               return False
            hashmap[pattern[p]] = s_arr[q]
            
           
         else:
            if hashmap[pattern[p]] != s_arr[q]:
               return False
            
         p+=1
         q+=1
         
      print(hashmap)
      if p < len(pattern) or q < len(s_arr):
         return False
      
      return True        
           
           
                
    
    
    
sol = Solution()

print(sol.wordPattern("abc","b c a"))