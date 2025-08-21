def kth_smallest_element(A:list, B:int):

    A.sort()
    return A[B-1]

A = [2, 1, 4, 3, 2]
B = 3
print(kth_smallest_element(A, B))