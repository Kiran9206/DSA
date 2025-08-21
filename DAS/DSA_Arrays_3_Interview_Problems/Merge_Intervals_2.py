from typing import List
def merge_intervals(A: List[List[int,int]])-> List[List[int]]:
    ans = []
    if len(A) > 0:
        start = A[0][0]
        end = A[0][1]

        for idx in range(1, len(A)):
            if end >= A[idx][0]:
                start = min(start,A[idx][0])
                end = max(end, A[idx][1])
            else:
                ans.append([start,end])
                start = min(start, A[idx][0])
                end = max(end, A[idx][1])
        ans.append([start,end])
    return ans