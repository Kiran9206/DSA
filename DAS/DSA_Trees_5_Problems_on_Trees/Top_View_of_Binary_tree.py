'''
Problem Description
Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.
The top view of a Binary Tree is a set of nodes visible when the tree is visited from the top.
Return the nodes in any order.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Input Format
First and only argument is head of the binary tree A.

Output Format
Return an array, representing the top view of the binary tree.

Example Input
Input 1:
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8
Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5

Example Output
Output 1:
 [1, 2, 4, 8, 3, 7]
Output 2:
 [1, 2, 3]

Example Explanation
Explanation 1:
Top view is described.
Explanation 2:
Top view is described.
'''

from collections import deque

def top_view(root):

    if root is None:
        return []

    queue = deque([(root, 0)])
    ans = {}
    min_level = max_level = 0

    while queue:

        node, level = queue.popleft()
        # only store the first occurrence....
        if level not in ans:
            ans[level]= node.data
        min_level = min(min_level, level)
        max_level = max(max_level, level)

        if node.left:
            queue.append((node.left, level-1))

        if node.right:
            queue.append((node.right, level+1))

    return [ans[idx] for idx in range(min_level, max_level+1)]


def bottom_view(root):

    if root is None:
        return []

    queue = deque([(root, 0)])
    ans = {}
    min_level = max_level = 0

    while queue:
        node, level = queue.popleft()
        # only store the last occurrence....
        ans[level]= node.data
        min_level = min(min_level, level)
        max_level = max(max_level, level)

        if node.left:
            queue.append((node.left, level-1))

        if node.right:
            queue.append((node.right, level+1))
    return [ans[idx] for idx in range(min_level, max_level + 1)]



