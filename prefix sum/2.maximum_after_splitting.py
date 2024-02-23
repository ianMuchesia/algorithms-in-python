class Solution:
    def maxScore(self, s: str) -> int:
        sum_of_one = 0
        
        s_arr  = list(s)
        for i in range(len(s_arr)):
            if s_arr[i] == "1":
                sum_of_one += 1
                s_arr[i] = sum_of_one
            
        print(s_arr)

        sum_of_zero = 0
        current_sum_of_one = 0
        
        maximum = float("-inf")
        
        for i in range(len(s_arr)):
            if s_arr[i] == "0":
                sum_of_zero +=1
            else:
                current_sum_of_one = sum_of_one - s_arr[i]
            current_sum = sum_of_zero + current_sum_of_one 
            print("currentsum: ",current_sum)
            maximum = max(maximum,current_sum)
            
        print(maximum)
                  

sol = Solution()
sol.maxScore("11101")