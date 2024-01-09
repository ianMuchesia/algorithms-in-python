class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        start = 0
        end = 3
        count = 0
        while end < len(s):
            print(s[start:end])
            if len(set(s[start:end])) == 3:
                count += 1
            start += 1
            end += 1
            
        print(count)
        return count
            
        
        
  
  
      
sol = Solution()

sol.countGoodSubstrings("aababcabc")