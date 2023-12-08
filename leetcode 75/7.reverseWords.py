class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split()
        
        p = 0
        q = len(arr)-1
        
        while(p<q):
            arr[p],arr[q] = arr[q], arr[p]
            p+=1
            q-=1
        return ' '.join(arr)
    
    
    
    
    
solution = Solution()

print(solution.reverseWords("the sky is blue"))