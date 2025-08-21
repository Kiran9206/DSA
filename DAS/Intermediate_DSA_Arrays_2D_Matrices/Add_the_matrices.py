
def add_matrices(A:list, B:list)->list:

    result_matrix = [[0]*len(A[0]) for _ in range(len(A))]

    for row in range(len(A)):
        for col in range(len(A[0])):
            result_matrix[row][col] = A[row][col] + B[row][col]
    return result_matrix

# using list comprehension

def add_matrices1(A:list, B:list)->list:
    return [[A[row][col] + B[row][col] for col in range(len(A[0]))] for row in range(len(A))]

if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

    A = [[1, 2, 3],
         [4, 1, 2],
         [7, 8, 9]]

    B = [[9, 9, 7],
         [1, 2, 4],
         [4, 6, 3]]

    print(add_matrices(A,B))
    print(add_matrices1(A,B))


