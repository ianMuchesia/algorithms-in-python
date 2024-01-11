class Solution:
    def reverseWords(self, s: str) -> str:
        
        stack = []
        
        for i in s:
            stack.append(i)
            
        result = []
        
        while len(stack):
            result.append(stack.pop())
        
        start = 0
       
        
        result_2 = "".join(result).split(" ")
        
        print(result_2)
        
        end = len(result_2) -1
        while start < end:
            result_2[start], result_2[end] = result_2[end], result_2[start]
            start += 1
            end -= 1
            
        print(" ".join(result_2))
        
        
sol = Solution()
sol.reverseWords("Let's take LeetCode contest")