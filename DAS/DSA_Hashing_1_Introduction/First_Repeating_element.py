'''
Problem Description

Given an integer array A of size N, find the first repeating element in it.
We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
If there is no repeating element, return -1.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
The first and only argument is an integer array A of size N.

Output Format
Return an integer denoting the first repeating element.

Example Input
Input 1:
 A = [10, 5, 3, 4, 3, 5, 6]
Input 2:
 A = [6, 10, 5, 4, 9, 120]

Example Output
Output 1:
 5
Output 2:
 -1

Example Explanation
Explanation 1:
 5 is the first element that repeats
Explanation 2:
 There is no repeating element, output -1
'''


# bruteforce approach...

def repeating_ele(A: list)-> int:
    for item in A:
        freq = 0
        for idx in range(len(A)):
            if item == A[idx]:
                freq +=1
                if freq > 1:
                    return A[idx]
    return -1

# optimized approach... using hashmap
def repeating_ele_opt(A:list)-> int:
    # step1: create a hashmap
    hash_map = {}
    # creating hashmap using all the elements in a list to ensure all the elements mapped in a right order
    for item in A:
        hash_map[item] = hash_map.get(item,0)+1

    # Using the order of an elements in hashmap getting tbe first repeating element
    for item in A:
        if hash_map.get(item) > 1:
            return item

    return -1



A = [10, 5, 3, 4, 3, 5, 6]
# A = [6, 10, 5, 4, 9, 120]
print(repeating_ele(A))
print(repeating_ele_opt(A))

