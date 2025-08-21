def prefix_sum_odd(A):
    arr = []
    if len(A) > 0:
        arr.append(0)
        for idx in range(1,len(A)):
            if idx % 2 == 0:
                sum_val = arr[idx - 1] + 0
                arr.append(sum_val)
            else:
                sum_val = arr[idx - 1] + A[idx]
                arr.append(sum_val)
    return arr

def prefix_sum_even(A):
    arr = []
    if len(A) > 0:
        arr.append(A[0])
        for idx in range(1,len(A)):
            if idx % 2 == 1:
                sum_val = arr[idx - 1] + 0
                arr.append(sum_val)
            else:
                sum_val = arr[idx - 1] + A[idx]
                arr.append(sum_val)
    return arr

def special_index(A):
    prefix_odd = prefix_sum_odd(A)
    prefix_even = prefix_sum_even(A)
    special_index_count = 0

    for idx in range(len(A)):

        odd_sum = even_sum = 0

        if idx > 0:
            odd_sum = prefix_odd[idx - 1]; even_sum = prefix_even[idx -1]

        odd_sum += (prefix_even[-1] - prefix_even[idx])
        even_sum += (prefix_odd[-1] - prefix_odd[idx])

        if odd_sum == even_sum:
            special_index_count += 1
    return special_index_count

# Example usage
A = [1, 1, 1]
print(special_index(A))  # Output: 3 (indices 0, 1, and 2 are special indices)
        

