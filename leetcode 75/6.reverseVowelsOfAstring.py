
class Solution:
    def reverseVowels(self, s: str) -> str:
        p = 0
        q = len(s)-1
        s_list = list(s)
        hashMap = {"a":"a","e":"e","i":"i","o":"o","u":"u","A":"A", "E":"E","I":"I","O":"O","U":"U"}
        
        while (p<q):
            if s_list[p] not in hashMap:
               p+=1
            if s_list[q] not in hashMap:
                q-=1
            if s_list[p] in hashMap and s_list[q] in hashMap:
                s_list[p],s_list[q] = s_list[q], s_list[p] 
                p+=1
                q-=1
                  
            
        return ''.join(s_list)
        
        
        
solution = Solution()
print(solution.reverseVowels("aA"))