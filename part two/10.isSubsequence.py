class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        k = 0
        
        counter = 0
        
        while counter < len(t):
            if s[k] == t[counter]:
                k+=1
                
            if k >= len(s):
                return True
            
            counter += 1
            
        if  k < len(s):
            return False
    
    
    
sol = Solution()
print(sol.isSubsequence("acb","ahbgdc"))