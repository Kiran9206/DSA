'''
Problem Description
Sort a linked list, A in O(n log n) time.

Problem Constraints
0 <= |A| = 105

Input Format
The first and the only arugment of input contains a pointer to the head of the linked list, A.

Output Format
Return a pointer to the head of the sorted linked list.

Example Input
Input 1:
A = [3, 4, 2, 8]
Input 2:
A = [1]

Example Output
Output 1:
[2, 3, 4, 8]
Output 2:
[1]

Example Explanation
Explanation 1:
 The sorted form of [3, 4, 2, 8] is [2, 3, 4, 8].
Explanation 2:
 The sorted form of [1] is [1].
'''

class ListNode:

    def __init__(self, data):
        self.val = data
        self.next = None

def find_mid(head):
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(head1, head2):
    dummy_head = ListNode(-1)
    dummy_tail = dummy_head
    while head1 and head2:
        if head1.val <= head2.val:
            dummy_tail.next = head1
            head1 = head1.next
        else:
            dummy_tail.next = head2
            head2 = head2.next
        dummy_tail = dummy_tail.next
    if not head1:
        dummy_tail.next = head2
    else:
        dummy_tail.next = head1
    return dummy_head.next


def sort_list(A): # O(n log n) and O(log n)

    if not A or not A.next:
        return A

    head1 = A
    mid = find_mid(head1)  #O(n) and O(1) space
    head2 = mid.next
    mid.next = None

    head1 = sort_list(head1) #O(log n) and O(log n) space
    head2 = sort_list(head2) #O(log n) and O(log n) space
    return merge(head1, head2) #O(n + m) and O(1) space
