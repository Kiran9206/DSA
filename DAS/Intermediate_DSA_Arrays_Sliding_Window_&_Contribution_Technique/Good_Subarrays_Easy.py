# Bruteforce approach.......

def good_sub_arrays(A:list, B:int)-> int:
    count = 0
    N = len(A)
    for start in range(N):
        for end in range(start, N):
            current_sum = sum(A[start:end+1])
            length = end - start + 1
            if length % 2 == 0 and current_sum < B:
                count+=1
            elif length % 2 != 0 and current_sum > B:
                count+=1
    return count

A = [1, 2, 3, 4, 5]
B = 4
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(good_sub_arrays(A,B))


# Carry forward approach......

def good_sub_array_carry(A:list, B:int)->int:
    count = 0
    N = len(A)

    for start in range(N):
        current_sum = 0
        for end in range(start,N):
            current_sum+=A[end]
            length = end - start + 1
            if length % 2 == 0 and current_sum < B:
                count += 1
            elif length % 2 != 0 and current_sum > B:
                count += 1
    return count

A = [1, 2, 3, 4, 5]
B = 4
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(good_sub_array_carry(A,B))

# ------------------------------------------------------



