from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        fast = 1
        slow = 0
        
        largest = 0
        max_array = []
       
        
        while fast < len(prices):
            if prices[fast] < prices[slow]:
                slow = fast
            else:
                if fast + 1 < len(prices):
                    if prices[fast+1] < prices[fast]:
                        largest += prices[fast] - prices[slow]
                        slow = fast
            fast += 1
            
        return largest
    
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))