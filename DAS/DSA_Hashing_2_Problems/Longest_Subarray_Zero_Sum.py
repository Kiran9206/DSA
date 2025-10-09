'''
Problem Description

Given an array A of N integers.
Find the length of the longest subarray in the array which sums to zero.
If there is no subarray which sums to zero then return 0.

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
Single argument which is an integer array A.

Output Format
Return an integer.
Example Input
Input 1:
 A = [1, -2, 1, 2]
Input 2:
 A = [3, 2, -1]
Example Output
Output 1:
3
Output 2:
0
Example Explanation
Explanation 1:
 [1, -2, 1] is the largest subarray which sums up to 0.
Explanation 2:
 No subarray sums up to 0.
'''


# brute force approach....

def longest_subarray_0_sum(A: list)->int:
    n = len(A)
    max_length = 0
    for start in range(n):
        for end in range(start, n):
            current_sum = sum(A[start:end+1])
            if current_sum == 0:
                max_length = max(max_length, end - start + 1)
    return max_length

# prefix sum approach....

def longest_subarray_0_sum_prefix(A: list)->int:
    n = len(A)
    max_length = 0
    # create prefix sum
    prefix_sum = [0] * (n)
    prefix_sum[0] = A[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

    for start in range(n):
        for end in range(start, n):
            current_sum = prefix_sum[end] - (prefix_sum[start-1] if start > 0 else 0)
            if current_sum == 0:
                max_length = max(max_length, end - start + 1)
    return max_length

# carry forward approach...
def longest_subarray_0_sum_carry(A: list)->int:
    n = len(A)
    max_length = 0
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += A[end]
            if current_sum == 0:
                max_length = max(max_length, end - start + 1)
    return max_length


# hashmap + prefix_sum approach.....

def longest_subarray_0_sum_hashmap(A:list)-> int:
    n= len(A)
    max_length = 0
    current_sum = 0
    hash_map = {}
    for idx, item in enumerate(A):
        current_sum+=item
        if current_sum == 0:
            max_length = max(max_length, idx+1)
        if current_sum in hash_map:
            prev_idx = hash_map[current_sum]
            max_length = max(max_length, idx - prev_idx)
        else:hash_map[current_sum] = idx
    return max_length








if __name__ == '__main__':
    A = [1, -2, 1, 2]
    A = [3, 2, -1]
    print(longest_subarray_0_sum(A))
    print(longest_subarray_0_sum_carry(A))
    print(longest_subarray_0_sum_prefix(A))
    print(longest_subarray_0_sum_hashmap(A))
