# Brute force approach....


def leaders(A:list)-> list:


    ans_list = []
    for idx_i in range(len(A)):
        leader = True
        for idx_j in range(idx_i+1,len(A)):
            if A[idx_i] < A[idx_j]:
                leader = False

        if leader:
            ans_list.append(A[idx_i])
    return ans_list

A = [1,10,0,5,2]
print(leaders(A))



# Optimized approach... Carry forward technique...


def leaders_optimized(A:list)-> None:
    leaders = []
    leaders.append(A[-1])  # The last element is always a leader
    max_so_far = A[-1]

    for idx in range(len(A)-2, -1, -1):
        if A[idx] > max_so_far:
            leaders.append(A[idx])
            max_so_far = A[idx]
    return leaders.reverse()

A = [1,10,0,5,2]
print(leaders(A))