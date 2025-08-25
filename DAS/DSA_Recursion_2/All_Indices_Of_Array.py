
def indices_of_array(A:list, B:int, idx: int, ans:list):

    # step1 : define a base condition
    if idx >= len(A):
        return ans
    #step2: check if idx of A is equal to B
    if A[idx] == B:
        ans.append(idx)
    # step3: return the same function by incrementing the idx value by 1
    return indices_of_array(A, B, idx+1, ans)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = 1
    A = []
    B = 1
    print(indices_of_array(A,B,0,[]))