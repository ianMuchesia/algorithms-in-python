def recursive_func(n,counter=1):
  
    
    if n==1:
        print("last counter")
    else:

        recursive_func(n-1,counter+1)
    
    print(counter)
    
recursive_func(5)


def count_calls(n):
    if n <1:
        return 0
    
    count = count_calls(n-1)
    
    return count + 1


print(count_calls(5))