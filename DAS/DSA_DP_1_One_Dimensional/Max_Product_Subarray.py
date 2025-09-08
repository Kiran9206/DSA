

# bruteforce solution


def max_product_subarray(A): # Time Complexity: O(N^3), Space Complexity: O(1)
    n = len(A)

    max_product = A[0]
    for start in range(n):
        for end in range(n):
            product = 1
            for k in range(start, end+1):
                product *= A[k]
            max_product = max(max_product, product)

    return max_product

A = [4, 2, -5, 1]
print(max_product_subarray(A))


# carry forward approach

def max_product_subarray1(A): # Time Complexity: O(N^2), Space Complexity: O(1)
    n = len(A)

    max_product = A[0]
    for start in range(n):
        product = 1
        for end in range(start, n):
            product *= A[end]
            max_product = max(max_product, product)

    return max_product

# kadane's algorithm

def max_product_subarray2(A): # Time Complexity: O(N), Space Complexity: O(1)
    n = len(A)

