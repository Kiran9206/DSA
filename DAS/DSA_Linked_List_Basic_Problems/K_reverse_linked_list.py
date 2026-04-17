'''
Problem Description
Given a singly linked list A and an integer B, reverse the nodes of the list B at a time
and return the modified linked list.

Problem Constraints
1 <= |A| <= 103
B always divides A

Input Format
The first argument of input contains a pointer to the head of the linked list.
The second arugment of input contains the integer, B.

Output Format
Return a pointer to the head of the modified linked list.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5, 6]
 B = 2
Input 2:
 A = [1, 2, 3, 4, 5, 6]
 B = 3

Example Output
Output 1:
 [2, 1, 4, 3, 6, 5]
Output 2:
 [3, 2, 1, 6, 5, 4]

Example Explanation
Explanation 1:
 For the first example, the list can be reversed in groups of 2.
    [[1, 2], [3, 4], [5, 6]]
 After reversing the K-linked list
    [[2, 1], [4, 3], [6, 5]]
Explanation 2:
 For the second example, the list can be reversed in groups of 3.
    [[1, 2, 3], [4, 5, 6]]
 After reversing the K-linked list
    [[3, 2, 1], [6, 5, 4]]
'''



def reverse(A, start, end):
    if not A or start == end:
        return A

    current = A
    prev =  forward = left_prev = None

    pos = 1


    # first reach to the start position that is start
    while pos < start:
        left_prev = current
        current = current.next
        pos+=1

    # step2 reverse the linked list from position start to end
    tail_connect = current
    while pos <= end:
        forward = current.next
        current.next = prev
        prev = current
        current = forward
        pos+=1

    # step3 connect the left and right part of the linked list
    if left_prev:
        left_prev.next = prev
    else:
        A = prev
    tail_connect.next = current
    return A

def reverseList(A,B):
    if not A or B == 1:
        return A

    size = 0
    temp = A
    while temp:
        size+=1
        temp = temp.next
    start = 1
    end = B
    while end <= size:
        A = reverse(A, start, end)
        start+=B; end+=B

    return A

