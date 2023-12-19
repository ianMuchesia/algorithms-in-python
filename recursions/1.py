def counter(n):
    total = 0
    for i in range(n+1):
        total += i
        print("total: ", total, " i: ", i)
    return total

#print(counter(10))

def recursive_counter(n,total = 0):
    if n == 0:
        return 1 + total
    total += n
    print(total)
    return recursive_counter(n-1,total)
    
print(recursive_counter(10))