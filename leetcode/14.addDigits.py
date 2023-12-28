class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        
        rem = num % 9
        
        if rem == 0:
            return 9
        
        return rem
     
        
sol = Solution()