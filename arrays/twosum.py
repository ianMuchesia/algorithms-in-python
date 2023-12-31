#Time complexity: 0(n)
#Space complexity: 0(n)

def two_sum_hash_table(A,target):
    ht = dict()
    
    for i in range(len(A)):
        print(ht)
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target-A[i]] = A[i]
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum_hash_table(A,target))