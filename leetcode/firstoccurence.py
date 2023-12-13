class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        slow = 0
        
        length = len(needle)
        fast = 0
        
        while slow < len(haystack):
           
            if haystack[slow] == needle[0]:
                fast = slow + length
               
                if needle == haystack[slow:fast]:
                   
                    return slow
                # else:
                #     slow = fast 
            slow += 1
        return -1        
            
        
        
        
solution = Solution()


print(solution.strStr("mississippi","issip"))

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
