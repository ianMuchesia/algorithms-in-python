
def product(num1,num2):
    if num2 == 0:
        return 0
    
    return num1  + product(num1,num2-1)


print(product(5,3))