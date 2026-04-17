'''
Problem Description
Find the lowest common ancestor in an unordered binary tree A, given two values, B and C, in the tree.
Lowest common ancestor: the lowest common ancestor (LCA) of two nodes and w in a tree or directed acyclic
graph (DAG) is the lowest (i.e., deepest) node that has both v and w as descendants.

Problem Constraints
1 <= size of tree <= 100000
1 <= B, C <= 109

Input Format
First argument is head of tree A.
Second argument is integer B.
Third argument is integer C.

Output Format
Return the LCA.

Example Input
Input 1:
      1
     /  \
    2    3
B = 2
C = 3
Input 2:
      1
     /  \
    2    3
   / \
  4   5
B = 4
C = 5

Example Output
Output 1:
 1
Output 2:
 2
Example Explanation
Explanation 1:
 LCA is 1.
Explanation 2:
 LCA is 2.
'''



def lca_util(A,B,C):

    if A is None:
        return None

    if A.val == B or A.val == C:
        return A

    left_lca = lca_util(A.left, B, C)
    right_lca = lca_util(A.right, B, C)

    if left_lca and right_lca:
        return A

    return left_lca if left_lca else right_lca

def exists(A, val):

    if A is None:
        return False
    if A.val == val:
        return True

    return exists(A.left, val) or exists(A.right, val)

def lca(A,B,C):
    node = lca_util(A,B,C)
    if node and exists(A,B) and exists(A,C):
        return node.val
    else: return -1



