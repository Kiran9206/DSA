'''
Problem Description
Given preorder and inorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First argument is an integer array A denoting the preorder traversal of the tree.
Second argument is an integer array B denoting the inorder traversal of the tree.

Output Format
Return the root node of the binary tree.

Example Input
Input 1:
 A = [1, 2, 3]
 B = [2, 1, 3]
Input 2:
 A = [1, 6, 2, 3]
 B = [6, 1, 3, 2]

Example Output
Output 1:
   1
  / \
 2   3
Output 2:
   1
  / \
 6   2
    /
   3

Example Explanation
Explanation 1:
 Create the binary tree and return the root node of the tree.
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def build_bt(preorder, inorder, pre_start, pre_end, in_start, in_end):

    if pre_start > pre_end or in_start > in_end:
        return None

    root = preorder[pre_start]
    node = Node(root)

#     find where is this root located in the inorder tree
    root_idx = inorder.index(root)
    lst_count = root_idx - in_start

    # build left sub tree for this root
    node.left = build_bt(preorder,inorder, pre_start + 1, pre_start + lst_count, in_start, root_idx - 1)
    # build right sub tree for this root
    node.right = build_bt(preorder,inorder, pre_start + lst_count + 1, pre_end, root_idx + 1, in_end)

    return node






