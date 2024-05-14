from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total = 0
 
        for i in range(k):
            total += nums[i]

        avg = total/k
        print(total)
        maxAvg = avg
        for i in range(k,len(nums)):
            print(f"nums[i]: {nums[i]} nums[k-i]: {nums[i-k]}")
            total = total + nums[i] - nums[i-k]
            print(total)
            maxAvg = max(maxAvg, total/k)
            
            
        return maxAvg
    
    
sol = Solution()
print(sol.findMaxAverage([7,4,5,8,8,3,9,8,7,6],7))