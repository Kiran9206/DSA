# bruteforce..



def majority_element(A:list):
    n = len(A)
    if n == 1:  #edge case......
        return A[0]
    for idx in range(n - 1):
        count = 0
        for j in range(idx + 1, n):
            if A[idx] == A[j]:
                count += 1
        if count + 1 > n // 2:
            return A[idx]
    return -1


# optimised approach.....
# [2, 1, 2]

def majority_element_optimised(A:list)->int:
    count = 0; candidate = None
    for num in A:
        if count == 0:
            candidate =num
            count+=1
        elif candidate == num:
            count+=1
        else: count-=1
    # verify if candidate is actually a majority element
    freq = A.count(candidate)
    return candidate if freq > len(A) // 2 else -1  # return -1 if no majority element exists






# test case


if __name__ == "__main__":
    A = [2, 1, 2]
    print(majority_element(A))  # Output: 2

    A = [1, 1, 1]
    print(majority_element(A))  # Output: 1

    A = [3, 3, 4]
    print(majority_element(A))  # Output: 3 (no majority element)

    A = [1,2]
    print(majority_element(A))

    A = [2, 1, 2]
    print(majority_element_optimised(A))  # Output: 2

    A = [1, 1, 1]
    print(majority_element_optimised(A))  # Output: 1

    A = [3, 3, 4]
    print(majority_element_optimised(A))  # Output: 3 (no majority element)

    A = [1, 2]
    print(majority_element_optimised(A))




