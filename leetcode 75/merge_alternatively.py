class Solution:
    def mergeAlternatively(self, word1:str, word2:str)->str:
        first = 0
        second = 0 
        
        final = ""
        
        while first < len(word1) or second< len(word2):
           
            if first < len(word1) :
                final += word1[first]
                first+=1
            if second< len(word2):
                final+=word2[second]
                second+=1
            print(final)
        print(final)
            
            
            
solution = Solution()
solution.mergeAlternatively("abcd", "pq")
            