
def sum_of_digits(A:int):
    # step1: set the base condition
    if A == 0:
        return 0
    # step2: calculate the last digit
    last_digit = A%10
    # step3: calculate for the remaining digits
    remaining_digits = A//10
    # step4: return the sum of last digit and the sum of remaining digits
    return last_digit + sum_of_digits(remaining_digits)