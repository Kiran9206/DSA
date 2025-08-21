# bruteforce approach....
from typing import List   #Time complexity: O(n^2) Space complexity: O(1)


def min_swap(A:List[int], B: int)-> int:
    n = len(A)
    # step1: find how many elements are good numbers(<=B)
    good = sum([1 for idx in A if idx <= B ])
    # step2: find how many elements are bad numbers(>B)

    # Edge case
    if good <= 1 or good == n:
        return 0

    ans = float('inf')
    for idx in range(n - good + 1):
        bad = 0
        i = idx; count = good
        while i < n and count > 0:
            if A[i] > B:
                bad += 1
            count -= 1; i += 1
        ans = min(bad, ans)

    return ans

    # optimised approach....

def min_swap_opt(A: List[int], B: int)-> int:
    n = len(A)

    # step1: find how many elements are good numbers(<=B)
    good_numbers = sum([1 for idx in A if idx <= B])
    # step2: find how many elements are bad numbers(>B) in the window of size good_numbers
    bad_numbers = sum([1 for idx in A[:good_numbers] if idx > B])
    # Edge case
    if good_numbers <= 1 or good_numbers == n:
        return 0

    ans = bad_numbers

    # step3: slide the window of size good_numbers and find the minimum bad numbers in the window
    left_side = 0; right_side = good_numbers
    while(right_side<n):
        if A[left_side] > B: #eleminating the left side element
            bad_numbers -= 1
        if A[right_side] > B: #adding the right side element
            bad_numbers += 1
        left_side+=1; right_side+=1
        ans = min(ans, bad_numbers)
    return ans










    