class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        strings = "abcdefghijklmnopqrstuvwxyz"
        
        new_str=""
        for i in range(len(s)):
            new_str = new_str + str(strings.index(s[i]) + 1)
        
     
        current_total = 0
        
        def sum_digits(num:str):
            total = 0
            while int(num) > 0:
                rem = int(num) % 10
                total = total + rem
                num = int(num) // 10
            return total
        
        while k != 0:
            current_total = sum_digits(new_str)
            new_str = str(current_total)
            k-=1
        
            
        return current_total
        pass
        
        
sol = Solution()

print(sol.getLucky(s = "zbax",k = 2))