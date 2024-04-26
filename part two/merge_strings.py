class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return word2 or word1
        
        p=q=0
        
        output = ""
        
        while p<len(word1) and q<len(word2):
            
            output += word1[p]
            
            output += word2[q]
            
            p += 1
            q += 1
            
        while p<len(word1):
            output += word1[p]
            p+=1
        while q<len(word2):
            output += word2[q]
            q+=1
        
        return output
            
    
    

sol = Solution()


print(sol.mergeAlternately("abcd","pq"))
    
    