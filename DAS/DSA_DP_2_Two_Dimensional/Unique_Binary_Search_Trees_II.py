from idlelib.mainmenu import menudefs


# as it's a binary search tree it should e in order.....

# ex:   N = 0 -> there is one way means keep it empty or do nothing
#       N = 1 -> there is one way cause, lets say 1 keep the 1
#       N = 2 -> there are two ways both can be potential to become root nod 1 -right 2 and node 2 -left 1
#       N = 3 -> there are 5 ways lets say each can be potential to become root node c0*c2 + c1*c1 + c2*c0 => 5ways



# bruteforce solution.... is backtracking.....

def unique_BST(A: int) -> int:

    # set the base case
    if A == 0 or A == 1:
        return 1
    result = 0
    for idx in range(A):
        result += unique_BST(idx) * unique_BST(A - idx - 1)

    return result


# we can do this by using dynamic programming also... because it satisfies the optimal substructure and overlapping sub_problems....

# Memorisation
def unique_BTS_memo(A: int)-> int:
    memo = [-1] * (A + 1)

    def helper(A: int)-> int:

        # set the base case
        if A == 0 or A == 1: return 1

        # check the result is precalculated or not
        if memo[A] != -1:
            return memo[A]

        result = 0
        # iterate over the A number of times...
        for idx in range(A):
            result += helper(idx) * helper(A - idx - 1)
        # store it into the memory before returning the result
        memo[A] = result
        return memo[A]
    return helper(A)


# Tabulation approach.....

def unique_BST_tab(A: int) -> int:
    DP = [0] * (A+1)
    def helper(A: int)-> int:

        if A == 0 or A == 1: return 1

        if DP[A] != 0:
            return DP[A]

        result = 0
        for idx in range(A):
            result += helper(idx) * helper(A - idx - 1)
        DP[A] = result
        return DP[A]
    return helper(A)


# here i can't optimize the space because we need to store all the values from 0 to A in order to calculate the result.....'


if __name__ == "__main__":
    A = 4
    print(unique_BST(A))
    print(unique_BTS_memo(A))
    print(unique_BST_tab(A))