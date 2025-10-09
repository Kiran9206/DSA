'''
Problem Description

Given an array A of N integers.
Find the count of the sub_arrays in the array which sums to zero. Since the answer can be very large, return the remainder
on dividing the result with 109+7


Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109


Input Format
Single argument which is an integer array A.

Output Format
Return an integer.

Example Input
Input 1:
 A = [1, -1, -2, 2]
Input 2:
 A = [-1, 2, -1]

Example Output
Output 1:
3
Output 2:
1

Example Explanation
Explanation 1:
 The sub_arrays with zero sum are [1, -1], [-2, 2] and [1, -1, -2, 2].
Explanation 2:
 The subarray with zero sum is [-1, 2, -1].
'''


# bruteforce approach...

def count_subarray_zero_sum(A: list) -> int:
    count = 0
    for start in range(len(A)):
        for end in range(start,len(A)):
            if sum(A[start:end + 1]) == 0:
                count += 1
    return count


# carry forward approach....

def count_subarray_zero_sum_1(A: list)-> int:

    count = 0
    for start in range(len(A)):
        sum = 0
        for end in range(start, len(A)):
            sum += A[end]
            if sum == 0:
                count += 1
    return count

# optimising using hashmap approach....

def count_subarray_zero_sum_2(A: list) -> int:
    count = 0
    hash_map = {}
    curr_sum = 0
    for item in A:
        curr_sum+=item
        if curr_sum == 0:
            count+=1
        if curr_sum in hash_map:
            count += hash_map[curr_sum]
        hash_map[curr_sum] = hash_map.get(curr_sum, 0) + 1

    return count








A = [1, -1, -2, 2]
A = [1,-2,0,2]
print(count_subarray_zero_sum(A))
print(count_subarray_zero_sum_1(A))
print(count_subarray_zero_sum_2(A))

