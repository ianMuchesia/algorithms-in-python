from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        steps = gcd(len(str1),len(str2))
        prefix = str2[0:steps]
        
        for i in range(0,len(str2),steps):
            if prefix != str2[i:steps+i]:
                return ""
        
        
        for i in range(0,len(str1),steps):
            
            if prefix != str1[i:steps+i]:
                return ""
        
        print(prefix)
        return prefix
            
            
            
            
solution = Solution()
solution.gcdOfStrings("ABCABC","ABC")

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        # If str1 and str2 share a common prefix, that prefix is the answer
        return str1[:gcd(len(str1), len(str2))]
