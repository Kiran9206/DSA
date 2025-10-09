'''
Problem Description
You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.
Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.
NOTE: if B > N, return an empty array.

Problem Constraints
1 <= N <= 106
1 <= A[i] <= 109

Input Format
First argument is an integer array A
Second argument is an integer B.

Output Format
Return an integer array.

Example Input
Input 1:
 A = [1, 2, 1, 3, 4, 3]
 B = 3
Input 2:
 A = [1, 1, 2, 2]
 B = 1
Example Output
Output 1:
 [2, 3, 3, 2]
Output 2:
 [1, 1, 1, 1]
Example Explanation
Explanation 1:
 A=[1, 2, 1, 3, 4, 3] and B = 3
 All windows of size B are
 [1, 2, 1]
 [2, 1, 3]
 [1, 3, 4]
 [3, 4, 3]
 So, we return an array [2, 3, 3, 2].
Explanation 2:
 Window size is 1, so the output array is [1, 1, 1, 1].
'''

# brute force approach....


def distinct_no_window(A: list, B:int)->list:
    n = len(A)

    # edge case
    if B > n:
        return []
    result = []
    for idx in range(n-B+1):
        window = A[idx:idx+B]
        distinct_count = len(set(window))
        result.append(distinct_count)
    return result

# Optimised approach....

def distinct_no_window_opt(A:list, B:int)->list:

    n= len(A)
    if B > n:
        return []
    hashmap = {}
    result = []
    # travers first window
    for item in A[0:B]:
        hashmap[item] = hashmap.get(item, 0)+1

    result.append(len(hashmap))
    # travers remaining windows
    for idx in range(B, n):
        # remove the first element from the previous window
        left_element = A[idx-B]
        hashmap[left_element] -= 1
        if hashmap[left_element] == 0:
            del hashmap[left_element]
        # add the new element from the current window
        right_element = A[idx]
        hashmap[right_element] = hashmap.get(right_element, 0)+1
        result.append(len(hashmap))
    return result



if __name__ == "__main__":
    # A = [1, 2, 1, 3, 4, 3]
    # B = 3
    A = [1, 1, 2, 2]
    B = 1
    print(distinct_no_window(A,B))
    print(distinct_no_window_opt(A,B))