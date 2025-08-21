# brute force approach....

def sub_array_sum_with_window(A: list, N: int, B: int, C:int)->int: # time complexity O(N*B) and space complexity O(1)
    start = 0
    end = B - 1
    while end < N:
        current_sum_value = sum(A[start:end+1])
        start+=1; end+=1
        if C == current_sum_value:
            return 1
    return 0

A = [6,3,3,6,7,8,7,3,7]
N = len(A)
B = 2  # Length of the subarray
C = 10  # Desired sum of the subarray

print(sub_array_sum_with_window(A, N, B, C))


# optimised sliding window approach....

def sub_array_sum_with_window_optimised(A: list, N: int, B: int, C:int)->int: # ti
    current_sum_value = sum(A[:B])
    if current_sum_value == C:
        return 1

    for idx in range(B, N):
        current_sum_value += A[idx] - A[idx - B]
        if current_sum_value == C:
            return 1
    return 0