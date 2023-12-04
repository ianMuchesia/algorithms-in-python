def decimal_to_binary(num):
    if not num:
        return num
    stack = []
    while num > 0:
        remainder = num % 2
        num = num // 2
        #insert is inefficient, use append then reverse
        stack.insert(0,str(remainder))
    return (''.join(stack))


print(decimal_to_binary(242))
print(int(decimal_to_binary(56),2)==56)