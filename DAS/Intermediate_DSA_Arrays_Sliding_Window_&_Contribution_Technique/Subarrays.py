# Brute force approach....


def sub_arrays(A: list, B: int)-> int:

    count = 0
    N = len(A)

    for start in range(N):
        for end in range(start, N):
            current_sum = sum(A[start: end+1])
            if current_sum < B:
                count+= 1
    return count

# Input 1:
A = [2, 5, 6]
B = 10
print(sub_arrays(A,B))
# Input 2:
A = [1, 11, 2, 3, 15]
B = 10
print(sub_arrays(A,B))


# --------------------------------------------------------

# Optimised carry forward approach....

def Sub_array_carry(A:list, B: int)->int:

    count = 0
    N = len(A)

    for start in range(N):
        current_sum = 0
        for end in range(start, N):
            current_sum+= A[end]
            if current_sum < B:
                count+=1

    return count

# Input 1:
A = [2, 5, 6]
B = 10
print(Sub_array_carry(A,B))
# Input 2:
A = [1, 11, 2, 3, 15]
B = 10
print(Sub_array_carry(A,B))

# ------------------------------------------------------------------------------

# optimised sliding window approach.....

def sub_array_slinding(A:list, B:int)->int:

    count = 0
    N = len(A)
    start = 0
    current_sum = 0
    for end in range(N):
        current_sum += A[end]

        while current_sum >= B and start <= end:
            current_sum -= A[start]
            start += 1

        # Count all subarrays from start to end
        count += (end - start + 1)

    return count

# Input 1:
A = [2, 5, 6]
B = 10
print(sub_array_slinding(A,B))
# Input 2:
A = [1, 11, 2, 3, 15]
B = 10
print(sub_array_slinding(A,B))