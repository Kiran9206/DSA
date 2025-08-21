# bruteforce approach.....
# step:1 - iterate an array A from 0 to n-2
# step:2 - iterate an array A from step1+1 to n-1
# step:3 - iterate an array A from step2+1 to N
# step:4 - validate the condition

def count_increasing_triplets(A:list)-> int:
    count = 0
    n = len(A)
    for idx_i in range(n - 2):
        for idx_j in range(idx_i + 1, n - 1):
            for idx_k in range(idx_j + 1, n):
                if A[idx_i] < A[idx_j] < A[idx_k]:
                    count += 1
    return count

# optimised approach....

# step1: consider every element strat from 1 to n-2 as middle element.
# step2: iterate the over the array from 1-n-2
# step3: for current element check for the left and right elements and count
#        how many left and right elements are greater and less than the current elements
# step4: multiply the left and right elements count and add it to the ans.


def count_increasing_triplets_optimised(A:list)-> int:
    n = len(A)
    ans = 0
    for idx in range(1,n-1):
        left_count = 0
        right_count = 0
        # checking for left side elements.......
        for l_idx in range(idx):
            if A[l_idx] < A[idx]:
                left_count +=1
        # checking for right side elements........
        for r_idx in range(idx+1, n):
            if A[idx] < A[r_idx]:
                right_count+=1
        ans +=(left_count * right_count)
    return ans


# Test cases
if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    print(count_increasing_triplets(A))  # Output: 10
    print(count_increasing_triplets_optimised(A))  # Output: 10

    B = [5, 4, 3, 2, 1]
    print(count_increasing_triplets(B))  # Output: 0
    print(count_increasing_triplets_optimised(B))  # Output: 0

    C = [1, 3, 2, 4]
    print(count_increasing_triplets(C))  # Output: 2
    print(count_increasing_triplets_optimised(C))  # Output: 2

    D = [1, 2, 3, 4, 5, 6]
    print(count_increasing_triplets_optimised_1(D))  # Output: 10

