
def decreasing_increasing(n):

    # step1: set the base case
    if n == 0:
        return
    # step2: print the value in decreasing order
    print(n, end=' ')
    # step3: call the same function with n-1
    decreasing_increasing(n - 1)
    # step4: print the value in increasing order
    print(n , end=' ')


# Driver code
if __name__ == "__main__":
    n = 5
    decreasing_increasing(n)
    print()  # for a new line after the output