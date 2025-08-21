def second_largest(A):
    second_largest = -1
    largest = A[0]
    for item in A:
        if item > largest:
            largest = item
    for item in A:
        if item > second_largest and item != largest:
            second_largest = item
    return second_largest

if __name__ == "__main__":
    A = [2, 1, 2]
    A = [2]
    print(second_largest(A))