def minor_diagonal(A:list):
    Sum = 0; col = len(A) - 1
    for row in range(len(A)):
        Sum+= A[row][col]
        col-=1
    return Sum


