class Solution:
    def isHappy(self, n: int) -> bool:
        
        hashMap = {}
        
        def helperSquare(num:str):
            return int(num) * int(num)
        
        def findSquare(nums:[str]):
            total = map(helperSquare,nums)
            
            return list(total)
        
        def findTotal(nums:[int]):
            total = 0
            for num in nums:
                total += num
            
            return total
        
        nums = findSquare(list(str(n)))
        total = findTotal(nums)
        
        while total != 1:
            if total in hashMap:
                return False
            else:
                hashMap[total] = total
            
            nums = findSquare(list(str(total)))
            total = findTotal(nums)
            
        return True
            
    
sol = Solution()


print(sol.isHappy(19))