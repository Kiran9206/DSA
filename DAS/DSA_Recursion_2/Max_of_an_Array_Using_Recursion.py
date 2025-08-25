

def max_of_array(A, idx=0, max=-float('inf')):

    if idx == len(A):
        return max
    if A[idx] > max:
        max = A[idx]
    return max_of_array(A, idx+1, max)


A = [12, 10, 3, 4, 5]
A = [1, -5, 80, -40]
print(max_of_array(A))