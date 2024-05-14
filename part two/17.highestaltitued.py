from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        maxTotal = float("-inf")
        print(max(-6,0))
        for num in gain:
            total += num
            print(total)
            maxTotal = max(maxTotal,total)
            
        return maxTotal if maxTotal > 0 else 0
    
    
    
sol = Solution()

print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))