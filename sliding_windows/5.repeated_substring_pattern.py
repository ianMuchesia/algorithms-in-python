class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        if len(s) == 1 or (len(s) == 2 and s[0] != s[1]):
            return False
        
        
        window = []
        
        window.append(s[0])
        
        count = 1
        
        while s[0] != s[count] and count<len(s):
            window.append(s[count])
            print(s[count])
            count += 1
        
        if count == len(s):
            return False
        
        
        end = count
        
        print(window)
        
        start = 0
        
        for i in range(end,len(s)):
            if start == end:
                start = 0
            if s[i] != window[start]:
                return False
            
            start += 1
        
        if s[-1] != window[-1]:
            return False
        return True
            
            
       
                
        
        
        
        
sol = Solution()
print(sol.repeatedSubstringPattern("abab"))