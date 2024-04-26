

class Solution:
    def isPalindrome(self,x:int)->bool:
        arr = list(str(x))
        
        i = 0
        k = len(arr)-1

        while (i<k):
            if arr[i] != arr[k]:
                return False
            else:
                i=i+1
                k=k-1
                    
        return True
    
    
sol = Solution()
print(sol.isPalindrome(121))