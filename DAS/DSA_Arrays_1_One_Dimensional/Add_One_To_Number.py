# bruteforce approach....

def add_one_to_number(A:list)-> list:

    number = int(''.join(map(str, A)))  # Convert list of digits to a number
    number += 1  # Increment the number by one
    for idx in range(len(A) -1, -1, -1):
        A[idx] = number % 10
        number //= 10
    return A

A = [1, 2, 3, 4, 5]
print(add_one_to_number(A))



# optimised approach....
def add_one_to_number_optimized(A: list) -> list:
    carry = 1  # Start with carry of 1 to add one
    for i in range(len(A) - 1, -1, -1):
        A[i] += carry
        if A[i] == 10:  # If the digit becomes 10, set it to 0 and carry over
            A[i] = 0
            carry = 1
        else:
            carry = 0  # No carry needed anymore
            break
    if carry:  # If there's still a carry after the last digit
        A.insert(0, 1)  # Insert a new digit at the front
    return A


def add_one_to_number_optimized_1(A: list)-> list:
    for idx in range(len(A)-1,-1,-1):
        if A[idx] >= 9:
            A[idx] = 0
        else:
            A[idx]+=1
            return A
    # if all the numbers are 9
    A.append(1)
    A[0], A[len(A)-1] = A[len(A)-1], A[0]
    return A



# working for all the solutions.......


def add_one_to_number_optimized_2(A:list)-> list:

    n = len(A)

    carry = 1
    for idx in range(n-1,-1,-1):
        total = A[idx] + carry
        A[idx] = total % 10
        carry = total // 10

    if carry:
        A.append(carry)
        A[-1], A[0] = A[0], A[-1]

    # remove all the leading 0's
    idx = 0
    while A and A[idx] == 0:
        A.pop(0)
    return A
