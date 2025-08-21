def arithematic_progression(A:list)->int:
    A.sort()
    ans = A[1] - A[0]
    for idx in range(2, len(A)):
        diff = A[idx] - A[idx - 1]
        if diff != ans:
            return 0
    return 1