class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVowels = float("-inf")
       
        vowelSet = {"a", "e", "i", "o","u"}

        currentCount = 0
        for i in range(k):
            if s[i] in vowelSet:
                currentCount += 1
        
        maxVowels = currentCount
        
        for i in range(k,len(s)):
            if s[i-k] in vowelSet:
                currentCount -=1
            if s[i] in vowelSet:
                currentCount += 1
            
            maxVowels = max(maxVowels, currentCount)
            
        return maxVowels
           
                
            
            
        
    
    
    
sol = Solution()
print(sol.maxVowels("aeiou",2))
