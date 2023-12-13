A = [ 1,4,9]
l = map(str,A)
s = ''.join(list(map(str,A)))

r =str(int(s)+1)

print(list(r))



def plus_one(A):
    A[-1] +=1
    #iterate backwards
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A