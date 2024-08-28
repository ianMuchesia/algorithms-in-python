class Solution:
    def isValid(self, s: str) -> bool:
        opening_map = {"(":")","[":"]","{":"}"}
        
        stack = []
        
        
        for i in  s:
            if i in opening_map:
                stack.append(i)
            else:
                if not len(stack): return False
                if stack[-1] in opening_map:
                    if opening_map[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
                    
                    
        return not len(stack)
                

                    
                
                
    
    
sol = Solution()
print(sol.isValid("(){}}{"))