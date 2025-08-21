# brute force approach

def reverse_in_range(A, B, C):
    if B < 0 or C >= len(A) or B >= C:
        return A

    while (B<C):
        A[B], A[C] = A[C], A[B]
        B+=1; C-=1
    return A

A = [1, 2, 3, 4]
B = 2
C = 3

A = [2, 5, 6]
B = 0
C = 2
print(reverse_in_range(A,B,C))