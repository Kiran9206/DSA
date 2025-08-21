# brute force approach...

def max_subarray_brute(A:int, B:int, C:list)->int:
    ans  = -float('inf')

    for start in range(A):
        for end in range(start,A):
            maxsum=sum(C[start:end+1])
            if maxsum < B:
                ans = max(ans, maxsum)
    return ans




def max_subarray(A:int, B:int, C:list)->int:    #carryforword technique
    ans = -float('inf')
    for start in range(A):
        cur_ans = C[start]
        for end in range(start+1,A):
            cur_ans+=C[end]
            if cur_ans >= B:
                break
            if ans < cur_ans:
                ans = cur_ans
    return ans

A = 9
B = 14
C = [1,2,4,4,5,5,5,7,5]

print(max_subarray(A,B,C))

# optimized approach.......

# Only works correctly if all elements in C are non-negative.
# At no point did cur_sum reach 7 or more, so the while loop never triggered.
def max_subarray_opt(A:int, B:int, C:list)->int:  #carryforword technique + sliding window technique
    ans = -float('inf')
    cur_sum = 0
    start =0

    for end in range(A):
        cur_sum += C[end]
        # shrink the window from left....
        while cur_sum >= B and start <= end:
            cur_sum-=C[start]
            start+=1
        ans = max(ans,cur_sum)
    return ans
A = 5
B = 7
C = [4, -5, 2, 3, 1]


print(max_subarray_opt(A,B,C))
