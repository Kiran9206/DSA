

# brute force solution using recursion.....

def max_sum_no_adjacent(A: int):

    def helper(A: int, idx=0)-> int:

        # step1: set the base condition...
        if idx >= len(A):
            return 0

        # step2: select the element and jump to next of next index...
        selected = A[idx] + helper(A, idx + 2)
        # step3: not select the element and jump to the very next index.....
        not_selected = helper(A, idx + 1)
        return max(selected, not_selected)

    return helper(A)


# as we know here it is following the optimal structure ie: recursion and also following the overlapping
# sub_problems hence it's a dp problem we can optimise it further...

# dp -> memorization
def max_sum_no_adj_memo(A: int)-> int:
    n = len(A)
    memo = [-1] * (n)
    def helper(A: int, idx=n-1)-> int:

        # set the base
        if idx < 0:
            return 0

        # check the sub_problem is already calculated or not
        if memo[idx] != -1:
            return memo[idx]

        # step2: select the element and jump to next of next index...
        selected = A[idx] + helper(A, idx - 2)
        # step3: not select the element and jump to the very next index.....
        not_selected = helper(A, idx - 1)
        memo[idx] = max(selected, not_selected)
        return memo[idx]
    return helper(A)


# dp -> tabulation
def max_sum_no_adj_tab(A: int)-> int:
    if not A:
        return 0
    memo = [0] * len(A)
    memo[0] = A[0]
    for idx in range(1, len(A)):
        selected = A[idx]
        if idx > 1:
            selected += memo[idx - 2]
        not_selected = memo[idx - 1]
        memo[idx] = max(selected, not_selected)
    return memo[len(A)-1]

# dp -> space optimisation

def max_sum_no_adj_space(A: int)->int:
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return A[0]
    prev_prev = max(0, A[0])
    prev = max(A[1], prev_prev)
    ans = 0

    for idx in range(2,len(A)):
        selected = A[idx] + prev_prev
        not_selected = prev
        ans = max(selected, not_selected)
        prev, prev_prev = ans, prev
    return ans



# for 2 * N grid same problem

# convert it into 1d array
def convert_2d_to_1d(A):
    n = len(A[0])
    ans = [0] * n
    for idx in range(n):
        ans[idx] = max(A[0][idx], A[1][idx])
    return ans

# pass the same to the above problem

if __name__ == "__main__":
    A = [1,0,10,15,1]
    print(max_sum_no_adjacent(A))
    print(max_sum_no_adj_memo(A))
    print(max_sum_no_adj_tab(A))
    print(max_sum_no_adj_space(A))

