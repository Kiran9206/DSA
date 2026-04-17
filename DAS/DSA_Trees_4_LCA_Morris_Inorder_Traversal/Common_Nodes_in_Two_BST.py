'''
Problem Description
Given two BST's A and B, return the (sum of all common nodes in both A and B) % (109 +7) .
In case there is no common node, return 0.
NOTE:
Try to do it one pass through the trees.

Problem Constraints
1 <= Number of nodes in the tree A and B <= 105
1 <= Node values <= 106

Input Format
First argument represents the root of BST A.
Second argument represents the root of BST B.

Output Format
Return an integer denoting the (sum of all common nodes in both BST's A and B) % (109 +7) .

Example Input
Input 1:
 Tree A:
    5
   / \
  2   8
   \   \
    3   15
        /
        9
 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11
Input 2:
  Tree A:
    7
   / \
  1   10
   \   \
    2   15
        /
       11
 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11

Example Output
Output 1:
 17
Output 2:
 46

Example Explanation
Explanation 1:
 Common Nodes are : 2, 15
 So answer is 2 + 15 = 17
Explanation 2:
 Common Nodes are : 7, 2, 1, 10, 15, 11
 So answer is 7 + 2 + 1 + 10 + 15 + 11 = 46
'''
from DSA_Hashing_1_Introduction.Count_unique_elements import frequency


# brute force

def search(node, value):
    if not node:
        return False

    if node.val == value:
        return True
    elif node.val > value:
        return search(node.left, value)
    else:
        return search(node.right, value)

def dfs(A,B):
    if not A:
        return 0

    total = 0
    if search(B, A.val):
        total += A.val

    total += dfs(A.left,B)
    total += dfs(A.right,B)
    return total


def common_nodes(A,B):
    MOD = 10 ** 9 + 7
    return dfs(A,B) % MOD


# optimised version

def get_inorder(A):
    stack = []
    if A is None: return stack
    current = A
    while current:
        if current.left is None:
            stack.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                stack.append(current.val)
                current = current.right
    return stack




def common_nodes_optimised(A,B):
    MOD = 10 ** 9 + 7
    total = 0
    freq = {}
    stack_a = set(get_inorder(A))
    stack_b = get_inorder(B)
    for value in stack_b:
        if value in stack_a:
            total += value
    return total % MOD









