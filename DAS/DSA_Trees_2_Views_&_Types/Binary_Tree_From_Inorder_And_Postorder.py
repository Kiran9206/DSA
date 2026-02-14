'''
Problem Description

Given the inorder and postorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First argument is an integer array A denoting the inorder traversal of the tree.
Second argument is an integer array B denoting the postorder traversal of the tree.

Output Format
Return the root node of the binary tree.

Example Input
Input 1:
 A = [2, 1, 3]
 B = [2, 3, 1]
Input 2:
 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]

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

def build_bt(inorder, postorder,  in_start, in_end, post_start, post_end):

    if in_start > in_end or post_start > post_end:
        return None

    root = postorder[post_end]
    node = Node(root)
    root_idx = inorder.index(root)  # alone takes O(n) time, we can optimize this by using a hashmap to store the index of each node in the inorder tree
    lst_count = root_idx - in_start

    node.left = build_bt(inorder, postorder, in_start, root_idx - 1, post_start, post_start + lst_count - 1 )
    node.right = build_bt(inorder, postorder, root_idx + 1, in_end, post_start + lst_count, post_end - 1)

    return node


def build_bt_opt(inorder, postorder,  in_start, in_end, post_start, post_end, inorder_index_map):

    if in_start > in_end or post_start > post_end:
        return None

    root = postorder[post_end]
    node = Node(root)
    root_idx = inorder_index_map[root]  # alone takes O(1) time
    lst_count = root_idx - in_start

    node.left = build_bt_opt(inorder, postorder, in_start, root_idx - 1, post_start, post_start + lst_count - 1,inorder_index_map )
    node.right = build_bt_opt(inorder, postorder, root_idx + 1, in_end, post_start + lst_count, post_end - 1,inorder_index_map)

    return node

A = [2, 1, 3]
B = [2, 3, 1]


inorder_index_map = {num : idx for idx, num in enumerate(A)}
