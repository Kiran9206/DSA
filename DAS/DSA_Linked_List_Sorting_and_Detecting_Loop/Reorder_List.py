'''
Problem Description

Given a singly linked list A
 A: A0 → A1 → … → An-1 → An
reorder it to:
 A0 → An → A1 → An-1 → A2 → An-2 → …
You must do this in-place without altering the nodes' values.

Problem Constraints
1 <= |A| <= 106

Input Format
The first and the only argument of input contains a pointer to the head of the linked list A.

Output Format
Return a pointer to the head of the modified linked list.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [1, 2, 3, 4]

Example Output
Output 1:
 [1, 5, 2, 4, 3]
Output 2:
 [1, 4, 2, 3]

Example Explanation
Explanation 1:
 The array will be arranged to [A0, An, A1, An-1, A2].
Explanation 2:
 The array will be arranged to [A0, An, A1, An-1, A2].
'''

def reorder(A):

    if not A or not A.next:
        return A

    stack = []
    current = A
    while current:
        stack.append(current)
        current = current.next

    current = A
    while stack:
        forward = current.next
        if current == stack[-1]:
            current.next = None
            break
        current.next = stack.pop()
        current.next.next = forward
        current = forward
    return A


# optimised solution....
def reorder_optimised(A):

    if not A or not A.next:
        return A

    # find mid point
    slow = fast = A
    while fast and fast.next:
        slow =slow.next
        fast = not fast.next.next

    # reverse the second half of the linked list
    prev = None
    current = slow.next
    # reverse the second half of the linked list
    while current:
        forward = current.next
        current.next = prev
        prev = current
        current = forward

    # now merge the two halves of the linked list
    current = A
    mid = prev
    while mid:
        forward = current.next
        current.next = mid
        mid = mid.next
        current.next.next = forward
        current = forward
    return A