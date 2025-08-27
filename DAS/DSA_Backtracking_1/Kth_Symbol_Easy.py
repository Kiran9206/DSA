


def kth_symbol(A:int, B:int):
    # step1: base case
    if A == 1:
        return '0'
    prev = kth_symbol(A-1, B)
    ans = ['01' if ch == '0' else '10' for ch in prev]
    return ''.join(ans)

A = 4
B =4
ans = kth_symbol(A,B)
print(ans[B])

# -------------------------------------------------------------
def k_th_symbol(A:int, B:int)->int:

    # step1: base case
    if A == 1:
        return 0

    mid  = 2**(A-1) // 2 # or you can do 2**(A-2)
    if B< mid:
        return k_th_symbol(A-1,B)
    else:
        return 1 - k_th_symbol(A-1, B - mid)

print(k_th_symbol(4,4))

