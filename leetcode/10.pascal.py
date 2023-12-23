from typing import List
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows == 1:
#             return [[1]]
#         arr = [[1]]
        
#         while len(arr) < numRows+1:
            
#             count = 0
#             temp = arr[-1]
#             new_arr = [1]
#             while count < len(temp):
#                 if (count+1) < len(temp):
#                     new_entry =temp[count] + temp[count+1]
#                     new_arr.append(new_entry)
#                 else:
#                     new_arr.append(1) 
#                 count+=1    
                
#             arr.append(new_arr)
        
#         print(arr[numRows])
#         return arr
        
# sol = Solution()
# sol.generate(5)


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [[1]]
        arr = [[1]]
        
        while len(arr) < rowIndex+1:
            
            count = 0
            temp = arr[-1]
            new_arr = [1]
            while count < len(temp):
                if (count+1) < len(temp):
                    new_entry =temp[count] + temp[count+1]
                    new_arr.append(new_entry)
                else:
                    new_arr.append(1) 
                count+=1    
                
            arr.append(new_arr)
        
        # print(arr)
        return arr[rowIndex]
    
    
sol = Solution()
print(sol.getRow(1))