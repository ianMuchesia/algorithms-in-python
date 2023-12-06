from main import Node


def is_palindrome_string(node):
    s = ""
    p = node
    
    while p:
        s+=p.data
        p = p.next
    
    return s == s[::1]


def is_palindrome_stack(node):
    stack = []
    p = node
    
    while p:
        stack.append(p.data)
        p = p.next
    
    p = node
    
    while p:
        data = stack.pop()
        if data != p.data:
            return False
        p = p.next
        
    return True    



def is_palindrome(self):
  if self.head:
    p = self.head 
    q = self.head 
    prev = []
    
    i = 0
    while q:
      prev.append(q)
      q = q.next
      i += 1
    q = prev[i-1]

    count = 1

    while count <= i//2 + 1:
      if prev[-count].data != p.data:
        return False
      p = p.next
      count += 1
    return True
  else:
    return True
    