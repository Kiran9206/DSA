# brute force approach

def array_rotation_bruteforce(A,B):
    n = len(A)
    for b in range(B):
        temp  = A[n-1]
        for i in range(n-1, 0, -1):
            A[i] = A[i-1]
        A[0] = temp
    return A

# optimized approach using reverse method
def reverse(A, B, C):
    if B < 0 or C >= len(A) or B>= C:
        return A

    while B < C:
        A[B], A[C] = A[C], A[B]
        B+=1; C-=1

def array_rotation(A,B):
    n = len(A)
    if B < 1 or len(A) <=1:
        return A

    B = B % n  # Handle cases where B is greater than n

    reverse(A,0,n-1)
    reverse(A,0,B-1)
    reverse(A,B,n-1)
    return A

# Test the function
if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = 2
    A = [2, 5, 6]
    B = 1
    # print(array_rotation(A,B))
    print(array_rotation_bruteforce(A,B))


