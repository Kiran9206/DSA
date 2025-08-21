from numpy.core.defchararray import lower


def anti_diagonal_r_l(A:list)->list:
    ans_arr = [[0]*len(A[0]) for _ in range(2*len(A)-1)]

    n = len(A)

    for idx in range(n):
        row = 0; col= idx; i = idx; j=0
        while row < n and col >= 0:
            ans_arr[i][j] = A[row][col]
            row += 1; col -= 1; j += 1
    for idx in range(1,n):
        row = idx; col = n-1; i = n-1+idx; j=0
        while row <n and col >= 0:
            ans_arr[i][j] = A[row][col]
            row +=1; col -= 1; j += 1
    return ans_arr


A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(anti_diagonal_r_l(A))


# -----------------------------------------------------------------------------


def anti_diagonal_l_r(A:list)->list:

    ans_arr = [[0]*len(A[0]) for _ in range(2*len(A)-1)]
    n = len(A)

    # upper half
    for idx in range(n):
        row = idx; col = 0;  i = idx; j =0

        while row >=0 and col < n:
            ans_arr[i][j] = A[row][col]
            row-=1; col+=1; j+=1
    # lower half

    for idx in range(1,n):
        col = idx; row = n-1; i = n-1+idx; j=0
        while row >=0 and col < n:
            ans_arr[i][j] = A[row][col]
            row -= 1; col += 1; j += 1
    return ans_arr

A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(anti_diagonal_l_r(A))