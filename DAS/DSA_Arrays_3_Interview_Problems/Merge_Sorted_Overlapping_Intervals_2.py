# from typing import List
#
# from ansible_collections.community.general.plugins.callback.elastic import ElasticSource
#
#
# def merge_intervals(A: List[List[int, int]], B: List[int,int])-> List[List[int]]:
#     # ans = []
#     # if len(A) > 0 and len(B) > 0:
#     #     start = B[0]
#     #     end = B[1]
#     #     for idx in range(len(A)):
#     #         if A[idx][1] >= start and end >= A[idx][0]:
#     #             start = min(start,A[idx][0])
#     #             end = max(end, A[idx][1])
#     #         else:
#     #             ans.append([A[idx][0],A[idx][1]])
#     #     ans.append([start,end])
#     # return ans
#
#     # step1: initialize ans list and start and end variables...
#     ans = []
#     if len(A) > 0 and len(B) > 0:
#         start = B[0]
#         end = B[1]
#         inserted = False
#         # Step 2: Iterate over each interval in A
#         for idx in range(len(A)):
#             #step3: check if the current interval in A no overlaps with B
#             if A[idx][1] < start:
#                 ans.append(A[idx])
#             else:
#                 # step4: if there is an overlap, merge the intervals
#                 if not inserted and :
#                     start = min(start, A[idx][0])
#                     end = max(end, A[idx][1])
#     else:
#         if len(B)>0:
#             ans.append(B)
#         else:
#             return A
#
# [[1,2],[2,5],[6,9]]
# [5,4]
