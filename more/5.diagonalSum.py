from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        current_sum = 0
        midpoint = n //2
        for i in range(len(mat)):
            if(midpoint) == i:
                if n % 2:
                    current_sum += mat[i][i]
                # else:
                #     current_sum += mat[i][i] + mat[i][n-(i+1)]
                    # current_sum += mat[i][i] + mat[i][n-(i+1)]
                break;
            current_sum += mat[i][i] + mat[i][n-(i+1)]
            print(current_sum)
          
        
        print(current_sum)
        
        steps = 1
        midpoint += 1
        while steps < midpoint:
            current_sum += mat[midpoint][steps-1] + mat[midpoint][steps+1] 
            print("this is current sum",mat[midpoint])
            steps += 1
            
        
        
        print(current_sum)
        
        return current_sum
    
    
    
    
    

sol = Solution()

sol.diagonalSum( [[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]])
        