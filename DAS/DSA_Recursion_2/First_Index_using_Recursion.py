

def first_index(A: list, B: int, idx: int = 0 )-> int:
    if idx == len(A):
        return -1
    if A[idx] == B:
        return idx
    return first_index(A, B, idx+1)

A = [-3, 5, 6, 2]
B = 6
A = [0, 1, 0, 2]
B = 3
print(first_index(A, B))  # Output: 2