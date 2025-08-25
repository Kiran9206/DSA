

def is_palindrome(A,left,right):

    # step1: check base case
    if left >= right:
        return int(True)
    #step2: check if the characters at the left and right indices are equal
    if A[left] != A[right]:
        return int(False)
    # step3: move towards the center of the string
    return is_palindrome(A,left+1, right-1)