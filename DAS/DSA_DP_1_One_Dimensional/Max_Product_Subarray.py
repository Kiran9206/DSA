

# bruteforce solution


def max_product_subarray(A): # Time Complexity: O(N^3), Space Complexity: O(1)
    n = len(A)

    max_product = A[0]
    for start in range(n):
        for end in range(start,n):
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

def max_product_subarray2(A: list)->int: # Time Complexity: O(N), Space Complexity: O(1)
    if not A:
        return 0
    # step1: create 3 variables local_max, global_max, local_min
    local_max = global_max = local_min = A[0]
    # step2: iterate over the array from 1 to N
    for idx in range(1,len(A)):

        # storing the current min and max value
        prev_max = local_max
        prev_min = local_min

        local_max = max(A[idx], prev_max * A[idx], prev_min * A[idx])
        local_min = min(A[idx], prev_max * A[idx], prev_min * A[idx])

        global_max = max(global_max, local_max)
    return global_max
