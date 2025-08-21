
from typing import List
def max_one(A: List[List[int]])-> int:
    ans = -1
    row = 0; column = len(A[0]) - 1
    while row < len(A) and column >= 0:
        if A[row][column] == 1:
            column -= 1; ans = row
        if A[row][column] == 0:
            row += 1
    return ans