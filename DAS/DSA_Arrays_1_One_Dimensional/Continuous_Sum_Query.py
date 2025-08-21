# bruteforce approach.....
from typing import List


def continuous_sum_query(A: int, B: List[List[int]])-> List[int]:

    result = [0]*A
    for q in range(len(B)):
        left = B[q][0]
        right = B[q][1]
        value = B[q][2]
        for i in range(left-1, right):
            result[i] += value

    return result



# optimised approach.... using prefix sum array

def continuous_sum_query_optimised(A: int, B: List[List[int]]) -> List[int]:
    result = [0] * A
    for q in range(len(B)):
        left = B[q][0]
        right = B[q][1]
        value = B[q][2]

        result[left - 1] += value
        if right < A:
            result[right] -= value

    for i in range(1, A):
        result[i] += result[i - 1]

    return result

