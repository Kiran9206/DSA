# bruteforce approach...
from typing import List
def search_in_matrix(A: List[List[int]], B: int):
    n = len(A)
    m = len(A[0])
    ans = -1
    for row in range(n):
        for col in range(m):
            if A[row][col] == B:
                cans = (row+1)*1009+(col+1)
                if ans == -1 or cans < ans:
                    ans = cans
    return ans


# optimised approach... if it is sorted!

def search_in_matrix_opt(A: List[List[int]], B: int):
    l = 0; r = len(A[0]) - 1; ans = -1
    while l < len(A) and r >= 0 :
        if A[l][r] == B:
            cans = ((l+1) * 1009 + (r+1))
            if ans == -1 or cans < ans:
                ans = cans
            r -= 1
        elif A[l][r] > B:
            r -= 1
        else: l += 1
    return ans

