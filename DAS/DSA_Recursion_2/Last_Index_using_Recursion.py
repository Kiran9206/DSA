
def last_index(A:list, B: int, idx: int = 0):
    if idx == len(A):
        return -1

    # first recursive call to the end of the list
    last_idx = last_index(A, B, idx + 1)
    if last_idx != -1:
        return last_idx
    if A[idx] == B:
        return idx
    else:
        return -1
