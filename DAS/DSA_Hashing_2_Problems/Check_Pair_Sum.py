'''
Problem Description

Given an Array of integers B, and a target sum A.
Check if there exists a pair (i,j) such that Bi + Bj = A and i!=j.

Problem Constraints
1 <= Length of array B <= 105
0 <= Bi <= 109
0 <= A <= 109

Input Format
First argument A is the Target sum, and second argument is the array B

Output Format
Return an integer value 1 if there exists such pair, else return 0.

Example Input
Input 1:
A = 8
B = [3, 5, 1, 2, 1, 2]
Input 2:
A = 21
B = [9, 10, 7, 10, 9, 1, 5, 1, 5]
Example Output
Output 1:
1
Output 2:
0
Example Explanation
Example 1:
It is possible to obtain sum 8 using 3 and 5.
Example 2:
There is no such pair exists.
'''



# brute force
def checkPairSum(A:int, B:list)->int:
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            if B[i] + B[j] == A:
                return 1
    return 0

# Optimisation using hashset

def checkPairSum1(A:int, B:list)->int:
    hash_set = set()
    for item in B:
        if A - item in hash_set:
            return 1
        else:
            hash_set.add(item)
    return 0

if __name__ == "__main__":
    A = 8
    B = [3, 5, 1, 2, 1, 2]
    # A = 21
    # B = [9, 10, 7, 10, 9, 1, 5, 1, 5]
    print(checkPairSum(A,B))
    print(checkPairSum1(A,B))