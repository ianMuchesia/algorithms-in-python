class Solution:
    def countBinarySubstrings(self, s:str)->int:
        
        last = -1
        total = 0
        
        count = 0 
        
        lastcount = 0
        
        for i in s:
            if last != i:
                total += min(count,lastcount)
                
                lastcount = count
                count = 1
                last = i
            else:
                count+=1
        total += min(count,lastcount)
        
        return total
    
    
sol = Solution()
print(sol.countBinarySubstrings("01001010101001101101"))