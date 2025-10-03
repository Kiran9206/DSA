# brute force approach: using catalon numbers

def chords(A: int) -> int:
    mod = 10**9 + 7

    # step1: base case
    if A <= 1:
        return 1

    result = 0
    for idx in range(A):
        result += chords(idx) * chords(A - 1 - idx)

    return result % mod


# optimise it using dp-> memorisation...

def chords_memorisation(A: int):
    memo = [-1] * (A + 1)
    mod = 10**9 + 7

    def chord_helper(leftover_chords: int):

        # base case
        if leftover_chords <= 1:
            return 1

        # check if the sub_problem is precalculated or not
        if memo[leftover_chords] != -1:
            return memo[leftover_chords]

        result = 0
        for idx in range(leftover_chords):
            result += chord_helper(idx) * chord_helper(leftover_chords - 1 - idx)

        # store the result in the memory
        memo[leftover_chords] = result % mod
        return memo[leftover_chords]
    return chord_helper(A)


# same with using dp-> tabulation....

def chord_tabulation(A: int):
    mod = 10 ** 9 + 7
    memo = [0] * (A + 1)
    memo[0] = 1
    memo[1] = 1

    for idx in range(2, A + 1):
        result = 0
        for j in range(idx):
            result += memo[j] * memo[idx - 1 - j]
        memo[idx] = result % mod
    return memo[A]


# can't further optimise it because it is dependent the all other sub_problems

if __name__ == "__main__":
    A = 3
    print(chords(A))
    print(chords_memorisation(A))
    print(chord_tabulation(A))