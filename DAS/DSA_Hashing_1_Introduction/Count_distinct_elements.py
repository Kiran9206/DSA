'''
Problem Description
Given an array A of N integers, return the number of unique elements in the array.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First argument A is an array of integers.

Output Format
Return an integer.

Example Input
Input 1:
A = [3, 4, 3, 6, 6]
Input 2:
A = [3, 3, 3, 9, 0, 1, 0]

Example Output
Output 1:
3
Output 2:
4

Example Explanation
For Input 1:
The distinct elements of the array are 3, 4 and 6.
For Input 2:
The distinct elements of the array are 3, 9, 0 and 1.
'''

# brute force
def distinct_ele(A: list)-> int:

    count = 0
    for idx_i in range(len(A)):
        is_distinct = True
        for idx_j in range(idx_i):
            if A[idx_i] == A[idx_j]:
                is_distinct = False
                break
        if is_distinct:
            count+=1
    return count

# optimising using hashset approach....

def distinct_ele_hashset(A: list)-> int:
    hash_set = set()
    for item in A:
        if item not in hash_set:
            hash_set.add(item)
    return len(hash_set)

# or

def distinct_ele_hashset_1(A: list)-> int:
    hash_set = set(A)
    return len(hash_set)


A = [3, 4, 3, 6, 6]
print(distinct_ele(A))
