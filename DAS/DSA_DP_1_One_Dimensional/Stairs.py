

# brute force solution recursion
from typing import List

def stairs(A: int)-> List[List[int]]:


    def stairs_helper(A: int, current_ans: List[int] = None, result: List[List[int]] = None)->List[List[int]]:

        if current_ans is None:
            current_ans = []

        if result is None:
            result = []

        # step1: base condition
        if A < 0:
            return result
        if A == 0:
            result.append(current_ans[:])
            return result

        # step2: iterate through all the possible steps ie: 1, 2

        # go for 1 step
        current_ans.append(1)
        stairs_helper(A - 1, current_ans, result)
        current_ans.pop() #backtrack

        # go for 2 step
        current_ans.append(2)
        stairs_helper(A - 2, current_ans, result)
        current_ans.pop() #backtracing....

        return result
    return stairs_helper(A)

print(stairs(3))


# Time Complexity: O(2^N), Space Complexity: O(N)

# Optimization using memorisation / top-down approach

def stairs(A: int)-> List[List[int]]:
    memo = {}

    def stairs_helper(remaining_steps: int)-> List[List[int]]:

        # edge case
        if remaining_steps < 0:
            return []

        # step1: base case
        if remaining_steps == 0:
            return [[]]   #for 0 there is only one way that is do nothing

        if remaining_steps in memo:
            return memo[remaining_steps]

        result = []
        # Moving all the way to 1 step
        for way in stairs_helper(remaining_steps-1):
            result.append(way + [1])

        # Moving all the ways to 2 steps
        for way in stairs_helper(remaining_steps - 2):
            result.append(way + [2])

        memo[remaining_steps] = result
        return memo[remaining_steps]

    return stairs_helper(A)


# Tabulation/ bottom-up approach

def stairs_tabulation(remaining_step: int)-> List[List[int]]:

    memo = {0: [[]]}

    for step in range(1, remaining_step+1):
        result = []

        # Moving all the way to 1 step
        for way in memo.get(step - 1, []):
            result.append(way + [1])

        # Moving all the way to 2 steps
        for way in memo.get(step - 2, []):
            result.append(way + [2])

        memo[step] = result

    return memo[remaining_step]



