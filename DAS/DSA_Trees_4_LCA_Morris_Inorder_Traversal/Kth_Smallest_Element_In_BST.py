'''
Problem Description
Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Input Format
First and only argument is head of the binary tree A.

Output Format
Return an integer, representing the Bth element.

Example Input
Input 1:
            2
          /   \
         1    3
B = 2
Input 2:
            3
           /
          2
         /
        1
B = 1

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:
2nd element is 2.
Explanation 2:
1st element is 1.
'''
from http.cookiejar import cut_port_re


# brute force

def in_dfs(A,B):
    if A is None:
        return
    return in_dfs(A.left, B) + [ A.val ] + in_dfs(A.right, B)

# counter approach
counter = 0
def counter_dfs(A, B):
    global counter
    if A is None:
        return

    counter_dfs(A.left, B)
    counter+=1
    if counter == B:
        return A.val
    counter_dfs(A.right, B)

def kth_smallest(A, B):
    in_order = in_dfs(A, B)
    return in_order[B - 1]


def optimized_kth_smallest(A, B):

    if A is None:
        return -1

    current = A
    while current:
        if current.left is None:
            B -= 1
            if B == 0:
                return current.val
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is current:
                predecessor.right = None
                B-=1
                if B == 0:
                    return current.val
                current = current.right
            else:
                predecessor.right = current
                current = current.left
    return -1






