# core bruteforce approach to find the first missing positive integer in an array.
from typing import List

def missing_integer_core(A: List[int]) -> int:
    # step1: initialize a number to 1
    num = 1
    # step2: iterate through the array and find the number
    while True:
        if num in A:
            num += 1
        else: break
    return num



# bruteforce approach....

def missing_integer(A: List[int])-> int:

    # step1: sort the array
    A.sort()
    i = 0; num = 1
    # step2: iterate through the array
    while i < len(A):
        # edge case
        if A[i] <= 0:
            i += 1
            continue
        # duplicate cases ignore.,,
        elif A[i] < num:
            i += 1
        # if the number is equal to num, increment both
        else:
            if A[i] == num:
                i += 1
                num += 1
            else:
                break
    return num


# OPTIMISED INDEX BASED APPROACH......

def missing_integer_opt(A: List[int])->int:

    # step1 : place the elements on it's position(idx-1)
    i = 0
    while(i<len(A)):
        pos = A[i] - 1
        # case1: if the element is negative ignore
        # case2: if the element is out of bound ignore
        # case3: if the element is duplicate ignore
        if 0 < A[i] <= len(A):
            if A[i] != A[pos]:
                # case4: place the element on it's position
                A[pos], A[i] = A[i], A[pos]
            else: i += 1
        else:
            i += 1

    # step2 : iterate the array and check if idx + 1 is equals to number idx
    for idx in range(len(A)):
        # if the number is not equal to idx + 1, return idx + 1
        if A[idx] != idx + 1:
            return idx + 1

    return len(A) + 1

if __name__ == "__main__":
    A = [1, 1000000, 2]
    print(missing_integer_opt(A))
