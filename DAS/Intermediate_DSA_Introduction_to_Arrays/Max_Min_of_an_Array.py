def min_max_array(A):
    min = max = A[0]
    for idx in range(len(A)):
        if A[idx] < min:
            min = A[idx]
        if A[idx] > max:
            max = A[idx]

    return min + max

if __name__ == '__main__':
    A = [-2, 1, -4, 5, 3]
    A = [1, 3, 4, 1]
    print(min_max_array(A))
