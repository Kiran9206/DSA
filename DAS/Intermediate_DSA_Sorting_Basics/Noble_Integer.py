# bruteforce approach...


def noble_integer(A:list)->int:

    for idx_i in range(len(A)):
        count = 0
        for idx_j in range(len(A)):
            if A[idx_j] > A[idx_i]:
                count+=1
        if count == A[idx_i]:
            return 1
    return -1


# optimized approach...


def noble_integer_optimized(A:list)->int:
    A.sort(reverse=True)
    n = len(A); count = 0
    if A[0] == 0:
        return 1
    for idx in range(1,n):
        if A[idx] != A[idx-1]:
            count = idx
        if count == A[idx]:
            return 1
    return -1
