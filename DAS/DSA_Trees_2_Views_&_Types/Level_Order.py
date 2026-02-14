'''
Problem Description
Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return a 2D integer array denoting the level order traversal of the given binary tree.

Example Input
Input 1:
    3
   / \
  9  20
    /  \
   15   7
Input 2:
   1
  / \
 6   2
    /
   3
Example Output
Output 1:
 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:
 [
   [1]
   [6, 2]
   [3]
 ]
Example Explanation
Explanation 1:
 Return the 2D array. Each row denotes the traversal of each level.
'''

from collections import deque
def levelOrder(root):

    if root is None:
        return []

    queue = deque([root])
    ans = []

    while queue:

        size = len(queue)
        for idx in range(size):

            node = queue.popleft()
            ans.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans


