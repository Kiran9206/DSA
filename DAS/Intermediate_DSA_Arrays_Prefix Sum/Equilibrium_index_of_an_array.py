# brute force approach.....
# Equilibrium Index of an Array
def equilibrium_index(A):


    left_sum = 0
    right_sum = sum(A)

    for idx in range(len(A)):
        right_sum -= A[idx]

        if left_sum == right_sum:
            return idx

        left_sum += A[idx]

    return -1

# Example usage
A = [1, 3, 5, 2, 2]
print(equilibrium_index(A))  # Output: 2 (index of the equilibrium point)

# If no equilibrium index exists, it returns -1

A = [1, 2, 3, 4, 5]
print(equilibrium_index(A))  # Output: -1 (no equilibrium index)
# Time Complexity: O(N) where N is the length of the array A.
# Space Complexity: O(1) as we are using only a constant amount of extra space.
# This approach efficiently finds the equilibrium index by maintaining a running sum of the left and right sides of the array.
# This is a simple and efficient solution to find the equilibrium index of an array.
# It iterates through the array, maintaining a running sum of the left and right sides.
# If it finds an index where the left sum equals the right sum, it returns that index.
# If no such index exists, it returns -1.

