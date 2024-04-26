class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
        
        p = len(s)-1
        
        arr = list(s)
        
        total = 0
        
        prev = 0
        
        while (p>=0):
            curr = hashmap[arr[p]]
            print(curr)
            
            if curr < prev:
                total = total - curr
            else:
                total = total + curr
               
                
           
            
            prev = curr
            
            p -= 1
        return total
    
    
sol = Solution()
print(sol.romanToInt("MCMXCIV"))
            
        
            
        
            