from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        fast = 1
        slow = 0
        
        largest = 0
       
        
        while fast < len(prices):
            if prices[fast] < prices[slow]:
               slow = fast
             
            else:
                temp = prices[fast] - prices[slow]
                if temp > largest: largest = temp
                
            
            fast+=1
            
        return largest
    
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))