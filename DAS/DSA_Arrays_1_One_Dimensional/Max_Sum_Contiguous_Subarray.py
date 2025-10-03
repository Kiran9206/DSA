# bruteforce approach....
def max_sum_contiguous_subarray(A: list)-> int:
    ans = float('-inf')
    for start in range(len(A)):
        for end in range(start, len(A)-1):
            ans = max(ans, sum(A[start:end+1]))
    return ans

# carry forward approach...
def max_sum_contiguous_subarray1(A: list) -> int:
    ans = float('-inf')
    for start in range(len(A)):
        sum = 0
        for end in range(start, len(A)):
            sum+= A[end]
            ans = max(ans, sum)
    return ans

# optimised kadane's algorithm...
def max_sum_contiguous_subarray2(A: list) -> int:
    local_sum = global_sum = A[0]
    for idx in range(1, len(A)):
        if local_sum < 0:
            local_sum = 0
        local_sum += A[idx]
        global_sum = max(local_sum, global_sum)
    return global_sum







'''
Great! Let’s walk through how Kadane’s algorithm (or a variation of it) can be applied to different types of arithmetic subarray 
problems, including:
Maximum Subarray Sum
Minimum Subarray Sum
Maximum Subarray Product
Minimum Subarray Product
Maximum Absolute Subarray Sum
Maximum Average Subarray (conceptually related)
'''

# 1. Maximum Subarray Sum(Classic)

# step1: create two variables local_sum and global_sum
# step2: iterate through the array from 1 to N
# step3: if local_sum < 0 then local_sum = 0
# step4: local_sum += A[idx]
# step5: global_sum = max(local_sum, global_sum)

def max_sum(A:list):
    if A == 0:
        return 0
    local_max = global_max = A[0]
    for idx in range(1,len(A)):
        if local_max < 0:
            local_max = 0
        local_max += A[idx]
        global_max = max(local_max, global_max)
    return global_max

# 2. Minimum Subarray Sum

# step1: create two variables local_sum and global_sum
# step2: iterate through the array from 1 to N
# step3: if local_sum > 0 then local_sum = 0
# step4: local_sum += A[idx]
# step5: global_sum = min(local_sum, global_sum)


def min_sum(A:list):
    if A == 0:
        return 0
    local_min = global_min = A[0]
    for idx in range(1,len(A)):
        if local_min > 0:
            local_min = 0
        local_min += A[idx]
        global_min = min(local_min, global_min)
    return global_min

# 3. Maximum Subarray Product

def max_product(A: list) -> int:
    if not A:
        return 0

    local_max = local_min = global_max = A[0]

    # 3. Maximum Subarray Product

    # Step 1:
    # Initialize three variables:
    # - local_max: the maximum product that ends at the current position
    # - local_min: the minimum product that ends at the current position (important for negatives)
    # - global_max: the overall maximum product found so far
    # Set them all to the first element of the array
    local_max = local_min = global_max = A[0]

    # Step 2:
    # Iterate through the array from index 1 to the end
    for idx in range(1, len(A)):
        num = A[idx]

        # Step 3:
        # Save the previous local_max and local_min
        # because we'll need both for the current calculation
        prev_max = local_max
        prev_min = local_min

        # Step 4:
        # Compute the new local_max and local_min by considering:
        # - the current number itself (start a new subarray)
        # - the product with previous local_max (extend the positive product subarray)
        # - the product with previous local_min (could turn a negative into a positive)
        local_max = max(num, num * prev_max, num * prev_min)
        local_min = min(num, num * prev_max, num * prev_min)

        # Step 5:
        # Update the global_max if the current local_max is greater
        global_max = max(global_max, local_max)

    # Step 6:
    # Return the global_max, which holds the maximum product of any subarray
    return global_max



# Minimum Subarray Product

def min_product(A: list)-> int:
    if not A:
        return 0
    # step1: create 3 variables local_max, local_min, global_min and initialise the first element from the array value
    local_max = local_min = global_min = A[0]
    # step2: iterate the array starting from 1 to len(A)
    for idx in range (1, len(A)):
        cur_num = A[idx]
        prev_max = local_max
        prev_min = local_min
        local_max = max(cur_num, cur_num * prev_max, cur_num * prev_min)
        local_min = min(cur_num, cur_num * prev_max, cur_num * prev_min)
        # Update the global_max if the current local_max is greater
        global_min = min(global_min, local_min)
        # Return the global_max, which holds the maximum product of any subarray
    return global_min

# Maximum Absolute Subarray Sum

def max_abs_sub(A: list)-> int:

    if not A:
        return 0

    # step1: create 4 variables local_max, global_max, local_min, global_min
    local_max = global_max = local_min = global_min = A[0]

    # step2: iterate the array starting from 1 to N
    for idx in range(1,len(A)):

        local_max = max(A[idx], A[idx] + local_max)
        global_max = max(local_max, global_max)

        local_min = min(A[idx], local_min + A[idx])
        global_min = min(local_min, global_min)

    # step3: return the max of abs value..
    return max(global_max, abs(global_min))


# Maximum Average Subarray (conceptually related)

def max_avg(A: list)-> float:
    if not A:
        return 0.0
    local_sum = global_sum = A[0]; global_size = local_size = 1
    for idx in range(1,len(A)):
        if local_sum < 0:
            local_sum = 0
            local_size = 0
        local_sum += A[idx]
        local_size += 1
        if local_sum / local_size > global_sum / global_size:
            global_sum = local_sum
            global_size = local_size
    return global_sum / global_size

