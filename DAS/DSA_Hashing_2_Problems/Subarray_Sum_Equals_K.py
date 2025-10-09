'''
Problem Description

Given an array of integers A and an integer B.
Find the total number of subarrays having sum equals to B.

Problem Constraints
 1 <= length of the array <= 50000
-1000 <= A[i] <= 1000

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the total number of subarrays having sum equals to B.

Example Input
Input 1:
A = [1, 0, 1]
B = 1
Input 2:
A = [0, 0, 0]
B = 0

Example Output
Output 1:
4
Output 2:
6
Example Explanation
Explanation 1:
[1], [1, 0], [0, 1] and [1] are four subarrays having sum 1.
Explanation 1:
All the possible subarrays having sum 0.
'''
from distutils.command.register import register

from Tools.scripts.texi2html import spprog


# Brute force approach....
def subarray_sum_equals_k(A: list , B: int)-> int:
    n = len(A)
    count = 0
    for start in range(n):
        for end in range(start, n):
            current_sum = sum(A[start: end+1])
            if current_sum == B:
                count += 1
    return count

# fre_fix sum approach....
def subarray_sum_equals_k_prefix(A: list, B: int) -> int:
    n = len(A)
    count=0
    # create prefix sum
    prefix_sum = [0] * (n)
    prefix_sum[0] = A[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

    for start in range(n):
        for end in range(start, n):
            current_sum = prefix_sum[end] - (prefix_sum[start-1] if start > 0 else 0)
            if current_sum == B:
                count += 1
    return count

# carry-forward approach...
def subarray_sum_equals_k_carry(A: list, B: int) -> int:
    n = len(A)
    count = 0
    for start in range(n):
        current_sum =0
        for end in range(start, n):
            current_sum+= A[end]
            if current_sum == B:
                count += 1
    return count

# optimised approach using hashmap + prefix sum...
def subarray_sum_equals_k_hashmap(A: list, B: int) -> int:
    n = len(A)
    count = 0
    curr_sum = 0
    hash_map = {}
    for item in A:
        curr_sum += item
        if curr_sum == B:
            count+=1
        if (curr_sum - B) in hash_map:
            count += hash_map[curr_sum - B]
        hash_map[curr_sum] = hash_map.get(curr_sum, 0) + 1
    return count



if __name__ == "__main__":
    A = [1, 0, 1]
    B = 1
    print(subarray_sum_equals_k(A, B))
    print(subarray_sum_equals_k_prefix(A, B))
    print(subarray_sum_equals_k_carry(A,B))
    print(subarray_sum_equals_k_hashmap(A, B))