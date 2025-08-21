# brute force approach

def good_pair(A, B):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == B:
                return 1
    return 0

A = [1,2,3,4]
B = 7
A = [1,2,4]
B = 4
A = [1,2,2]
B = 4
print(good_pair(A,B))