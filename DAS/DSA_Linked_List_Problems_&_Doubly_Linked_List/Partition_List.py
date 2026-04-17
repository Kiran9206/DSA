'''
Problem Description
Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B.
You should preserve the original relative order of the nodes in each of the two partitions.

Problem Constraints
1 <= |A| <= 106
1 <= A[i], B <= 109

Input Format
The first argument of input contains a pointer to the head to the given linked list.
The second argument of input contains an integer, B.

Output Format
Return a pointer to the head of the modified linked list.

Example Input
Input 1:
A = [1, 4, 3, 2, 5, 2]
B = 3
Input 2:
A = [1, 2, 3, 1, 3]
B = 2

Example Output
Output 1:
[1, 2, 2, 4, 3, 5]
Output 2:
[1, 1, 2, 3, 3]

Example Explanation
Explanation 1:
 [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.
Explanation 2:
 [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.
'''

class ListNode:

    def __init__(self, data):
        self.val = data
        self.next = None

def partition(A,B):

    if not A or not A.next:
        return A

    small_dummy = ListNode(-1)
    big_dummy  = ListNode(-1)

    small_head = small_dummy
    big_head = big_dummy

    current = A
    while current:
        if current.val < B:
            small_dummy.next = current
            small_dummy = small_dummy.next
        else:
            big_dummy.next = current
            big_dummy = big_dummy.next
        current = current.next

    big_dummy.next = None
    small_dummy.next = big_head.next

    return  small_head.next
