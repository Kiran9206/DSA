# brute force approach.....


def closest_minmax(A):

    min_value = min(A)
    max_value = max(A)
    ans = float('inf')
    if min_value == max_value:
        return 1

    for idx in range(len(A)):
        is_min = False
        is_max = False
        for idx_1 in range(idx,len(A)):
            if A[idx_1] == min_value:
                is_min = True
            if A[idx_1] == max_value:
                is_max = True

            if is_max and is_min:
                ans = min(ans, idx_1 - idx + 1)
                break
    return ans if ans != float('inf') else 0


# optimized approach.... Carry forward approach

def closest_minmax_optimized(A):

    minimum = min(A)
    maximum = max(A)
    ans = len(A) + 1

    if minimum == maximum:
        return 1
    min_value = max_value = -1

    for idx in range(len(A)):
        if A[idx] == minimum:
            min_value = idx
            if max_value != -1:
                ans = min(ans, abs(min_value - max_value)+1)
        if A[idx] == maximum:
            max_value = idx
            if min_value != -1:
                ans = min(ans, abs(max_value - min_value)+1)
    return ans if ans != (len(A)+1) else 0


    





    