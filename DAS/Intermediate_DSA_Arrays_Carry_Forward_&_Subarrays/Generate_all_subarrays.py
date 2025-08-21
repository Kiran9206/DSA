# brute force approach.....

def subarray(A):
    ans = []
    for i in range(len(A)):
        for j in range(i, len(A)):
            tem = []
            for k in range(i, j + 1):
                tem.append(A[k])
            ans.append(tem)
    return ans

def subarray_with_slice(A):
    ans = []
    for i in range(len(A)):
        for j in range(i, len(A)):
            temp = A[i:j + 1]
            ans.append(temp)
    return ans