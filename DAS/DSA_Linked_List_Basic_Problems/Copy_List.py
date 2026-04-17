'''
Problem Description

You are given a linked list A
Each node in the linked list contains two pointers: a next pointer and a random pointer
The next pointer points to the next node in the list
The random pointer can point to any node in the list, or it can be NULL
Your task is to create a deep copy of the linked list A
The copied list should be a completely separate linked list from the original list, but with the same node values and
random pointer connections as the original list
You should create a new linked list B, where each node in B has the same value as the corresponding node in A
The next and random pointers of each node in B should point to the corresponding nodes in B (rather than A)

Problem Constraints
0 <= |A| <= 106

Input Format
The first argument of input contains a pointer to the head of linked list A.

Output Format
Return a pointer to the head of the required linked list.

Example Input
Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1

Example Output
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
'''

class Node:

    def __init__(self,val):
        self.val = val
        self.next = self.random = None

# bruteforce
def new_ll(A):
    if not A:
        return None

    current = A
    new_head = Node(current.val)
    new_current = new_head
    current = current.next

    while current:
        new_current.next = Node(current.val)
        current = current.next
        new_current = new_current.next
    return new_head

def copy_ll(A):
    new_linked_list = new_ll(A)
    current = A
    new_current = new_linked_list

    while current:
        if current.random:
            temp = A
            index = 0
            while temp != current.random:
                temp = temp.next
                index+=1
            new_temp = new_linked_list
            for _ in range(index):
                new_temp = new_temp.next
            new_current.random = new_temp

        current = current.next
        new_current = new_current.next
    return new_linked_list

# optimised solution
def copy_ll_optimised(A):

    if not A:
        return None

    current = A
    #create duplicate nodes and insert them in between the original nodes
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    current = A
    #assign random pointers for the duplicate nodes
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    current = A
    # remove the duplicate nodes from the original list and form the new list
    new_head = A.next
    while current:
        new_node = current.next
        current.next = new_node.next
        if new_node.next:
            new_node.next = new_node.next.next
        current = current.next
    return new_head



