# brute force backtracking.....

from typing import List
def min_sum_path(A: List[List[int]]):
    M = len(A)
    N = len(A[0])
    def helper(A: List[List[int]], row: int = 0, col: int = 0)-> int:


        # step1: set the base case
        if row == M-1 and col == N-1:
            return A[row][col]

        # edge cases
        if row > M-1 or col > N-1:
            return float('inf')

        # step2: move towards right
        right = helper(A, row, col+1)
        # step3: move towards down
        down = helper(A, row+1, col)
        return A[row][col] + min(right, down)

    return helper(A)

# DP can be applied here because it has standard structure of DP ie: optimal structure and overlapping sub_problems

# Memorization

def min_sum_path_memo(A: List[List[int]])-> int:
    M = len(A)
    N = len(A[0])
    memo = [[-1 for _ in range(N)] for _ in range(M)]
    def helper(A: List[List[int]], row: int = 0, col: int = 0)-> int:

        # step1: set the base case
        if row == M-1 and col == N-1:
            return A[row][col]

        # edge cases
        if row > M-1 or col > N-1:
            return float('inf')

        # check if the sub_problem is already calculated or not
        if memo[row][col] != -1:
            return memo[row][col]

        right = helper(A, row, col+1)
        down = helper(A, row+1, col)
        memo[row][col] = A[row][col] + min(right, down)
        return memo[row][col]
    return helper(A)

# tabulation
def min_sum_path_tab(A: List[List[int]])-> int:
    M = len(A)
    N = len(A[0])
    DP = [[-1 for _ in range(N)] for _ in range(M)]
    DP[M-1][N-1] = A[M-1][N-1]

    # fill the last row
    for col in range(N-2, -1, -1):
        DP[M-1][col] = A[M-1][col] + DP[M-1][col+1]

    # fill the last col
    for row in range(M-2, -1, -1):
        DP[row][N-1] = A[row][N-1] + DP[row+1][N-1]

    # fill the rest with the DP table
    for row in range(M-2, -1, -1):
        for col in range(N-2, -1, -1):
            DP[row][col] = A[row][col] + min(DP[row+1][col], DP[row][col+1])
    return DP[0][0]


# further space optimisation

def min_sum_path_space(A:List[List[int]])-> int:
    M = len(A)
    N = len(A[0])
    DP = [A[M-1][N-1]] * N

    # fill up the last row first
    for col in range(N-2, -1, -1):
        DP[col] = A[M-1][col] + DP[col+1]

    # fill up the last column and compute the result
    for row in range(M - 2, -1, -1):
        # update the last colum first
        DP[N-1] += A[row][N-1]
        for col in range(N - 2, -1, -1):
            DP[col] = A[row][col] + min(DP[col], DP[col+1])

    return DP[0]


A = [[0,1,5,10],[2,3,4,5],[8,0,0,1]]
print(min_sum_path(A))
print(min_sum_path_memo(A))
print(min_sum_path_space(A))


