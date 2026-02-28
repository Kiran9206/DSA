'''
Problem Description
Given a binary tree,
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Assume perfect binary tree.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Input Format
First and only argument is head of the binary tree A.

Output Format
Return the head of the binary tree after the changes are made.

Example Input
Input 1:
     1
    /  \
   2    3
Input 2:
        1
       /  \
      2    5
     / \  / \
    3  4  6  7

Example Output
Output 1:
        1 -> NULL
       /  \
      2 -> 3 -> NULL
Output 2:
         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL

Example Explanation
Explanation 1:
Next pointers are set as given in the output.
Explanation 2:
Next pointers are set as given in the output.
'''

from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = self.next = None



def connect(root):

    if root is None:
        return None

    queue = deque([root])
    while queue:

        size = len(queue)
        prev = None

        for idx in range(size):
            node = queue.popleft()
            if prev:
                prev.next = node
            prev = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def connect_optimised(root):

    if root is None:
        return None

    dummy_node = Node(-1)
    temp = dummy_node
    current_node = root

    while current_node:

        if current_node.left:
            temp.next = current_node.left
            temp = temp.next

        if current_node.right:
            temp.next = current_node.right
            temp = temp.next

        current_node = current_node.next

        if current_node is None:
            current_node = dummy_node.next
            dummy_node.next = None
            temp = dummy_node

    return root






def print_connected_nodes(root):

    if root is None:
        return {}

    queue = deque([root])
    ans = {}
    while queue:
        size = len(queue)

        for idx in range(size):
            node = queue.popleft()
            ans[node.data] = node.next.data if node.next else None

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans



if __name__ == "__main__":
    # Build tree
    n1 = Node(1)
    n2 = Node(2)
    n5 = Node(5)
    n3 = Node(3)
    n4 = Node(4)
    n6 = Node(6)
    n7 = Node(7)

    n1.left = n2
    n1.right = n5

    n2.left = n3
    n2.right = n4

    n5.left = n6
    n5.right = n7

    connect(n1)
    print(print_connected_nodes(n1))
    connect_optimised(n1)
    print(print_connected_nodes(n1))


