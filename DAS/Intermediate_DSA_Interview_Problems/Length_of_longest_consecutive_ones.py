


def longest_consecutive_ones(A:str)->int:
    count_1 = A.count('1'); ans = 0

    # edge cases
    if count_1 == 0:
        return 0
    if count_1 == len(A):
        return len(A)

    for idx, item in enumerate(A):
        left_count =0; right_count = 0
        left = right = -1
        # check for zero's....
        if item == '0':
            left = idx - 1
            right = idx + 1

            # moving towards left......
            while left >= 0 and A[left] == '1':
                left_count += 1
                left -= 1

            # moving towards right.....
            while right < len(A) and A[right] == '1':
                right_count+=1
                right+=1

            # return the max count of consecutive ones
            left_overs = count_1 - left_count - right_count
            if left_overs > 0:
                local_maximum = left_count + right_count + 1
            else:
                local_maximum = left_count + right_count
            ans = max(ans, local_maximum)

    return ans

