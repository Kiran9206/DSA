# bruteforce solution.... backtracking....
from stringprep import in_table_a1
from typing import List
def min_sum_path(A: List[List[int]])->int:
    def helper(A: List[List[int]], row: int = 0, col: int= 0)->int:

        # step1: set the base case
        if row == len(A) -1:
            return A[row][col]

        # edge case
        if col < 0 or col >= len(A[row]):
            return float('inf')

        # step2: recursive case
        # deside which way to go down or down-right
        down = helper(A, row+1, col)
        down_right = helper(A, row+1, col+1)
        return A[row][col] + min(down, down_right)

    return helper(A)

# It's a dp satisfying optimal substructure and overlapping sub_problem property

# Memorization
def min_sum_path_memo(A: List[List[int]])-> int:
    memo = [[-1 for _ in range(len(A[-1]))] for _ in range(len(A))]

    def helper(A: List[List[int]], row: int = 0, col: int = 0):
        # step1: set the base case
        if row == len(A) - 1:
            return A[row][col]

        # edge case
        if col < 0 or col >= len(A[row]):
            return float('inf')

        # step2: check if the result is already computed
        if memo[row][col] != -1:
            return memo[row][col]

        # step3: recursive case
        down = helper(A, row+1, col)
        down_right = helper(A, row+1, col+1)
        memo[row][col] = A[row][col] + min(down, down_right)
        return memo[row][col]

    return helper(A)

# Tabulation approach...

def min_sum_path_tab(A: List[List[int]])-> int:
    DP = [[0 for _ in range(len(A))] for _ in range(len(A))]

    # Fill the last row of the DP table
    for col in range(len(A[-1])):
        DP[-1][col] = A[-1][col]

    # Fill rest of the table
    for row in range(len(A)-2, -1, -1):
        for col in range(len(A[row])):
            DP[row][col] = A[row][col] + min(DP[row+1][col], DP[row+1][col+1])

    return DP[0][0]


# Space optimisation

def min_sum_path_space(A: List[List[int]])->int:
    prev = A[-1][:]

    for row in range(len(A)-2, -1, -1):
        for col in range(len(A[row])):
            prev[col] = A[row][col] + min(prev[col], prev[col+1])

    return prev[0]


A = [
         [2],
         [3, 4],
         [6, 5, 7],
         [4, 1, 8, 3]
    ]

print(min_sum_path(A))
print(min_sum_path_memo(A))
print(min_sum_path_tab(A))
print(min_sum_path_space(A))