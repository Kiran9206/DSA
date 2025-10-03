
# trying of greedy approach since the problem is related to greedy


# step1: find the nearest perfect square
# step2: subtract that from the main int and repeat step1 for the remaining value
# hear greedy approach may not work because we may need to check all the possible perfect square for the main value.


# brute force solution.....
# Recursion
def min_no_of_squares(A: int)->int:

    # step1: set base
    if A == 0:
        return 0
    ans = float('inf')
    for idx in range(1, int(A**0.5) + 1):
        ans = min(ans , 1 + min_no_of_squares(A - (idx * idx)))

    return ans

A = 12
print(min_no_of_squares(A))

# Time Complexity: O(2^N), Space Complexity: O(N)

# -------------------------------------------------------

# Approach 2: Top Down / memorization
# check it has a optimal structure or not and overlapping sub_problems or not
# in this case both the conditions are satisfied

def min_no_of_squares_top_down(A: int, dp: list = None)->int:

    # step1: define the storage for overlapping sub_problems
    if dp is None:
        dp = [-1] * (A + 1)

    # step2: base condition
    if A == 0: return 0

    # step3: check if the sub_problem is already solved or not
    if dp[A] != -1:
        return dp[A]

    ans = float('inf')
    # step4: iterate through all the possible perfect squares ie: <= sqrt(A)
    for idx in range(1, int(A**0.5)+1):

        # step5: solve the sub_problem recursively
        ans = min(ans, 1 + min_no_of_squares_top_down(A - (idx * idx), dp))
        # step6: store the result
    dp[A] = ans
    return dp[A]


A = 12
print(min_no_of_squares_top_down(A))

# Time Complexity: O(N * sqrt(N)), Space Complexity: O(N)

# -------------------------------------------------------

# Approach 3: Bottom Up / Tabulation

def min_no_of_squares_bottom_up(A: int)->int:

    # step1: create the dp array
    dp = [-1] * (A + 1)

    # step2: base case
    dp[0] = 0

    # step3: iterate through all the values from 1 to A
    for idx in range(1, A + 1):
        ans = float('inf')
        # step4: iterate through all the possible perfect squares ie: <= sqrt(idx)
        for j in range(1, int(idx**0.5) + 1):
            ans = min(ans, 1 + dp[idx - (j * j)])
            dp[idx] = ans
    return dp[A]

A = 12
print(min_no_of_squares_bottom_up(A))

# Time Complexity: O(N * sqrt(N)), Space Complexity: O(N)
# -------------------------------------------------------
# here we can't further optimize the space because we need all the previous values to calculate the current value.