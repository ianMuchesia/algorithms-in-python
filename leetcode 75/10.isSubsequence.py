class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p =0
        q=0
        
        while p<len(t) and q<(len(s)):
            if t[p] == s[q]:
                q+=1
            p+=1
            
       
        return q == len(s)
            
                
            
        
        
solution = Solution()

print(solution.isSubsequence("abc","ahbgdc"))