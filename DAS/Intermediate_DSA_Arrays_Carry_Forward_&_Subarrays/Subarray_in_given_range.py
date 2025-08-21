def substring_in_a_range(A,B,C):
    if len(A) <= 1:
        return A
    return A[B:C+1]