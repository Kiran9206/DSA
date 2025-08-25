



def sum_of_digits(A:int)->int:

    # step1: define a base case
    if A == 0:
        return 0

    # step2: get the last digit
    last_digit = A % 10
    # step3: get the remaining number/digits
    remaining_digits = A // 10
    # step4: call the same function with the remaining digits
    return last_digit + sum_of_digits(remaining_digits)



def is_magic(A:int)->int:
    # base condition
    if A <=10:
        if A == 1 or A == 10:
            return 1
        else:
            return 0
    return is_magic(sum_of_digits(A))

A = 83557
A = 1291
print(is_magic(A))

