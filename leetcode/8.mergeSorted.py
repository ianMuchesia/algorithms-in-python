from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            for i in range(m,len(nums1)):
                nums1[i] = nums2[count]
                count+=1
        nums1.sort()
        print(nums1)
        
    def mergeEfficient(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        k = m+n-1
        
        while j>=0 and i>=0:
         
            if nums1[i]>nums2[j]:
                
                nums1[k] = nums1[i]
                i -= 1
                
            elif nums1[i] < nums2[j]:
            
                nums1[k] = nums2[j]
                j-=1
            else:
                
                nums1[k] = nums1[i]
                nums1[k-1] = nums1[i]
                k=k-1
                i-=1
                j-=1
           
            k-=1
            print(nums1)
            
        while j>=0:
            nums1[k] = nums2[j]
            k=-1
        print(nums1)
    
    
solution = Solution()
solution.mergeEfficient([0],0,[1],1)