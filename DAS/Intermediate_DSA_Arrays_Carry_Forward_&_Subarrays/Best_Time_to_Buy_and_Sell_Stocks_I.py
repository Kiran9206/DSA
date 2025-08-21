

def best_time(A):
    ans = 0
    if len(A) > 1:
        min_value = A[0]; max_value = max(A)
        for idx in range(1, len(A)):
            if A[idx] == max_value:
                return ans
            if A[idx] < min_value:
                min_value = A[idx]
                prof = max_value - min_value
                ans = max(ans, prof)
    return ans
        