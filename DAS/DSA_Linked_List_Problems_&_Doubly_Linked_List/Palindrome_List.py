'''
Problem Description
Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.

Problem Constraints
1 <= |A| <= 105

Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.

Output Format
Return 0, if the linked list is not a palindrome.
Return 1, if the linked list is a palindrome.

Example Input
Input 1:
A = [1, 2, 2, 1]
Input 2:
A = [1, 3, 2]

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
Explanation 2:
 The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].
'''
def mid(head):
    slow = fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head):
    current = head
    prev = forward = None

    while current:
        forward = current.next
        current.next = prev
        prev = current
        current = forward
    return prev

def palindrome(head):

    if not head or not head.next:
        return 1

    mid_ele = mid(head)
    head_2 = mid_ele.next
    mid_ele.next = None

    head_2 = reverse(head_2)

    while head_2:
        if head.val != head_2.val:
            return 0
        head = head.next; head_2 = head_2.next
    return 1