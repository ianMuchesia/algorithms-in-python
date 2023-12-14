def recursive_func(n):
    counter = 1
    
    if n==1:
        print("last counter")
    
    recursive_func(n-1)
    counter+=1
    print(counter)
    
recursive_func(5)