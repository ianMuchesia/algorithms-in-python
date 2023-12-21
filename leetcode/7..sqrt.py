from math import floor
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        if x == 1:
            return 1
        left = 0
        right = x
        
        found = False
      
        
        while not found:
            mid = (left + right)/2
           
            if (int(mid * mid)) == x:
                print(mid)
                return floor(mid)
            elif((mid * mid))>x:
                right = mid
            else:
                left = mid
                
        
        
        
solution = Solution()
print(solution.mySqrt(8))