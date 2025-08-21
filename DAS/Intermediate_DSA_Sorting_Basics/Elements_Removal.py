# bruteforce approach...


def remove_elements(A:list)-> int:
    A.sort(reverse=True)
    min_coast = sum(A)
    for idx in range(1,len(A)):
        min_coast += sum(A[idx : len(A)])

    return  min_coast

# using suffix sum approach...


def remove_elements_prefix_sum(A:list)-> int:
    A.sort(reverse=True); n = len(A)
    min_cost = 0
    for idx in range(n-2, -1, -1):
        A[idx] += A[idx + 1]

    for idx in range(n):
        min_cost+= A[idx]

    return min_cost

# if you don't want to modify the original array apart from the sorting, you can go with contribution technique...

def remove_elements_contribution(A:list)-> int:
    A.sort(reverse=True)
    min_cost = 0
    for idx in range(len(A)):
        min_cost += A[idx] * (idx + 1)
    return min_cost



