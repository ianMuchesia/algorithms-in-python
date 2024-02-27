from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p = l1
        q = l2
        
        res = ListNode(0)
        temp = res
        carry = 0
        while p and q:
            current_sum = p.val + q.val + carry
            if current_sum >= 10:
                current_sum = current_sum - 10
                carry = 1
            else:
                carry =0
            
            res.next = ListNode(current_sum)
            
            res = res.next
            p = p.next
            q = q.next
            
        while p:
            current_sum = p.val + carry
            if current_sum >= 10:
                current_sum = current_sum - 10
                carry = 1
            else:
                carry = 0
            res.next = ListNode(current_sum)
            res = res.next
            p = p.next 
            
        while q:
            current_sum = q.val + carry
            if current_sum >= 10:
                current_sum = current_sum - 10
                carry = 1
            else:
                carry = 0
            res.next = ListNode(current_sum)
            res = res.next
            q = q.next 
            
        if carry:
            res.next = ListNode(carry)
            
        return temp.next
            
        
        