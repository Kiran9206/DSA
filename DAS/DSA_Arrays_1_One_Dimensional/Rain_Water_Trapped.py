# bruteforce approach....

def rain_water_trapped(A: list) -> int:
    ans = 0
    left_max = [0] * len(A)
    right_max = [0] * len(A)
    tem_l = tem_r = 0
    for idx in range(len(A)):
        tem_l = max(tem_l, A[idx])
        left_max[idx] = tem_l

    for idx in range(len(A)-1, -1, -1):
        tem_r = max(tem_r, A[idx])
        right_max[idx] = tem_r

    for idx in range(len(A)):
        ans += min(left_max[idx], right_max[idx]) - A[idx]

    return ans


# optimised approach two pointer......


def rain_water_trapped_opt(A: list) -> int:

    ans  = left_max = right_max =0
    left = 0; right = len(A) - 1
    while left < right:
        left_max = max(A[left], left_max)
        right_max = max(A[right], right_max)

        if left_max <= right_max:
            ans += left_max - A[left]
            left+=1
        else:
            ans += right_max - A[right]
            right-=1
    return ans

