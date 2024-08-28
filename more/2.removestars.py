class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for letter in s:
            if(letter == "*"):
                stack.pop()
            else:
                stack.append(letter)
                
        result = ("".join(stack))
        
        return result
        
        
sol = Solution()
print(sol.removeStars("leet**cod*e"))