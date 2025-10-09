'''
Problem Description
Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
If the answer does not exist return an array with a single integer "[-1]".
First sub-array means the sub-array for which starting index in minimum.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single integer "[-1]".

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:
 A = [5, 10, 20, 100, 105]
 B = 110
Example Output
Output 1:
 [2, 3]
Output 2:
 [[-1]]

Example Explanation
Explanation 1:
 [2, 3] sums up to 5.
Explanation 2:
 No subarray sums up to required number.
'''
from typing import List

# BRUTE FORCE APPROACH...
def subarray_with_given_sum(A: list, B: int) -> List[int]:
    n = len(A)
    for start in range(n):
        for end in range(start, n):
            if sum(A[start: end+1]) == B:
                return A[start:end+1]
    return [-1]


# fre-fix sum approach....
def subarray_with_given_sum_prefix(A: list, B: int) -> List[int]:
    n = len(A)
    # create prefix sum
    prefix_sum = [0] * n
    prefix_sum[0] = A[0]
    for idx in range(1,n):
        prefix_sum[idx] = prefix_sum[idx-1] + A[idx]

    for start in range(n):
        for end in range(start, n):
            current_sum = prefix_sum[end] - (prefix_sum[start -1] if start > 0 else 0)
            if current_sum == B:
                return A[start:end+1]
    return [-1]

# Carry forward approach....
def subarray_with_given_sum_carry(A: list, B: int) -> List[int]:
    n = len(A)
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += A[end]
            if current_sum == B:
                return A[start:end+1]
            if current_sum > B:
                break
    return [-1]

# optimise using hashmap + fre-fix sum approach....
def subarray_with_given_sum_hashmap(A: list, B: int) -> List[int]:
    n = len(A)
    current_sum = 0
    hashmap = {}
    for idx, item in enumerate(A):
        current_sum+=item
        if current_sum == B:
            return A[:idx+1]
        if (current_sum - B) in hashmap:
            prev_idx = hashmap[current_sum - B]
            return A[prev_idx+1: idx+1]
        hashmap[current_sum] = idx
    return [-1]



# using sliding window approach... since, it has only positive elements in an array we can go for this appraoch..
def subarray_with_given_sum_sliding_window(A: list, B: int) -> List[int]:
    n = len(A)
    left = 0
    current_sum = 0
    for idx, item in enumerate(A):
        current_sum += item
        while current_sum > B and left <= idx:
            current_sum -= A[left]
            left += 1
        if current_sum == B:
            return A[left:idx+1]
    return [-1]
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = 5
    A = [5, 10, 20, 100, 105]
    B = 110
    print(subarray_with_given_sum(A, B))
    print(subarray_with_given_sum_prefix(A,B))
    print(subarray_with_given_sum_carry(A, B))
    print(subarray_with_given_sum_hashmap(A,B))
    print(subarray_with_given_sum_sliding_window(A,B))
    import sys
    print(sys.maxsize)  # Maximum number of elements a list can theoretically hold
    # l = [0] * (10**9)
    # print(l)