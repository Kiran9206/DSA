# Bruteforce approach......


def sub_array_with_least_average(A: list, B: int) -> int:

    min_average = float('inf')
    result = -1
    N = len(A)
    start = 0
    end = B - 1
    while end < N:
        current_average = sum(A[start:end + 1])// B
        if current_average < min_average:
            min_average = current_average
            result = start
        start+=1; end+=1
    return result

# Example usage
A = [3, 7, 5, 20, -10, 0, 12]
B = 2

A = [18,11,16,19,11,9,8,15,3,10,9,20,1,19]
B = 1
print(sub_array_with_least_average(A, B))


# Optimised sliding window approach

def sub_array_with_least_average_opt(A: list, B: int) -> int:
    N = len(A)
    current_avgerage = sum(A[:B]) // B
    min_average = current_avgerage
    result = 0

    for idx in range(B, N):
        current_avgerage += (A[idx] - A[idx - B]) / B
        if current_avgerage < min_average:
            min_average = current_avgerage
            result = idx - B + 1
    return result

A = [18,11,16,19,11,9,8,15,3,10,9,20,1,19]
B = 1
print(sub_array_with_least_average_opt(A, B))


