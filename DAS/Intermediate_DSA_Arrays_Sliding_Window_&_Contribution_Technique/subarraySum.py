# brute force approach......

def sub_array_sum(A:list)->int:
    sumvalue = 0
    for stat in range(len(A)):
        for end in range(stat, len(A)):
            sumvalue += sum(A[stat:end+1])
    return sumvalue


A = [1, 2, 3]
print(sub_array_sum(A))


# brute force with carry forward approach.....

def sub_array_sum_carry(A:list)->int:
    sumvalue = 0
    for start in range(len(A)):
        carry = 0
        for end in range(start,len(A)):
            carry+=A[end]
            sumvalue+=carry

    return sumvalue

A = [1, 2, 3]
print(sub_array_sum_carry(A))


# optimised contribution approach......

def sub_array_sum_opt(A:list)->int:
    sumvalue = 0
    n = len(A)

    for idx in range(n):
        contribution = (idx + 1) * (n - idx)
        sumvalue+= contribution * A[idx]
    return sumvalue


A = [1, 2, 3]
print(sub_array_sum_opt(A))