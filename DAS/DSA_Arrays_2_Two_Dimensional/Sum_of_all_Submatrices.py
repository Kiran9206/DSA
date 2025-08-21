# bruteforce approach....
from typing import List
def sum_of_submatrices(A:List[List[int]]):
    n = len(A)
    m = len(A[0])
    total_sum = 0
    for r_start in range(n):
        for c_start in range(m):
            for r_end in range(r_start, n):
                for c_end in range(c_start, m):
                    for i in range(r_start, r_end + 1):
                        for j in range(c_start, c_end + 1):
                            total_sum += A[i][j]
    return total_sum

# Time Complexity: O(n^3 * m^3)
# Space Complexity: O(1)

# optimised contribution approach....

def sum_of_sub_matrices(A: List[List[int]]) -> int:
    n = len(A)
    m = len(A[0])
    total_sum = 0

    for idx_r in range(n):
        for idx_c in range(m):
            contribution = (idx_r + 1) * (n - idx_r) * (idx_c + 1) * (m - idx_c)
            total_sum += A[idx_r][idx_c] * contribution
    return total_sum

