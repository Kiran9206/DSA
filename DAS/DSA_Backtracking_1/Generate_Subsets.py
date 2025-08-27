


def subset(A:list, idx: int = 0, current_ans=None, ans=None):

    # step1: base case
    if current_ans is None:
        current_ans = []
    if ans is None:
        ans = []
    if idx == len(A):
        ans.append(current_ans[:])
        return ans
    #step2: select the current element
    current_ans.append(A[idx])
    subset(A, idx+1, current_ans, ans)
    # step3: backtracking.....
    current_ans.pop()  #backtracking since it's a list
    # step4: not select the current element
    subset(A, idx+1, current_ans, ans)
    return ans


A = [1,2,3]
print(subset(A))

