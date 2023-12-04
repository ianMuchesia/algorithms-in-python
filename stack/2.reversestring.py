def reverse_string(word):
    if not word:
        return word
    stack = []
    
    for w in word:
        stack.insert(0,w)
       
    print(stack)
    return ''.join(stack)
    
print(reverse_string("hello"))