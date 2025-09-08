'''
Problem Description
Given an integer array A of size N.
You are also given an integer B, you need to find whether their exist a subset in A whose sum equal B.
If there exist a subset then return 1 else return 0.
Note : Sum of elements of an empty subset is 0.

Problem Constraints
1 <= N <= 17
-109 <= A[i] <= 109
-109 <= B <= 109

Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return 1 if there exist a subset with sum B else return 0.

Example Input
Input 1:
 A = [3, 34, -3, 12, 5, 2]
 B = 9
Input 2:
 A = [-8, 34, 4, 0, -5, -2]
 B = -20

Example Output
Output 1:
 1
Output 2:
 0
Example Explanation
Explanation 1:
 There is a subset (-3, 12) with sum 9.
Explanation 2:
 There is no subset that add up to -20.
'''

from typing import  List, Optional

def sub_set_sum(A: List[int], B: int, idx=0, current_ans = 0, ans = 0)-> Optional[int]:
    # step1: base case
    if idx >= len(A):
        if B == current_ans:
            return 1
        else: return 0

    # step2: don't add the element
    if sub_set_sum(A, B, idx+1, current_ans) == 1:
        return 1

    # step3: add the current element to the ans list
    current_ans += A[idx]
    if sub_set_sum(A, B, idx+1, current_ans) == 1:
        return 1
    return 0

if __name__ == "__main__":

    A = [3, 34, -3, 12, 5, 2]
    B = 9
    print(sub_set_sum(A, B))
