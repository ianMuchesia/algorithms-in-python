from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        if len(flowerbed) < 2:
            if n < 2:
                return flowerbed[0] == 0
            else:
                return False
        
        if flowerbed[0] == 0 and flowerbed[1]==0:
            n-=1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n-=1
            flowerbed[-1] =1
        
        if n<1:
            return True
        
        for i in range(1,len(flowerbed)-1):
            if n<1:
                return True
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n-=1
                
        return False
                
                
    
    
    
solution = Solution()

print(solution.canPlaceFlowers([0],1))