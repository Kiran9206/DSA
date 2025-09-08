# brute force solution....

def fib(n: int)-> int:

    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# backtracking is not possible here because we are not making any choice here it's straight forward addition of previous two numbers

# Dp solution
# condition1: optimal / standard substructure : recursive call-> Large problem can be solved by breaking it down into smaller sub_problems
# condition2: overlapping sub_problems : recursive call -> same sub_problem is solved multiple times

# top-down approach / memoization : basically starts from largest problem and breaks it down into smaller sub_problems
def fib_memorization(n: int, memo = None):
    if memo is None:
        memo = [-1] * (n + 1)
        # base case adjusted here....
        memo[0] = 0; memo[1] = 1

    if memo[n] != -1:
        return memo[n]
    memo[n] = fib_memorization(n-1, memo) + fib_memorization(n-2, memo)
    return memo[n]

# bottom-up approach / tabulation : basically starts from smallest problem and builds up to the largest problem

def fib_tabulation(n: int)-> int:

    # edge case
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for idx in range(2, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]
    return dp[-1]

# Further optimize the space complexity from O(n) to O(1) because we only need last two computed values to compute the current value

def fib_optimized(n: int)-> int:

    if n <= 1:
        return n
    prev2 = 0
    prev1 = 1
    for idx in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1

