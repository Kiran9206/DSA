'''
Problem Description

You are given an integer array A denoting the Level Order Traversal of the Binary Tree.
You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.
NOTE:
In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.

Problem Constraints
1 <= number of nodes <= 105
-1 <= A[i] <= 105

Input Format
Only argument is an integer array A denoting the Level Order Traversal of the Binary Tree.

Output Format
Return the root node of the Binary Tree.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Input 2:
 A = [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]

Example Output
Output 1:
           1
         /   \
        2     3
       / \
      4   5
Output 2:
            1
          /   \
         2     3
        / \ .   \
       4   5 .   6

Example Explanation
Explanation 1:
 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3, 4 and 5 each has both NULL child we had represented that using -1.
Explanation 2:
 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3 has left child as NULL while 4 and 5 each has both NULL child.
'''


from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def deserialize(A):

    if not A or A[0] == -1:
        return None

    root = Node(A[0])
    queue = deque([root])
    i = 1

    while queue and i < len(A):

        node = queue.popleft()

        if A[i] != -1:
            node.left = Node(A[i])
            queue.append(node.left)
        i+=1

        if A[i] != -1 and i < len(A):
            node.right = Node(A[i])
            queue.append(node.right)
        i+=1
    return root