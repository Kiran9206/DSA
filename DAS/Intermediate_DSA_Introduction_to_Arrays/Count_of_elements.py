def count_of_eleents(A):
    max_val = max(A)
    count = 0
    for item in A:
        if item < max_val:
            count+=1
    return count

if __name__ == "__main__":
    A = [1, 2, 3, 4]
    print(count_of_eleents(A))  # Output: 3
    A = [2, 5, 6]
    print(count_of_eleents(A))  # Output: 2
    A = [1, 1, 1]
    print(count_of_eleents(A))  # Output: 0