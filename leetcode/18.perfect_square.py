class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        high = num // 2
        low = 0
        
        found = False
        
        while not found:
            midpoint = (high + low) //2
            
            current_square = midpoint * midpoint
            
            
            if current_square == num:
                return True
            elif current_square > num:
                high = midpoint
            else:
                low = midpoint
                
            if abs(high-low) <= 1:
                return False
                
sol = Solution()
print(sol.isPerfectSquare(4))