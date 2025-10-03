from  typing import List
# bruteforce approach.. backtracking....

def unique_paths(A: List[List[int]])-> int:

    def helper(A: List[List[int]], row: int, col: int)-> int:
        # base case
        if row == len(A) - 1 and col == len(A[0])-1:
            return 1
        # edge case
        if row >= len(A) or col >= len(A[0]) or A[row][col] == 1:
            return 0

        # move towards right and down
        return helper(A, row, col+1) + helper(A, row+1, col)

    return helper(A,0,0)


# DP is possible since the problem has overlapping sub_problems and optimal substructure

# Memorization approach....
def unique_paths_memo(A: List[List[int]])-> int:
    memo = [[-1 for _ in range(len(A[0]))] for _ in range(len(A))]
    def helper(A: List[List[int]], row:int, col: int)-> int:
        # base case
        if row == len(A) - 1 and col == len(A[0]) - 1:
            return 1
        # edge case
        if row >= len(A) or col >= len(A[0]) or A[row][col] == 1:
            return 0
        if memo[row][col] != -1:
            return memo[row][col]

        # move towards right and down
        memo[row][col] = helper(A, row, col + 1) + helper(A, row + 1, col)
        return memo[row][col]

    return helper(A, 0,0)


# Tabulation approach....
def unique_paths_tab(A: List[List[int]])-> int:
    DP = [[-1 for _ in range(len(A[0]))] for _ in range(len(A))]
    M = len(A)
    N = len(A[0])

    for row in range(M -1, -1, -1):
        for col in range(N -1, -1, -1):
            if A[row][col] == 1:
                DP[row][col] = 0
            elif row == M-1 and col == N-1:
                DP[row][col] = 1
            else:
                right = DP[row][col +1] if col + 1 < N else 0
                down = DP[row +1][col] if row +1 < M else 0
                DP[row][col] = right + down

    return DP[0][0]


# Further space optimisation......
def unique_paths_space(A: List[List[int]])-> int:
    M = len(A)
    N = len(A[0])
    curr = [0] * N

    for row in range(M-1, -1, -1):
        for col in range(N-1, -1, -1):
            if A[row][col] == 1:
                curr[col] = 0
            elif row == M-1 and col == N-1:
                if A[row][col] == 1:
                    return 0
                else:
                    curr[col] = 1
            else:
                right = curr[col + 1] if col + 1 < N else 0
                down = curr[col] if col < N else 0
                curr[col] = right + down
    return curr[0]





if __name__ == "__main__":
    A = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
         ]
    # A = [
    #     [0, 0, 0],
    #     [1, 1, 1],
    #     [0, 0, 0]
    # ]
    print(unique_paths(A)) # Output: 2
    print(unique_paths_memo(A))
    print(unique_paths_tab(A))
    print(unique_paths_space(A))