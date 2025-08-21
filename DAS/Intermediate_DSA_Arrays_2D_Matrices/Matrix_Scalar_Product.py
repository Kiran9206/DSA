def matrix_scalar_product(A:list, B:int)->list:
    rowlen = len(A)
    collen = len(A[0])
    for row in range(rowlen):
        for col in range(collen):
            A[row][col] *= B

    return A

if __name__ == '__main__':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    B = 2
    print(matrix_scalar_product(A,B))


