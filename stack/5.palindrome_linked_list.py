from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack = []
        
        current = head
        
        while head:
            stack.append(head.val)
            head = head.next
            
        while current:
            if (current.val != stack.pop()):
                return False
            current = current.next
            
        return True
            
        
        
    
    
sol = Solution()
node1 = ListNode(1)
node1.next  =ListNode(2)
# node1.next.next = ListNode(2)
# node1.next.next.next = ListNode(1)
print(sol.isPalindrome(node1))