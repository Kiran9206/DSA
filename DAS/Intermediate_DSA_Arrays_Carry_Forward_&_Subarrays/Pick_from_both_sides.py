def pick_from_both_sides(A,B):

    n = len(A)
    max_sum = float('-inf')

    for idx in range(B+1):
        left = A[:idx] # removing from the front side.....
        right = A[(n - (B-idx)):] # removing from the back side.....
        current_sum = sum(left) + sum(right)
        max_sum = max(max_sum, current_sum)

    return max_sum

# overall time complexity is O(B*B) where B is the number of elements to be removed from both sides and another B is calculating the sum for each time from both the sides....


B = 3
A = [1,2,3,4,5]
print(pick_from_both_sides(A,B))

# optimised approach........... pre and postfix sum approach.......
def pick_from_both_sides_optimised(A,B):
    n = len(A)
    prefix_sum = [0] * (n + 1)
    postfix_sum = [0] * (n + 1)
    max_sum = float('-inf')

    for idx in range(1, n+1):
        prefix_sum[idx] = A[idx -1] + prefix_sum[idx - 1]

    for idx in range(n-1, -1, -1):
        postfix_sum[idx] = A[idx] + postfix_sum[idx + 1]

    for idx in range(B+1):
        left_sum = prefix_sum[idx] # removing from the front side.....
        right_sum = postfix_sum[n - (B-idx)] # removing from the back side.....
        current_sum = left_sum + right_sum
        max_sum = max(max_sum, current_sum)

    return max_sum

