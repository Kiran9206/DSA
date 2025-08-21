# bruteforce approach.....

def n_by_3_repeat_number(A: list) -> int:

    n = len(A); candidate = -1

    for idx in range(n-1):
        count = 0
        for idx_j in range(idx + 1, n):
            if A[idx] == A[idx_j]:
                count += 1
        if count + 1 > n // 3:
            candidate = A[idx]
            break
    return candidate


# optimised approach.....

def n_by_3_repeat_number(A: list)->int:

    count = 0; candidate = None

    for num in A:
        if count == 0:
            candidate = num
            count += 1
        elif candidate == num:
            count+=1
        else: count-=1

    # verify if candidate is actually a n/3 repeat number
    freq = A.count(candidate)
    return candidate if freq > len(A) // 3 else -1  # return -1 if no n/3 repeat number exists

