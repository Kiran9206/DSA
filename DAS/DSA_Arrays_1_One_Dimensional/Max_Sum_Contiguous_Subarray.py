# bruteforce approach....
def max_sum_contiguous_subarray(A: list)-> int:
    ans = float('-inf')
    for start in range(len(A)):
        for end in range(start, len(A)-1):
            ans = max(ans, sum(A[start:end+1]))
    return ans

# carry forward approach...
def max_sum_contiguous_subarray1(A: list) -> int:
    ans = float('-inf')
    for start in range(len(A)):
        sum = 0
        for end in range(start, len(A)):
            sum+= A[end]
            ans = max(ans, sum)
    return ans

# optimised kadane's algorithm...
def max_sum_contiguous_subarray2(A: list) -> int:
    local_sum = global_sum = A[0]
    for idx in range(1, len(A)):
        if local_sum < 0:
            local_sum = 0
        local_sum += A[idx]
        global_sum = max(local_sum, global_sum)
    return global_sum