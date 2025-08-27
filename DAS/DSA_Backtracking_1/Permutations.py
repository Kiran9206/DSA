

def permutation(A:list, current_list = None, ans = None, tacklist = None):
    if current_list is None:
        current_list = []
    if ans is None:
        ans = []
    if tacklist is None:
        tacklist = [False] * len(A)

    # base condition
    if len(current_list) == len(A):
        ans.append(current_list[:])
        return ans

    # loop over the string A
    for idx in range(len(A)):
        if tacklist[idx] is False:
            tacklist[idx] = True
            current_list.append(A[idx])
            permutation(A, current_list, ans, tacklist)
            current_list.pop()
            tacklist[idx] = False
    return ans


A = "ABC"
A = [1,2,3]
print(permutation(A))