'''
Problem Description
Given a binary tree, return the inorder traversal of its nodes' values.
NOTE: Using recursion and stack are not allowed.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return an integer array denoting the inorder traversal of the given binary tree.

Example Input
Input 1:
   1
    \
     2
    /
   3
Input 2:
   1
  / \
 6   2
    /
   3

Example Output
Output 1:
 [1, 3, 2]
Output 2:
 [6, 1, 3, 2]

Example Explanation
Explanation 1:
 The Inorder Traversal of the given tree is [1, 3, 2].
Explanation 2:
 The Inorder Traversal of the given tree is [6, 1, 3, 2].
'''


def morris_inorder(A):
    ans  = []
    if A is None:
        return ans

    current = A

    while current:

        if current.left is None:
            ans.append(current.val)
            current = current.right

        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left

            else:
                ans.append(current.val)
                predecessor.right = None
                current = current.right
    return ans
