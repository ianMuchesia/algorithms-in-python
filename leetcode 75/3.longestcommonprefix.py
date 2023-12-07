from typing import List

class Solution:
    def longestCommonPrefix(self, strs:List[str])->str:
        res=""
        for i in range(len(strs[0])):
            for s in strs:
               
                if i == len(s) or s[i] != strs[0][i]:
                    print(s)
                    return res
            res += strs[0][i]
        print(res)    
        return res
    
    



solution = Solution()



print(solution.longestCommonPrefix(["flower", "f", "flight"]))





class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()  # Sort the list of strings lexicographically
        prefix = ""
        
        for char in strs[0]:
            if not strs[-1].startswith(prefix + char):
                break
            prefix += char
        
        return prefix

solution = Solution()
