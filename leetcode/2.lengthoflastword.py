class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       
        return len(s.strip().split(" ")[-1])
        
        
        
solution = Solution()
print(solution.lengthOfLastWord("Hello, world "))


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the length of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length