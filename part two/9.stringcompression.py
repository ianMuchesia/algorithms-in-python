from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        output = []
        count = 1
        
        for i in range(1,len(chars)):
            if prev != chars[i]:
                output.append(prev)
                if count > 1:
                   output.append(str(count))
                
                prev = chars[i]
                count = 1
            else:
                count += 1
        
       
        
        output.append(prev)
        if count > 1:
            output.append(str(count))
        returnln = ''.join(output)
        
        for i in range(len(returnln)):
            chars[i] = returnln[i]
            
        for i in range(len(chars)-len(returnln)):
            chars = chars[:-1]
            
        return len(chars)
            
            
    
sol = Solution()
print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]
))
        