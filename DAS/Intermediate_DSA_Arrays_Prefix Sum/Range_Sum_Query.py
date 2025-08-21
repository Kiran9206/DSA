# brute force approach.....


def range_sum_query(A, B):
    ans = []

    for idx in range(len(B)):
        sum = 0
        left = B[idx][0]
        right = B[idx][1]

        for i in range(left, right+1):
            sum+= A[i]
        ans.append(sum)
    return ans

A = [1, 2, 3, 4, 5]
B = [[0, 2], [1, 3], [2, 4]]
print(range_sum_query(A, B))


# Time Complexity: O(N * M) where N is the length of A and M is the number of queries in B.
# Space Complexity: O(1) for the sum variable and O(M) for the ans list.

# This is a brute force approach and may not be efficient for large inputs.

def range_sum_query_optimized(A, B):
    for i in range(1, len(A)):
        A[i] += A[i - 1]

    ans = []

    for idx in range(len(B)):
        left = B[idx][0]
        right = B[idx][1]

        if left == 0:
            ans.append(A[right])
        else: ans.append(A[right] - A[left - 1])
    return ans

A = [1, 2, 3, 4, 5]
B = [[0, 2], [1, 3], [2, 4]]
print(range_sum_query_optimized(A, B))