from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        
        fast = 0
        slow = 0
        
        while fast < len(nums):
            if not nums[slow]:
                del nums[slow]
                nums.append(0)
            else:
                slow+=1
            fast += 1
     
                
        return nums
       
       
       
       
       
solution = Solution()

print(solution.moveZeroes([0,1,0,3,12]))


def moveZeroes(nums: List[int]) -> None:
    slow = 0
    fast = 0

    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1
