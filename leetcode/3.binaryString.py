class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a,2)
        decimal_b = int(b,2)
        sum_decimal = decimal_a + decimal_b
        return (str(bin(sum_decimal)[2:]))
        
        
solution = Solution()
print(solution.addBinary("11","1"))