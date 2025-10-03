'''
Problem Description
Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.

NOTE:
Each element in the result should appear as many times as it appears in both arrays.
The result can be in any order.

Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A of size N.
Second argument is an integer array B of size M.

Output Format
Return an integer array denoting the common elements.

Example Input
Input 1:
 A = [1, 2, 2, 1]
 B = [2, 3, 1, 2]
Input 2:
 A = [2, 1, 4, 10]
 B = [3, 6, 2, 10, 10]

Example Output
Output 1:
 [1, 2, 2]
Output 2:
 [2, 10]

Example Explanation
Explanation 1:
 Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
Explantion 2:
 Elements (2, 10) appears in both the array.
'''


# brute force approach....
def common_elements(A, B)-> list:
    result = []
    for item in A:   #O(A)
        if item in B: #O(B)
            result.append(item)
            B.remove(item)
    return result



# Optimising using frequency approach....../ hashmap

def common_elements_freq(A: list, B: list)-> list:
    # step1: create hashmap to maintain the frequency of each element...
    hashmap = {}
    # iterate over A list and add it in hashmap with count
    for item in A:
        if hashmap.get(item) is None:
            hashmap[item] = 1
        else:
            hashmap[item]+=1
    # create a list to store the common values in both the list (A,B)
    result = []
    for item in B:
        if hashmap.get(item) is not None and hashmap[item] > 0:
            result.append(item)
            hashmap[item]-=1
    return result

if __name__ == "__main__":
    A = [1,2,3,4,5]
    B = [1,2,3,4,5]
    # print(common_elements(A,B))
    print(common_elements_freq(A,B))

