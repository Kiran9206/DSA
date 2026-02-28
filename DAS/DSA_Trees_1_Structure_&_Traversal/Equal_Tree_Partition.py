'''
Problem Description
Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values
after removing exactly one edge on the original tree.

Problem Constraints
1 <= size of tree <= 100000
0 <= value of node <= 109

Input Format
First and only argument is head of tree A.

Output Format
Return 1 if the tree can be partitioned into two trees of equal sum else return 0.
Example Input
Input 1:
                5
               /  \
              3    7
             / \  / \
            4  6  5  6
Input 2:
                1
               / \
              2   10
                  / \
                 20  2

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 Remove edge between 5(root node) and 7:
        Tree 1 =                                               Tree 2 =
                        5                                                     7
                       /                                                     / \
                      3                                                     5   6
                     / \
                    4   6
        Sum of Tree 1 = Sum of Tree 2 = 18
Explanation 2:
 The given Tree cannot be partitioned.
'''


from typing import Optional

class Solution:

    def find_partition(self, root, target_sum):
        global ans
        if root is None:
            return 0

        left_sum = self.find_partition(root.left, target_sum)
        right_sum = self.find_partition(root.right, target_sum)

        current_sum = left_sum + right_sum + root.data

        if current_sum == target_sum:
            ans = True

        return current_sum


    def tree_sum(self, root):
        if root is None:
            return 0
        return self.tree_sum(root.left) + self.tree_sum(root.right) + root.data


    def solve(self, A):
        global ans
        ans = False

        if A is None:
            return 0

        total_sum = self.tree_sum(A)

        if total_sum % 2 != 0:
            return 0

        # IMPORTANT: exclude the root itself
        self.find_partition(A.left, total_sum // 2)
        self.find_partition(A.right, total_sum // 2)

        return 1 if ans else 0









