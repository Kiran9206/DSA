# brute force approach.....


def special_subsequence(A:str)->int:
    pair = 0
    for idx in range(len(A)):
        if A[idx] == 'A':
            for j in range(idx+1,len(A)):
                if A[j] == 'G':
                    pair+=1
    return pair


# optimised approach.... carry forward technique...

def special_subsequence_optimised(A):
    pair = count_a = 0
    for item in A:
        if item == 'A':
            count_a+=1
        if item == 'G':
            pair+=count_a
    return pair


