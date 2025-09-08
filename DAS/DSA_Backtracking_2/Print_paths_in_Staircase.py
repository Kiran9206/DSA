

def staircase(A:int, current_list:list = None, ans:list = None)->list:

    if current_list is None:
        current_list = []
    if ans is None:
        ans = []

    if A < 0:
        return ans

    # base case
    elif A == 0:
        ans.append(current_list[:])
        return ans

    # I've two options 1) take 1 step 2) take 2 steps

    current_list.append(1)
    staircase(A-1, current_list, ans)
    current_list.pop()  # back tracking....
    current_list.append(2)
    staircase(A-2, current_list, ans)
    current_list.pop()  # back tracking....
    return ans


A = 3
print(staircase(A))

